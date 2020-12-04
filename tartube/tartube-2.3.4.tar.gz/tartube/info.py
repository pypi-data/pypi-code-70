#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020 A S Lewis
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


"""Info operation classes."""


# Import Gtk modules
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject


# Import other modules
import os
import queue
import re
import signal
import subprocess
import threading


# Import our modules
import downloads
import utils
# Use same gettext translations
from mainapp import _


# Classes


class InfoManager(threading.Thread):

    """Called by mainapp.TartubeApp.info_manager_start().

    Python class to create a system child process, to do one of three jobs:

    1. Fetch a list of available formats for a video, directly from youtube-dl

    2. Fetch a list of available subtitles for a video, directly from
        youtube-dl

    3. Test youtube-dl with specified download options; everything is
        downloaded into a temporary folder

    Reads from the child process STDOUT and STDERR, having set up a
    downloads.PipeReader object to do so in an asynchronous way.

    Args:

        app_obj (mainapp.TartubeApp): The main application

        info_type (str): The type of information to fetch: 'formats' for a list
            of video formats, 'subs' for a list of subtitles, or 'test_ytdl'
            to test youtube-dl with specified options

        media_data_obj (media.Video): For 'formats' and 'subs', the media.Video
            object for which formats/subtitles should be fetched. For
            'test_ytdl', set to None

        url_string (str): For 'test_ytdl', the video URL to download (can be
            None or an empty string, if no download is required, for example
            'youtube-dl --version'. For 'formats' and 'subs', set to None

        options_string (str): For 'test_ytdl', a string containing one or more
            youtube-dl download options. The string, generated by a
            Gtk.TextView, typically contains newline and/or multiple whitespace
            characters; the info.InfoManager code deals with that. Can be None
            or an empty string, if no download options are required. For
            'formats' and 'subs', set to None

    """


    # Standard class methods


    def __init__(self, app_obj, info_type, media_data_obj, url_string,
    options_string):

        super(InfoManager, self).__init__()

        # IV list - class objects
        # -----------------------
        # The mainapp.TartubeApp object
        self.app_obj = app_obj
        # The video for which information will be fetched (None if
        #   self.info_type is 'test_ytdl')
        self.video_obj = media_data_obj

        # This object reads from the child process STDOUT and STDERR in an
        #   asynchronous way
        # Standard Python synchronised queue classes
        self.stdout_queue = queue.Queue()
        self.stderr_queue = queue.Queue()
        # The downloads.PipeReader objects created to handle reading from the
        #   pipes
        self.stdout_reader = downloads.PipeReader(self.stdout_queue)
        self.stderr_reader = downloads.PipeReader(self.stderr_queue)

        # The child process created by self.create_child_process()
        self.child_process = None


        # IV list - other
        # ---------------
        # The type of information to fetch: 'formats' for a list of video
        #   formats, 'subs' for a list of subtitles, or 'test_ytdl' to test
        #   youtube-dl with specified options
        self.info_type = info_type
        # For 'test_ytdl', the video URL to download (can be None or an empty
        #   string, if no download is required, for example
        #   'youtube-dl --version'. For 'formats' and 'subs', set to None
        self.url_string = url_string
        # For 'test_ytdl', a string containing one or more youtube-dl download
        #   options. The string, generated by a Gtk.TextView, typically
        #   contains newline and/or multiple whitespace characters; the
        #   info.InfoManager code deals with that. Can be None or an empty
        #   string, if no download options are required. For 'formats' and
        #   'subs', set to None
        self.options_string = options_string

        # Flag set to True if the info operation succeeds, False if it fails
        self.success_flag = False

        # The list of formats/subtitles extracted from STDOUT
        self.output_list = []

        # (For debugging purposes, store any STDOUT/STDERR messages received;
        #   otherwise we would just set a flag if a STDERR message was
        #   received)
        self.stdout_list = []
        self.stderr_list = []


        # Code
        # ----

        # Let's get this party started!
        self.start()


    # Public class methods


    def run(self):

        """Called as a result of self.__init__().

        Creates a child process to run the youtube-dl system command.

        Reads from the child process STDOUT and STDERR, and calls the main
        application with the result of the process (success or failure).
        """

        # Show information about the info operation in the Output Tab
        if self.info_type == 'test_ytdl':

            msg = _(
                'Starting info operation, testing downloader with specified' \
                + ' options',
            )

        else:

            if self.info_type == 'formats':

                msg = _(
                    'Starting info operation, fetching list of video/audio'\
                    + ' formats for \'{0}\'',
                ).format(self.video_obj.name)

            else:

                msg = _(
                    'Starting info operation, fetching list of subtitles'\
                    + ' for \'{0}\'',
                ).format(self.video_obj.name)

        self.app_obj.main_win_obj.output_tab_write_stdout(1, msg)

        # Convert a path beginning with ~ (not on MS Windows)
        ytdl_path = self.app_obj.check_downloader(self.app_obj.ytdl_path)
        if os.name != 'nt':
            ytdl_path = re.sub('^\~', os.path.expanduser('~'), ytdl_path)

        # Prepare the system command
        if self.info_type == 'formats':

            cmd_list = [
                ytdl_path,
                '--list-formats',
                self.video_obj.source,
            ]

        elif self.info_type == 'subs':

            cmd_list = [
                ytdl_path,
                '--list-subs',
                self.video_obj.source,
            ]

        else:

            cmd_list = [ytdl_path]

            if self.options_string is not None \
            and self.options_string != '':

                # Parse the string into a list. It was obtained from a
                #   Gtk.TextView, so it can contain newline and/or multiple
                #   whitepsace characters. Whitespace characters within
                #   double quotes "..." must be preserved
                option_list = utils.parse_options(self.options_string)
                for item in option_list:
                    cmd_list.append(item)

            if self.url_string is not None \
            and self.url_string != '':

                cmd_list.append('-o')
                cmd_list.append(
                    os.path.join(
                        self.app_obj.temp_test_dir,
                        '%(title)s.%(ext)s',
                    ),
                )

                cmd_list.append(self.url_string)

        # Create the new child process
        self.create_child_process(cmd_list)

        # Show the system command in the Output Tab
        space = ' '
        self.app_obj.main_win_obj.output_tab_write_system_cmd(
            1,
            space.join(cmd_list),
        )

        # So that we can read from the child process STDOUT and STDERR, attach
        #   a file descriptor to the PipeReader objects
        if self.child_process is not None:

            self.stdout_reader.attach_file_descriptor(
                self.child_process.stdout,
            )

            self.stderr_reader.attach_file_descriptor(
                self.child_process.stderr,
            )

        while self.is_child_process_alive():

            # Read from the child process STDOUT, and convert into unicode for
            #   Python's convenience
            while not self.stdout_queue.empty():

                stdout = self.stdout_queue.get_nowait().rstrip()
                if stdout:

                    if os.name == 'nt':
                        stdout = stdout.decode('cp1252')
                    else:
                        stdout = stdout.decode('utf-8')

                    self.output_list.append(stdout)
                    self.stdout_list.append(stdout)

                    # Show command line output in the Output Tab
                    self.app_obj.main_win_obj.output_tab_write_stdout(
                        1,
                        stdout,
                    )

        # The child process has finished
        while not self.stderr_queue.empty():

            # Read from the child process STDERR queue (we don't need to read
            #   it in real time), and convert into unicode for python's
            #   convenience
            stderr = self.stderr_queue.get_nowait().rstrip()
            if os.name == 'nt':
                stderr = stderr.decode('cp1252')
            else:
                stderr = stderr.decode('utf-8')

            if stderr:

                # While testing youtube-dl, don't treat anything as an error
                if self.info_type == 'test_ytdl':
                    self.stdout_list.append(stderr)

                # When fetching subtitles from a video that has none, don't
                #   treat youtube-dl WARNING: messages as something that
                #   makes the info operation fail
                elif self.info_type == 'subs':

                    if not re.match('WARNING\:', stderr):
                        self.stderr_list.append(stderr)

                # When fetching formats, recognise all warnings as errors
                else:
                    self.stderr_list.append(stderr)

                # Show command line output in the Output Tab
                self.app_obj.main_win_obj.output_tab_write_stderr(
                    1,
                    stderr,
                )

        # (Generate our own error messages for debugging purposes, in certain
        #   situations)
        if self.child_process is None:

            msg = _('System process did not start')
            self.stderr_list.append(msg)
            self.app_obj.main_win_obj.output_tab_write_stdout(
                1,
                msg,
            )

        elif self.child_process.returncode > 0:

            msg = _('Child process exited with non-zero code: {}').format(
                self.child_process.returncode,
            )
            self.app_obj.main_win_obj.output_tab_write_stdout(
                1,
                msg,
            )

        # Operation complete. self.success_flag is checked by
        #   mainapp.TartubeApp.info_manager_finished
        if not self.stderr_list:
            self.success_flag = True

        # Show a confirmation in the the Output Tab
        self.app_obj.main_win_obj.output_tab_write_stdout(
            1,
            _('Info operation finished'),
        )

        # Let the timer run for a few more seconds to prevent Gtk errors (for
        #   systems with Gtk < 3.24)
        GObject.timeout_add(
            0,
            self.app_obj.info_manager_halt_timer,
        )


    def create_child_process(self, cmd_list):

        """Called by self.run().

        Based on code from downloads.VideoDownloader.create_child_process().

        Executes the system command, creating a new child process which
        executes youtube-dl.

        Args:

            cmd_list (list): Python list that contains the command to execute.

        """

        info = preexec = None

        if os.name == 'nt':
            # Hide the child process window that MS Windows helpfully creates
            #   for us
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        else:
            # Make this child process the process group leader, so that we can
            #   later kill the whole process group with os.killpg
            preexec = os.setsid

        try:
            self.child_process = subprocess.Popen(
                cmd_list,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=preexec,
                startupinfo=info,
            )

        except (ValueError, OSError) as error:
            # (The code in self.run() will spot that the child process did not
            #   start)
            self.stderr_list.append(_('Child process did not start'))


    def is_child_process_alive(self):

        """Called by self.run() and .stop_info_operation().

        Based on code from downloads.VideoDownloader.is_child_process_alive().

        Called continuously during the self.run() loop to check whether the
        child process has finished or not.

        Returns:

            True if the child process is alive, otherwise returns False.

        """

        if self.child_process is None:
            return False

        return self.child_process.poll() is None


    def stop_info_operation(self):

        """Called by mainapp.TartubeApp.do_shutdown(), .stop_continue(),
        .on_button_stop_operation() and mainwin.MainWin.on_stop_menu_item().

        Based on code from downloads.VideoDownloader.stop().

        Terminates the child process.
        """

        if self.is_child_process_alive():

            if os.name == 'nt':
                # os.killpg is not available on MS Windows (see
                #   https://bugs.python.org/issue5115 )
                self.child_process.kill()

                # When we kill the child process on MS Windows the return code
                #   gets set to 1, so we want to reset the return code back to
                #   0
                self.child_process.returncode = 0

            else:
                os.killpg(self.child_process.pid, signal.SIGKILL)
