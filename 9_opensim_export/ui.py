#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gui3d

class OpenSimExportTask(gui3d.TaskView):
    def __init__(self, category):
        super(OpenSimExportTask, self).__init__(category, "OpenSim Export")

        # UI-Elemente
        self.label = gui3d.Label("Exportiere einen OpenSim-kompatiblen Avatar:")
        self.addWidget(self.label)

        self.export_button = gui3d.Button("Avatar exportieren")
        self.export_button.setCallback(self.export_avatar)
        self.addWidget(self.export_button)

    def export_avatar(self):
        from .export import export_avatar
        output_path = "output/opensim_avatar.dae"

        try:
            export_avatar(output_path)
            gui3d.app.msgBox("Avatar erfolgreich exportiert!", "Export abgeschlossen")
        except Exception as e:
            gui3d.app.msgBox(f"Fehler beim Export: {str(e)}", "Export-Fehler")
