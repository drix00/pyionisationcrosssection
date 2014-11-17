#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

def eV_to_keV(value_eV):
    value_keV = value_eV*1.0e-3
    return value_keV

def keV_to_eV(value_keV):
    value_eV = value_keV*1.0e3
    return value_eV

def cm2_to_nm2(value_cm2):
    value_nm2 = value_cm2*1.0e14
    return value_nm2

def nm2_to_cm2(value_nm2):
    value_cm2 = value_nm2*1.0e-14
    return value_cm2

def nm2_to_m2(value_nm2):
    value_m2 = value_nm2*1.0e-18
    return value_m2

def m2_to_nm2(value_m2):
    value_nm2 = value_m2*1.0e18
    return value_nm2

def barn_to_nm2(value_barn):
    value_m2 = barn_to_m2(value_barn)
    value_nm2 = m2_to_nm2(value_m2)
    return value_nm2

def nm2_to_barn(value_nm2):
    value_m2 = nm2_to_m2(value_nm2)
    value_barn = m2_to_barn(value_m2)
    return value_barn

def barn_to_m2(value_barn):
    value_m2 = value_barn*1.0e-28
    return value_m2

def m2_to_barn(value_m2):
    value_barn = value_m2*1.0e28
    return value_barn

if __name__ == '__main__':  #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
