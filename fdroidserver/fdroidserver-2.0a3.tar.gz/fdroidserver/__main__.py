#!/usr/bin/env python3
#
# fdroidserver/__main__.py - part of the FDroid server tools
# Copyright (C) 2020 Michael Pöhn <michael.poehn@fsfe.org>
# Copyright (C) 2010-2015, Ciaran Gultnieks, ciaran@ciarang.com
# Copyright (C) 2013-2014 Daniel Marti <mvdan@mvdan.cc>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import sys
import os
import locale
import pkgutil
import logging

import fdroidserver.common
import fdroidserver.metadata
from fdroidserver import _
from argparse import ArgumentError
from collections import OrderedDict


COMMANDS = OrderedDict([
    ("build", _("Build a package from source")),
    ("init", _("Quickly start a new repository")),
    ("publish", _("Sign and place packages in the repo")),
    ("gpgsign", _("Add PGP signatures using GnuPG for packages in repo")),
    ("update", _("Update repo information for new packages")),
    ("deploy", _("Interact with the repo HTTP server")),
    ("verify", _("Verify the integrity of downloaded packages")),
    ("checkupdates", _("Check for updates to applications")),
    ("import", _("Add a new application from its source code")),
    ("install", _("Install built packages on devices")),
    ("readmeta", _("Read all the metadata files and exit")),
    ("rewritemeta", _("Rewrite all the metadata files")),
    ("lint", _("Warn about possible metadata errors")),
    ("scanner", _("Scan the source code of a package")),
    ("stats", _("Update the stats of the repo")),
    ("signindex", _("Sign indexes created using update --nosign")),
    ("btlog", _("Update the binary transparency log for a URL")),
    ("signatures", _("Extract signatures from APKs")),
    ("nightly", _("Set up an app build for a nightly build repo")),
    ("mirror", _("Download complete mirrors of small repos")),
])


def print_help(available_plugins=None):
    print(_("usage: ") + _("fdroid [<command>] [-h|--help|--version|<args>]"))
    print("")
    print(_("Valid commands are:"))
    for cmd, summary in COMMANDS.items():
        print("   " + cmd + ' ' * (15 - len(cmd)) + summary)
    if available_plugins:
        print(_('commands from plugin modules:'))
        for command in sorted(available_plugins.keys()):
            print('   {:15}{}'.format(command, available_plugins[command]['summary']))
    print("")


def preparse_plugin(module_name, module_dir):
    """simple regex based parsing for plugin scripts,
       so we don't have to import them when we just need the summary,
       but not plan on executing this particular plugin."""
    if '.' in module_name:
        raise ValueError("No '.' allowed in fdroid plugin modules: '{}'"
                         .format(module_name))
    path = os.path.join(module_dir, module_name + '.py')
    if not os.path.isfile(path):
        path = os.path.join(module_dir, module_name, '__main__.py')
        if not os.path.isfile(path):
            raise ValueError("unable to find main plugin script "
                             "for module '{n}' ('{d}')"
                             .format(n=module_name,
                                     d=module_dir))
    summary = None
    main = None
    with open(path, 'r', encoding='utf-8') as f:
        re_main = re.compile(r'^(\s*def\s+main\s*\(.*\)\s*:'
                             r'|\s*main\s*=\s*lambda\s*:.+)$')
        re_summary = re.compile(r'^\s*fdroid_summary\s*=\s["\'](?P<text>.+)["\']$')
        for line in f:
            m_summary = re_summary.match(line)
            if m_summary:
                summary = m_summary.group('text')
            if re_main.match(line):
                main = True

    if summary is None:
        raise NameError("could not find 'fdroid_summary' in: '{}' plugin"
                        .format(module_name))
    if main is None:
        raise NameError("could not find 'main' function in: '{}' plugin"
                        .format(module_name))
    return {'name': module_name, 'summary': summary}


def find_plugins():
    found_plugins = [{'name': x[1], 'dir': x[0].path} for x in pkgutil.iter_modules() if x[1].startswith('fdroid_')]
    plugin_infos = {}
    for plugin_def in found_plugins:
        command_name = plugin_def['name'][7:]
        try:
            plugin_infos[command_name] = preparse_plugin(plugin_def['name'],
                                                         plugin_def['dir'])
        except Exception as e:
            # We need to keep module lookup fault tolerant because buggy
            # modules must not prevent fdroidserver from functioning
            if len(sys.argv) > 1 and sys.argv[1] == command_name:
                # only raise exeption when a user specifies the broken
                # plugin in explicitly in command line
                raise e
    return plugin_infos


def main():
    available_plugins = find_plugins()

    if len(sys.argv) <= 1:
        print_help(available_plugins=available_plugins)
        sys.exit(0)

    command = sys.argv[1]
    if command not in COMMANDS and command not in available_plugins.keys():
        if command in ('-h', '--help'):
            print_help(available_plugins=available_plugins)
            sys.exit(0)
        elif command == 'server':
            print(_("""ERROR: The "server" subcommand has been removed, use "deploy"!"""))
            sys.exit(1)
        elif command == '--version':
            output = _('no version info found!')
            cmddir = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
            moduledir = os.path.realpath(os.path.dirname(fdroidserver.common.__file__) + '/..')
            if cmddir == moduledir:
                # running from git
                os.chdir(cmddir)
                if os.path.isdir('.git'):
                    import subprocess
                    try:
                        output = subprocess.check_output(['git', 'describe'],
                                                         stderr=subprocess.STDOUT,
                                                         universal_newlines=True)
                    except subprocess.CalledProcessError:
                        output = 'git commit ' + subprocess.check_output(['git', 'rev-parse', 'HEAD'],
                                                                         universal_newlines=True)
                elif os.path.exists('setup.py'):
                    import re
                    m = re.search(r'''.*[\s,\(]+version\s*=\s*["']([0-9a-z.]+)["'].*''',
                                  open('setup.py').read(), flags=re.MULTILINE)
                    if m:
                        output = m.group(1) + '\n'
            else:
                from pkg_resources import get_distribution
                output = get_distribution('fdroidserver').version + '\n'
            print(output)
            sys.exit(0)
        else:
            print(_("Command '%s' not recognised.\n" % command))
            print_help(available_plugins=available_plugins)
            sys.exit(1)

    verbose = any(s in sys.argv for s in ['-v', '--verbose'])
    quiet = any(s in sys.argv for s in ['-q', '--quiet'])

    # Helpful to differentiate warnings from errors even when on quiet
    logformat = '%(asctime)s %(levelname)s: %(message)s'
    loglevel = logging.INFO
    if verbose:
        loglevel = logging.DEBUG
    elif quiet:
        loglevel = logging.WARN

    logging.basicConfig(format=logformat, level=loglevel)

    if verbose and quiet:
        logging.critical(_("Conflicting arguments: '--verbose' and '--quiet' "
                           "can not be specified at the same time."))
        sys.exit(1)

    # Trick optparse into displaying the right usage when --help is used.
    sys.argv[0] += ' ' + command

    del sys.argv[1]
    if command in COMMANDS.keys():
        mod = __import__('fdroidserver.' + command, None, None, [command])
    else:
        mod = __import__(available_plugins[command]['name'], None, None, [command])

    system_langcode, system_encoding = locale.getdefaultlocale()
    if system_encoding is None or system_encoding.lower() not in ('utf-8', 'utf8'):
        logging.warning(_("Encoding is set to '{enc}' fdroid might run "
                          "into encoding issues. Please set it to 'UTF-8' "
                          "for best results.".format(enc=system_encoding)))

    try:
        mod.main()
    # These are ours, contain a proper message and are "expected"
    except (fdroidserver.common.FDroidException,
            fdroidserver.metadata.MetaDataException) as e:
        if verbose:
            raise
        else:
            logging.critical(str(e))
        sys.exit(1)
    except ArgumentError as e:
        logging.critical(str(e))
        sys.exit(1)
    except KeyboardInterrupt:
        print('')
        fdroidserver.common.force_exit(1)
    # These should only be unexpected crashes due to bugs in the code
    # str(e) often doesn't contain a reason, so just show the backtrace
    except Exception as e:
        logging.critical(_("Unknown exception found!"))
        raise e
    sys.exit(0)


if __name__ == "__main__":
    main()
