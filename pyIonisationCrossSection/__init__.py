#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pyIonizationCrossSection

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Different models of ionization cross section for electron
"""

###############################################################################
# Copyright 2019 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import os.path
import logging

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


def get_current_module_path(module_path, relative_path=""):
    base_path = os.path.dirname(module_path)
    logging.debug(base_path)

    filepath = os.path.join(base_path, relative_path)
    logging.debug(filepath)
    filepath = os.path.normpath(filepath)

    return filepath
