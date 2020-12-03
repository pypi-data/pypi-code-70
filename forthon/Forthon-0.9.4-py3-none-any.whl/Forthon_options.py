"""Define Forthon options"""

"""
This uses the obsoleted optparse since there is a horrible bug in argparse.
argparse cannot handle arguments like this
  --fargs -DMPIPARALLEL
since it insists on treating the -DMPIPARALLEL as a new argument rather than
the argument to the --fargs option. This is unbelievably stupid and would be
so easy to fix that I was stunned when I came across this. God forbid that
optparse is ever actually deleted.
"""

import sys
import os.path
import optparse
from .version import version

parser = optparse.OptionParser(
                   usage="Forthon [options] pkgname [extra Fortran or C files to be compiled or objects to link] [options for distutils]",
                   description="""
pkgname is the name of the package.
A complete package will have at least two files, the interface description
file and the fortran file. The default name for the interface file is
pkgname.v. Note that the first line of the interface file must be the package
name. The default name for the fortran file is pkgname.F

Extra files can for fortran or C files that are to be compiled and included
in the package.
""",
version=version
)

# --- This tells the optparser to stop parsing when it comes across a
# --- non-option argument (i.e. one without the preceeding '-').
# --- This first non-option argument should be the package name and possibly
# --- extra files to be compiled. Having the parser stop there allows
# --- additional arguments to be added to the command line, after the
# --- extra files, that are passed to distutils during the call to setup.
parser.disable_interspersed_args()

# --- With optparse, these need to be handled explicitly.
#parser.add_argument('pkgname', help=argparse.SUPPRESS)
#parser.add_argument('remainder', nargs=argparse.REMAINDER, help=argparse.SUPPRESS)

parser.add_option('--2to3', action='store_true', default=False, dest='do2to3', help='convert the script from Python2 to Python3')
parser.add_option('--build', action='store_true', default=True, dest='dobuild', help='build the package only, the default')
parser.add_option('--build-base', default='', help='Location where the build related temporary files are put.')
parser.add_option('--build-temp', default='', help='Location where the *pymodule.o files should be placed. This is relative to the builddir. This defaults to the builddir.')
parser.add_option('--builddir', help='Location where the temporary compilation files (such as object files) should be placed. This defaults to build/temp-osname.')

parser.add_option('--cargs', help='Additional options for the C compiler. These are passed through distutils, which does the compilation of C code. If there are any spaces in options, it must be surrounded in double quotes.')
parser.add_option('--compile_first', default='', metavar="FILE", help='The specified file is compiled first. Normally the file that is compiled first is the fortran file generated by Forthon, which would normally contain all of the modules. But if the modules are in a different file, for example, then that file would need to be compiled first and should be specified here.')

parser.add_option('-g', '--debug', action='store_true', default=False, help='Turns off optimization for fortran compiler.')
parser.add_option('-d', '--dependencies', action='append', default=[], help='Specifies that a package that the package being built depends upon. This option can be specified multiple times.')
parser.add_option('-D', '--defines', action='append', default=[], help='Defines a macro which will be inserted into the makefile. This is required in some cases where a third party library must be specified. This can be specified multiple times.')

parser.add_option('--f90', action='store_true', default=True, help='Writes wrapper code using f90, which means that python accessible variables are defined in f90 modules. This is the default.')
parser.add_option('--fargs', action='append', dest='fargslist', default=[], metavar="FARGS", help='Additional options for the fortran compiler. For example to turn on profiling. If there are any spaces in options, it must be surrounded in double quotes.')
parser.add_option('-F', '--fcomp', help='Fortran compiler. Will automatically be determined if not supplied. It can be one of the following, depending on the machine: intel8, intel, pg, absort, nag, xlf, mpxlf, xlf_r, g95, gfortran.')
parser.add_option('--fcompexec', help='The executable name of the fortran compiler, if it is different and the compiler name. The -F (--fcomp) option must also be specified.')
parser.add_option('--with_feenableexcept', action='store_true', default=False, help='Implements feenableexcept call (only supported on Linux)')
parser.add_option('--fixed_suffix', default='F', help='Suffix to use for fortran files in fixed format. Defaults to F')
parser.add_option('-f', '--fortranfile', help='Specifiy full name of main fortran file. It defaults to pkgname.F.')
parser.add_option('--fopt', help='Optimization option for the fortran compiler. This will replace the default optimization options. If there are any spaces in options, it must be surrounded in double quotes.')
parser.add_option('--free_suffix', default='F90', help='Suffix to use for fortran files in free format. Defaults to F90')

parser.add_option('--implicitnone', action='store_true', default=True, dest='implicitnone')
parser.add_option('--mpifort_compiler', help='Specifies the name of the compiler used by mpifort. This is normally the same as fcomp, but in some special cases the name can be different.')
parser.add_option('--noimplicitnone', action='store_false', default=True, dest='implicitnone', help='Specifies whether implicitnone is enforced. The default is --implicitnone.')
parser.add_option('-I', '--includedirs', action='append', default=[], help='Additional include paths')
parser.add_option('-a', '--initialgallot', action='store_true', default=False)
parser.add_option('--noinitialgallot', action='store_false', default=False, help='Specifies whether all groups will be allocated when package is imported into python. The default is --noinitialgallot.')
parser.add_option('--install', action='store_false', default=True, dest='dobuild', help='Install the package into site-packages')
parser.add_option('-i', '--interfacefile', help='Specify full name of interface file. It defaults to pkgname.v.')

parser.add_option('-l', '--libs', action='append', default=[], help="Additional libraries that are needed. Note that the prefix 'lib' and any suffixes should not be included.")
parser.add_option('-L', '--libdirs', action='append', default=[], help='Additional library paths')

parser.add_option('-t', '--machine', default=sys.platform, help='Machine type. Will automatically be determined if not supplied. Can be one of linux2, linux3, aix4, aix5, darwin, win32.')
parser.add_option('--macros', action='append', dest='othermacros', default=[], metavar="MACROS", help='Other interface files whose macros are needed')

parser.add_option('--omp', default=False, action='store_true', help="Activate OpenMP features")
parser.add_option('--ompdebug', action='store_true', default=False, help="flag to activate printing of omp debug log during execution of target program (not Forthon itself).")

parser.add_option('--pkgbase', default=None, help='Base name of code, when installed. This is use when the package is installed as part of a larger code, when the installed package name is different than the package name of the comiled module.')
parser.add_option('--pkgdir', default=None, help='Directory where files are that are to be installed with the wrapper')
parser.add_option('--pkgsuffix', default='', help='Suffix added to the name of the package when installed')

parser.add_option('--realsize', choices=['4', '8'], default='8', metavar='[4, 8]', help='The size of reals to use for variables that are declared to of type real in the variable description file. It defaults to 8.')

parser.add_option('--script', action='append', dest='scripts', help='script to be installed in the path. The option can be specified multiple times for multiple scripts.')

parser.add_option('--timeroutines', action='store_true', default=False)
parser.add_option('--notimeroutines', action='store_false', default=False, help='Specifies if timers are added for each python callable fortran routine. The default is --notimeroutines.')

parser.add_option('--underscoring', action='store_true', default=True)
parser.add_option('--nounderscoring', action='store_false', default=True, dest='underscoring', help='Specifies whether to use any underscores when doing fortran name mangling. For most systems, the default is --underscoring.')
parser.add_option('--2underscores', action='store_true', default=False, dest='twounderscores')
parser.add_option('--no2underscores', action='store_false', default=False, dest='twounderscores', help='Specifies whether or not to use second underscores when doing fortran name mangling.')

parser.add_option('-v', '--verbose', action='store_true', default=False, help='Turn on verbose output during the make process')
#parser.add_option('--version', action='version', version='%(prog)s '+version)

parser.add_option('--writemodules', action='store_true', default=True, dest='writemodules')
parser.add_option('--nowritemodules', action='store_false', default=True, dest='writemodules', help="Don't write out the module definitions. Useful if the modules have been written already. Note that if variables of derived type are used, the original code will need to be modified. See example2. Also note that if this option is used, no checks are made to ensure the consistency between the interface file description and the actual module.")




# --- Print help and then exit if no arguments are given
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

# --- Only process the true argument list when this is called from Forthon.
# --- Otherwise ignore the arguments. This is needed since for example this
# --- module may be imported by the compilers module which is used by some
# --- program other than Forthon.
if os.path.basename(sys.argv[0]).startswith('Forthon') or sys.argv[0] == '-c':
    args, extra_args = parser.parse_args()
else:
    args, extra_args = parser.parse_args(args=['dummypkg'])

# --- Hack the args to mock up the positional arguments
args.pkgname = extra_args[0]
args.remainder = extra_args[1:]
