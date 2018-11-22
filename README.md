# New File Nautilus Extension

This is a simple Nautilus Extension to add a "New File" context menu entry for creating new empty, ``.txt`` or ``.ods`` files.

![](https://github.com/MaxSchambach/github-binaries/blob/master/nautilus-new-file.jpg)

## Installation

From the main repository folder, run

    make
    
This installs the Nautilus extension to ``~/.local/share/nautilus-python/extensions/``.
If you need to, change the paths in the according install scripts in the `´setup`` folder.

## Uninstallation

To uninstall, simply run

    make uninstall
   
from within the repository folder. 
