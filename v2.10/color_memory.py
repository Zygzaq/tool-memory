#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2026  Sebastian Żmijewski (Zygzaq)
# This program is free software: you can redistribute it and/or modify it under 
# the terms of the GNU General Public License as published by the Free Software Foundation...

from gimpfu import *
import gtk
import gobject
import locale


lang, _ = locale.getdefaultlocale()

color_memory_timer = 160

if lang and lang.startswith("pl"):
    s_menu = "Pamięć koloru"
    s_opis = "Zapamiętuje i przywraca kolor pierwszoplanowy dla każdego narzędzia oddzielnie"
    s_msg_ex = "Pamięć koloru: AKTYWNA (do zamknięcia GIMPa)"
    s_msg_on = ">>> " + s_msg_ex
else:
    s_menu = "Color Memory"
    s_opis = "Memorizing the foreground color of each tool separately"
    s_msg_ex = "Color Memory: ACTIVE (until GIMP is closed)"
    s_msg_on = ">>> " + s_msg_ex

class ColorMemory:
    def __init__(self):
        self.color_memory = {}
        self.last_tool = None
        gobject.timeout_add(color_memory_timer, self.check_tool)

    def check_tool(self):        
        try:
            current = pdb.gimp_context_get_paint_method()
            if self.last_tool is not None and self.last_tool != current:
                if current in self.color_memory:
                    cl = self.color_memory[current]
                    pdb.gimp_context_set_foreground(cl)
            if current:
                self.color_memory[current] = (
                    pdb.gimp_context_get_foreground()
                )
            
            self.last_tool = current
        except:
            pass
        return True 

def run_zzq_color():    
    ColorMemory()
    print(s_msg_on)
    pdb.gimp_message(s_msg_ex)
    gtk.main() 

register(
    "python_fu_color_memory_persistent",
    s_opis,
    s_opis,
    "Zygzaq", "© 2026 Sebastian Żmijewski", "2026",
    s_menu,
    "*", # "" - global
    [],
    [],
    run_zzq_color,
    menu="<Image>/Tools/"
)

if __name__ == "__main__":
    main()