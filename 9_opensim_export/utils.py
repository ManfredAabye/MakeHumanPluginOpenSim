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

Hilfsfunktionen für den OpenSim-Export.
"""

import xml.etree.ElementTree as ET

def load_skeleton(file_path):
    """
    Lädt das Skelett aus der .mhskel-Datei.
    """
    skeleton = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for bone in root.findall('bone'):
            bone_name = bone.get('name')
            parent = bone.get('parent', None)
            head = bone.find('head')
            tail = bone.find('tail')

            skeleton.append({
                'name': bone_name,
                'parent': parent,
                'head': (float(head.get('x')), float(head.get('y')), float(head.get('z'))),
                'tail': (float(tail.get('x')), float(tail.get('y')), float(tail.get('z'))),
            })
    except Exception as e:
        print(f"Fehler beim Laden des Skeletts: {str(e)}")
    return skeleton


def load_weights(file_path):
    """
    Lädt die Gewichtsdaten aus der .mhw-Datei.
    """
    weights = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                vertex_id = int(parts[0])
                weights[vertex_id] = []
                for i in range(1, len(parts), 2):
                    joint = parts[i]
                    weight = float(parts[i + 1])
                    weights[vertex_id].append((joint, weight))
    except Exception as e:
        print(f"Fehler beim Laden der Gewichtsdaten: {str(e)}")
    return weights
