from cx_Freeze import setup, Executable
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('oyun.py',
    base=base,
    icon = "icon.ico" ) 
              ]

setup(
    name='Alya',
    version = '0.1',
    description = 'PyQt5-HelloWord',
    options = dict(build_exe = buildOptions),
    executables = executables
    )