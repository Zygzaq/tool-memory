# Copyright (C) 2026  Sebastian Żmijewski (Zygzaq)
# This program is free software: you can redistribute it and/or modify it under 
# the terms of the GNU General Public License as published by the Free Software Foundation...

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *
import gtk
import gobject
import locale

lang, _ = locale.getdefaultlocale()

if lang and lang.startswith("pl"):
    s_menu = "Pamięć narzędzia"
    s_opis = "Zapamiętuje i przywraca parametry końcówki każdego narzędzia oddzielnie (rozmiar, kształt i zachowanie)"
    s_opis2 = "Zapamiętuje i przywraca parametry końcówki każdego narzędzia oddzielnie (rozmiar, kształt i zachowanie)"
    s_msg_on = ">>> Pamięć narzędzia: AKTYWNA (do zamknięcia GIMPa)"
    s_msg_ex = "Pamięć narzędzia: AKTYWNA (do zamknięcia GIMPa)"
else:
    s_menu = "Tool Memory"
    s_opis = "Memorizing the tip parameters of each tool separately (size, shape, and behavior)"
    s_opis2 = "Memorizing the tip parameters of each tool separately (size, shape, and behavior)"
    s_msg_on = ">>> Tool Memory: ACTIVE (until GIMP is closed)"
    s_msg_ex = "Tool Memory: ACTIVE (until GIMP is closed)"

class ToolMemory:
    def __init__(self):
        self.tool_memory = {}
        self.last_tool = None
        gobject.timeout_add(150, self.check_tool)

    def check_tool(self):        
        try:
            current = pdb.gimp_context_get_paint_method()
            if self.last_tool is not None and self.last_tool != current:
                if current in self.tool_memory:
                    brush, size, angle, ar, s, f, h, d = self.tool_memory[current]
                    pdb.gimp_context_set_brush(brush)
                    pdb.gimp_context_set_brush_size(size)
                    pdb.gimp_context_set_brush_angle(angle)
                    pdb.gimp_context_set_brush_aspect_ratio(ar)
                    pdb.gimp_context_set_brush_spacing(s)
                    pdb.gimp_context_set_brush_force(f)
                    pdb.gimp_context_set_brush_hardness(h)
                    pdb.gimp_context_set_dynamics(d)
            if current:
                self.tool_memory[current] = (
                    pdb.gimp_context_get_brush(),
                    pdb.gimp_context_get_brush_size(),
                    pdb.gimp_context_get_brush_angle(),
                    pdb.gimp_context_get_brush_aspect_ratio(),
                    pdb.gimp_context_get_brush_spacing(),
                    pdb.gimp_context_get_brush_force(),
                    pdb.gimp_context_get_brush_hardness(),
                    pdb.gimp_context_get_dynamics(),
                )
            
            self.last_tool = current
        except:
            pass
        return True

def run_zzq_tool():
    ToolMemory()
    print(s_msg_on)
    pdb.gimp_message(s_msg_ex)
    gtk.main() 

    
register(
    "python_fu_tool_memory_persistent",
    s_opis,
    s_opis2,
    "Zygzaq", "© 2026 Sebastian Żmijewski", "2026",
    s_menu,
    "*", 
    [],
    [],
    run_zzq_tool,
    menu="<Image>/Tools/"
)

if __name__ == "__main__":
    main()