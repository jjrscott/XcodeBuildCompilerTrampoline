Xcode allows the compiler and linker to be overridden via `CC` and `LD`, respectively.
The usual reason for overriding the compiler is to do custom pre-processing, for example, to put logging in every function or some weird inline code generation 🤷.
The usual way is to set `CC` to your compiler and then try to get the information to your compiler with `OTHER_CFLAGS` or some other hack.

This example takes another approach I haven't seen elsewhere: set `CC=$(TARGET_TEMP_DIR)/XcodeBuildCompilerTrampolineCC.sh` the use a Build Phase to ensure`$CC` exists and contains all the info you want.
No extra flags to set, just `CC` (and the Build Phase).
