from src.base import SourceLocation, Target

# avy
SourceLocation(
	name = 'avy',
	vcs = 'git',
	location = 'https://bitbucket.org/arieg/extavy',
	revision = 'origin/master',
)

Target(
	name = 'avy',
	sources = [ 'avy' ],
	patches = [ 'avy.diff' ],
	license_url = 'https://bitbucket.org/arieg/avy/raw/a9685b8ba660e46fc3325797ef059cbe95adaf10/LICENSE',
)

# bitwuzla

SourceLocation(
	name = 'symfpu',
	vcs = 'git',
	location = 'https://github.com/martin-cs/symfpu',
	revision = '8fbe139bf0071cbe0758d2f6690a546c69ff0053',
)

Target(
	name = 'symfpu',
	sources = [ 'symfpu' ],
	patches = [ 'symfpu_20201114.patch' ],
	license_file = 'symfpu/LICENSE',
	license_build_only = True,
	build_native = True, # header only library
)

SourceLocation(
	name = 'bitwuzla',
	vcs = 'git',
	location = 'https://github.com/bitwuzla/bitwuzla',
	revision = 'origin/main'
)

Target(
	name = 'bitwuzla',
	sources = [ 'bitwuzla' ],
	dependencies = [ 'lingeling', 'cadical', 'btor2tools', 'symfpu' ],
	patches = [ 'Toolchain-mingw64.cmake' ],
	license_file = 'bitwuzla/COPYING',
)

# boolector

SourceLocation(
	name = 'lingeling',
	vcs = 'git',
	location = 'https://github.com/arminbiere/lingeling',
	revision = 'origin/master'
)

Target(
	name = 'lingeling',
	sources = [ 'lingeling' ],
	patches = [ 'Lingeling_20190110.patch' ],
	license_file = 'lingeling/COPYING',
	license_build_only = True,
)

SourceLocation(
	name = 'cadical',
	vcs = 'git',
	location = 'https://github.com/arminbiere/cadical',
	revision = 'origin/master'
)

Target(
	name = 'cadical',
	sources = [ 'cadical' ],
	patches = [ 'CaDiCaL_20190730.patch' ],
	license_file = 'cadical/LICENSE',
	license_build_only = True,
)

SourceLocation(
	name = 'btor2tools',
	vcs = 'git',
	location = 'https://github.com/Boolector/btor2tools',
	revision = 'origin/master'
)

Target(
	name = 'btor2tools',
	sources = [ 'btor2tools' ],
	license_file = 'btor2tools/LICENSE.txt',
	license_build_only = True,
)

SourceLocation(
	name = 'boolector',
	vcs = 'git',
	location = 'https://github.com/Boolector/boolector',
	revision = 'origin/master'
)

Target(
	name = 'boolector',
	sources = [ 'boolector' ],
	dependencies = [ 'lingeling', 'cadical', 'btor2tools' ],
	patches = [ 'Toolchain-mingw64.cmake' ],
	license_file = 'boolector/COPYING',
)

# pono

SourceLocation(
	name = 'smt-switch',
	vcs = 'git',
	location = 'https://github.com/makaimann/smt-switch',
	revision = 'e64c261faa826beb51f22ff6d5e74f581362ab47'
)

SourceLocation(
	name = 'pono',
	vcs = 'git',
	location = 'https://github.com/upscale-project/pono',
	revision = 'origin/master'
)

SourceLocation(
	name = 'cvc4',
	vcs = 'git',
	location = 'https://github.com/CVC4/CVC4.git',
	revision = '3dda54ba7e6952060766775c56969ab920430a8a'
)

SourceLocation(
	name = 'cvc5',
	vcs = 'git',
	location = 'https://github.com/cvc5/cvc5',
	revision = '77d0bec48a745e3c4acd65085f9c59bdfceed6c0'
)

Target(
	name = 'bison',
	sources = [ 'smt-switch' ],
	build_native = True,
)

Target(
	name = 'cvc5',
	sources = [ 'cvc5' ],
	patches = [ 'get-antlr-3.4' ],
	license_file = 'cvc5/COPYING',
	license_build_only = True,
)

Target(
	name = 'cvc4',
	sources = [ 'cvc4' ],
	license_file = 'cvc4/COPYING',
	license_build_only = True,
)

Target(
	name = 'smt-switch',
	sources = [ 'smt-switch' ],
	dependencies = [ 'cvc4', 'boolector', 'bison' ],
	patches = [ 'smt-switch-win32.diff' ],
	license_file = 'smt-switch/LICENSE',
	license_build_only = True,
)

Target(
	name = 'pono',
	sources = [ 'pono' ],
	dependencies = [ 'smt-switch', 'cvc4', 'boolector' ],
	license_file = 'pono/LICENSE',
)

# suprove

SourceLocation(
	name = 'suprove',
	vcs = 'git',
	location = 'https://github.com/sterin/super-prove-build',
	revision = 'origin/master'
)

Target(
	name = 'suprove',
	sources = [ 'suprove' ],
	dependencies = [ 'python2' ],
	resources = [ 'python2' ],
	patches = [ 'suprove.diff' ],
	arch = [ 'linux-x64', 'linux-arm', 'linux-arm64', 'linux-riscv64' ],
	license_file = 'suprove/pywrapper/LICENSE',
)

# yices

SourceLocation(
	name = 'yices',
	vcs = 'git',
	location = 'https://github.com/SRI-CSL/yices2',
	revision = 'origin/master'
)

Target(
	name = 'yices',
	sources = [ 'yices' ],
	license_file = 'yices/LICENSE.txt',
)

# z3

SourceLocation(
	name = 'z3',
	vcs = 'git',
	location = 'https://github.com/Z3Prover/z3',
	revision = 'origin/master'
)

Target(
	name = 'z3',
	sources = [ 'z3' ],
	license_file = 'z3/LICENSE.txt',
)

# aiger

SourceLocation(
	name = 'aiger',
	vcs = 'git',
	location = 'https://github.com/arminbiere/aiger',
	revision = 'origin/master'
)

SourceLocation(
	name = 'picosat',
	vcs = 'git',
	location = 'https://github.com/mmicko/picosat',
	revision = 'origin/main'
)

Target(
	name = 'picosat',
	sources = [ 'picosat' ],
	license_file = 'picosat/LICENSE',
	license_build_only = True,
)

Target(
	name = 'aiger',
	sources = [ 'lingeling', 'aiger' ],
	dependencies = [ 'picosat' ],
	arch = [ 'linux-x64', 'linux-arm', 'linux-arm64', 'linux-riscv64', 'darwin-x64', 'darwin-arm64' ],
	license_file = 'aiger/LICENSE',
)
