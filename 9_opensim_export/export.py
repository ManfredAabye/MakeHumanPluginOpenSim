#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
**Project Name:**      MakeHuman

**Product Home Page:** http://www.makehumancommunity.org/

**Github Code Home Page:**    https://github.com/makehumancommunity/

**Authors:**           Thomas Larsson, Jonas Hauquier, [Dein Name]

**Copyright(c):**      MakeHuman Team 2001-2024

**Licensing:**         AGPL3

    This file is part of MakeHuman (www.makehumancommunity.org).

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


Abstract
--------

Der OpenSim Exporter für MakeHuman.

Dieses Modul exportiert MakeHuman-Avatare im OpenSim-kompatiblen Format.
"""

from .utils import load_skeleton, load_weights
import gui
from export import Exporter
from .opensim_bento import exportOpenSim


class ExporterOpenSim(Exporter):
    def __init__(self):
        Exporter.__init__(self)
        self.name = "OpenSim Avatar Export"
        self.filter = "OpenSim Avatar (*.dae)"
        self.fileExtension = "dae"
        self.orderPriority = 90.0

    def build(self, options, taskview):
        # Hier könnten Optionen zum Export hinzufügt werden, z. B. Checkboxen oder Radios
        self.useNormals = options.addWidget(gui.CheckBox("Use Normals", True))

    def export(self, human, filename):
        """
        Exportiert den Avatar im OpenSim-kompatiblen Format.
        """
        from .mh2opensim import exportOpenSim
        cfg = self.getConfig()
        cfg.setHuman(human)

        # Hole Daten für das Rig und die Gewichte
        rig_path = "makehuman/data/rigs/opensim_bento.mhskel"
        weights_path = "makehuman/data/rigs/opensim_bento.mhw"

        skeleton = load_skeleton(rig_path)
        weights = load_weights(weights_path)

        # Exportiere das Collada-Dokument für OpenSim
        exportOpenSim(filename, skeleton, weights, cfg)

    def getConfig(self):
        """
        Konfiguriert die Exportoptionen
        """
        cfg = OpenSimConfig()
        cfg.scale, cfg.unit = self.taskview.getScale()
        cfg.useNormals = self.useNormals.selected
        return cfg


class OpenSimConfig:
    """
    Konfigurationseinstellungen für den OpenSim-Export.
    """
    def __init__(self):
        self.useNormals = True
        self.scale = 1.0
        self.unit = "m"

    def setHuman(self, human):
        """
        Setzt den aktuellen menschlichen Avatar.
        """
        self.human = human
