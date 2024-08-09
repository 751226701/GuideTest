from cx_Freeze import setup, Executable

setup(
    name="YourScript",
    version="1.0",
    description="Description of Your Script",
    executables=[Executable(r"D:\APP\pycharm\project\GuideTest\GUI\Pyqt5\run.py")],

)

# python setup.py build

