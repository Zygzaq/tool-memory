# Copyright (C) 2026  Sebastian Żmijewski (Zygzaq)
# This program is free software: you can redistribute it and/or modify it under 
# the terms of the GNU General Public License as published by the Free Software Foundation...

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import gi
gi.require_version('Gimp', '3.0')
gi.require_version('GimpUi', '3.0')
from gi.repository import Gimp, GimpUi, GObject, GLib
import locale

lang, _ = locale.getlocale()

if lang and lang.startswith("pl"):
    s_menu = "Pamięć koloru"
    s_opis = "Zapamiętuje i przywraca kolor pierwszoplanowy dla każdego narzędzia oddzielnie"
    s_opis2 = "Zapamiętuje i przywraca kolor pierwszoplanowy dla każdego narzędzia oddzielnie"
    s_msg_on = ">>> Pamięć koloru: AKTYWNA (do zamknięcia GIMPa)"    
    s_msg_ex = "Pamięć koloru: AKTYWNA (do zamknięcia GIMPa)"
else:
    s_menu = "Color Memory"
    s_opis = "Memorizing the foreground color of each tool separately"
    s_opis2 = "Memorizing the foreground color of each tool separately"
    s_msg_on = ">>> Color Memory: ACTIVE (until GIMP is closed)"
    s_msg_ex = "Color Memory: ACTIVE (until GIMP is closed)"

class ColorMemory:
    def __init__(self):
        self.color_memory = {}
        self.last_tool = None
        GLib.timeout_add(150, self.check_tool)

    def check_tool(self):
        try:
            current = Gimp.context_get_paint_method()
            if self.last_tool and self.last_tool != current:
                if current in self.color_memory:
                    s = self.color_memory[current]
                    Gimp.context_set_foreground(s['fcolor'])
            
            if current:
                self.color_memory[current] = {
                    'fcolor': Gimp.context_get_foreground()
                }
            self.last_tool = current
        except:
            pass
        return True

class ColorMemoryPlugin(Gimp.PlugIn):
    def do_set_i18n(self, name):
        return False

    def do_query_procedures(self):
        return ['python-fu-color-memory-persistent']

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name, 1, self.run, None)
        
        procedure.set_image_types("*")
        procedure.set_menu_label(s_menu)
        procedure.add_menu_path('<Image>/Tools/')
        
        procedure.set_documentation(s_opis, s_msg_ex, name)
        procedure.set_attribution("Zygzaq", "© 2026 Sebastian Żmijewski", "2026")
        return procedure

    def run(self, procedure, *args):
        ColorMemory()        
        print(s_msg_on)
        Gimp.message(s_msg_ex)
        loop = GLib.MainLoop()
        loop.run()

        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)

Gimp.main(ColorMemoryPlugin.__gtype__, sys.argv)