# Copyright (C) 2018  Maximilian Schambach
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Nautilus extension to create new empty files.
"""
import os

try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

import gi
gi.require_version('GConf', '2.0')
from gi.repository import Nautilus, GObject, GConf


class NewFileExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        self.client = GConf.Client.get_default()

    def get_file_items(self, window, files):
        pass

    def get_background_items(self, window, file):
        # Top Menu
        top_menuitem = Nautilus.MenuItem(name='NewFileExtension::NewFileBG', 
                                         label='New File...', 
                                         tip='',
                                         icon='')

        # Sub Menu
        submenu = Nautilus.Menu()
        
        # Sub Menu Item 1: New Empty File
        sub_menuitem = Nautilus.MenuItem(name='NewFileExtension::NewFileEmptyBG', 
                                         label='New Empty File', 
                                         tip='',
                                         icon='')
        sub_menuitem.connect('activate', self.newfile_menu_background_activate_cb, file)
        submenu.append_item(sub_menuitem)

        # Sub Menu Item 2: New Empty File
        sub_menuitem = Nautilus.MenuItem(name='NewFileExtension::NewFileTxtBG', 
                                         label='New .txt File', 
                                         tip='',
                                         icon='')
        sub_menuitem.connect('activate', self.newtxt_menu_background_activate_cb, file)
        submenu.append_item(sub_menuitem)

        # Sub Menu Item 3: New Empty File
        sub_menuitem = Nautilus.MenuItem(name='NewFileExtension::NewFileOdsBG', 
                                         label='New .ods File', 
                                         tip='',
                                         icon='')
        sub_menuitem.connect('activate', self.newods_menu_background_activate_cb, file)
        submenu.append_item(sub_menuitem)

        top_menuitem.set_submenu(submenu)

        return top_menuitem,
        
    # Define Item Actions
    def _new_file(self, file):
        # Replace %20 with whitespaces
        filepath = unquote(file.get_uri()[7:])
        filepath = os.path.join(filepath, "new_file")

        os.system("touch '" + filepath + "'")

    def _new_txt_file(self, file):
        # Replace %20 with whitespaces
        filepath = unquote(file.get_uri()[7:])
        filepath = os.path.join(filepath, "new_file.txt")

        os.system("touch '" + filepath + "'")
        os.system("gnome-text-editor '" + filepath + "'")

    def _new_ods_file(self, file):
        # Replace %20 with whitespaces
        filepath = unquote(file.get_uri()[7:])
        filepath = os.path.join(filepath, "new_file.ods")
        os.system("touch '" + filepath + "'")
        os.system("soffice --writer '" + filepath + "'")

    # Define Menu callbacks
    def newfile_menu_activate_cb(self, menu, file):
        self._new_file(file)
    def newfile_menu_background_activate_cb(self, menu, file):
        self._new_file(file)

    def newtxt_menu_activate_cb(self, menu, file):
        self._new_txt_file(file)
    def newtxt_menu_background_activate_cb(self, menu, file):
        self._new_txt_file(file)

    def newods_menu_activate_cb(self, menu, file):
        self._new_ods_file(file)
    def newods_menu_background_activate_cb(self, menu, file):
        self._new_ods_file(file)


