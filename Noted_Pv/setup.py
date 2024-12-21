import sys
from cx_Freeze import setup, Executable
import os

include_files = [
    '..\\icons_pv\\Noted_P.png',
    '..\\icons_pv\\Blue_sky_icon.png',
    '..\\icons_pv\\Chatgpt_icon.png',
    '..\\icons_pv\\Chrome_icon.png',
]

include_files.append('..\\Noted_Pv\\themes.py')

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable(
        script="..\\Noted_Pv\\Noted_pv.py",
        base=base,
        icon="..\\icons_pv\\Noted_P.png",
        target_name="Noted Platinum",
    )
]

setup(
    name="Noted Platinum",
    version="1.0",
    description="Noted Platinum - The rich text editor with advanced features.",
    options={
        "build_exe": {
            "include_files": include_files,
            "optimize": 2,
        }
    },
    executables=executables,
)
