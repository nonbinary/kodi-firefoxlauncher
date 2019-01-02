# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 eira wahlin
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import xbmc, xbmcgui


firefox_path = '/usr/bin/firefox'

class BlahMainWindow(xbmcgui.Window):
        # and define it as self
        def __init__(self):
            # add picture control to our window (self) with a hardcoded path name to picture
            self.addControl(xbmcgui.ControlImage(0,0,300,225, '/home/panina/Hämtningar/plugin.program.advanced.emulator.launcher/media/p_pixel/Commodore Plus-4.png'))

def main():
    # store our window as a short variable for easy of use
    W = BlahMainWindow()
    # run our window we created with our background jpeg image
    W.doModal()
    # after the window is closed, Destroy it.
    del W

    # stored for future reference 
    #xbmc.executebuiltin("action(reloadkeymaps)")

if __name__ == "__main__":
    main()
