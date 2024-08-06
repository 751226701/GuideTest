from cx_Freeze import setup, Executable

setup(
    name="YourScript",
    version="1.0",
    description="Description of Your Script",
    executables=[Executable(r"finance.py")],

)

# python setup.py build

