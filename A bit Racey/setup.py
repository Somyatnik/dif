import cx_Freeze

executables = [cx_Freeze.Executable("A bit Racey.py")]

cx_Freeze.setup(
    name = "A bit Racey",
    options = {"build_exe": {"packages":["pygame"],
                             "include_files":["racecar_sh.png"]}},
    executables = executables
    )
