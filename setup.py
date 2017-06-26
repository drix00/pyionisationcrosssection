#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: setup

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Setup script for the project pyionizationcrosssection.
"""

###############################################################################
# Copyright 2017 Hendrix Demers
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
import os

# Third party modules.
from setuptools import setup, find_packages

# Local modules.

# Globals and constants variables.

packages = find_packages()

setup(
    name='pyionisationcrosssection',
    version='0.1',
    packages=packages,
    url='',
    license='Apache License, Version 2.0',
    author='Hendrix Demers',
    author_email='hendrix.demers@mail.mcgill.ca',
    description='Electron ionization cross section models'
)
