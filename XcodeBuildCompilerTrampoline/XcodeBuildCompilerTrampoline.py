#!python3

import os
import stat
import sys

if 'CC' in os.environ:
    trampoline_script_content = f"""#!{os.environ['SHELL']}
echo CC has be intercepted by XcodeBuildCompilerTrampoline
echo Edit {sys.argv[0]} to access the build phase enivornment at compile time
export PATH={os.environ['PATH']}
clang $*
"""

    with open(os.environ['CC'], "w") as f:
        f.write(trampoline_script_content)
    st = os.stat(os.environ['CC'])
    os.chmod(os.environ['CC'], st.st_mode | stat.S_IEXEC)

if 'LD' in os.environ:
    trampoline_script_content = f"""#!{os.environ['SHELL']}
echo LD has be intercepted by XcodeBuildCompilerTrampoline
echo Edit {sys.argv[0]} to access the build phase enivornment at link time
export PATH={os.environ['PATH']}
clang $*
"""

    with open(os.environ['LD'], "w") as f:
        f.write(trampoline_script_content)
    st = os.stat(os.environ['LD'])
    os.chmod(os.environ['LD'], st.st_mode | stat.S_IEXEC)
