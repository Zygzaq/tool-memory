#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2026  Sebastian Żmijewski (Zygzaq)
# This program is free software: you can redistribute it and/or modify it under 
# the terms of the GNU General Public License as published by the Free Software Foundation...

import sys
import gi
gi.require_version('Gimp', '3.0')
gi.require_version('GimpUi', '3.0')
from gi.repository import Gimp, GimpUi, GObject, GLib
import locale

lang, _ = locale.getlocale()

tool_memory_timer = 160

if lang and lang.startswith("pl"):
    s_menu = "Pamięć narzędzia"
    s_opis = "Zapamiętuje parametry końcówki każdego narzędzia oddzielnie (rozmiar, kształt i zachowanie)"
    s_msg_ex = "Pamięć narzędzia: AKTYWNA (do zamknięcia GIMPa)"
    s_msg_on = ">>> "+s_msg_ex
else:
    s_menu = "Tool Memory"
    s_opis = "Memorizing the tip parameters of each tool separately (size, shape, and behavior)"
    s_msg_ex = "Tool Memory: ACTIVE (until GIMP is closed)"
    s_msg_on = ">>> "+s_msg_ex

class ToolMemory:
    def __init__(self):
        self.tool_memory = {}
        self.last_tool = None
        GLib.timeout_add(tool_memory_timer, self.check_tool)

    def check_tool(self):
        try:
            current = Gimp.context_get_paint_method()
            if self.last_tool and self.last_tool != current:
                if current in self.tool_memory:
                    s = self.tool_memory[current]
                    Gimp.context_set_brush(s['brush'])
                    Gimp.context_set_brush_size(s['size'])
                    Gimp.context_set_brush_angle(s['angle'])
                    Gimp.context_set_brush_aspect_ratio(s['aspect'])
                    Gimp.context_set_brush_spacing(s['spacing'])
                    Gimp.context_set_brush_hardness(s['hardness'])
            
            if current:
                self.tool_memory[current] = {
                    'brush': Gimp.context_get_brush(),
                    'size': Gimp.context_get_brush_size(),
                    'angle': Gimp.context_get_brush_angle(),
                    'aspect': Gimp.context_get_brush_aspect_ratio(),
                    'spacing': Gimp.context_get_brush_spacing(),
                    'hardness': Gimp.context_get_brush_hardness()
                }
            self.last_tool = current
        except:
            pass
        return True

class ToolMemoryPlugin(Gimp.PlugIn):
    def do_set_i18n(self, name):
        return False

    def do_query_procedures(self):
        return ['python-fu-tool-memory-persistent']

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name, 1, self.run, None)
        
        procedure.set_image_types("*")
        procedure.set_menu_label(s_menu)
        procedure.add_menu_path('<Image>/Tools/')
        
        procedure.set_documentation(s_opis, s_msg_ex, name)
        procedure.set_attribution("Zygzaq", "© 2026 Sebastian Żmijewski", "2026")
        return procedure

    def run(self, procedure, *args):
        ToolMemory()        
        print(s_msg_on)
        Gimp.message(s_msg_ex)
        loop = GLib.MainLoop()
        loop.run()

        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)

Gimp.main(ToolMemoryPlugin.__gtype__, sys.argv)
