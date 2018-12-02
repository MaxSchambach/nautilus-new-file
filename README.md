# New File Nautilus Extension

This is a simple Nautilus Extension to add a "New File" context menu entry for creating new empty, ``.txt`` or ``.ods`` files.

![](https://github.com/MaxSchambach/github-binaries/blob/master/nautilus-new-file.png)

## Installation

From the main repository folder, run

    mkdir build
    cd build
    cmake ..
    make
    make install
    
This installs the Nautilus extension to ``~/.local/share/nautilus-python/extensions/``.
If you need to, change the path in the `CMakeLists.txt` file.

## Uninstallation

To uninstall, simply run

    make uninstall
   
from within the `build` folder. 
