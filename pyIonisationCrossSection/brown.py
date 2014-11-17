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
import numpy as np

# Local modules.

# Project modules
import atomic_shell
import units

# Globals and constants variables.
class Brown1974(object):
    def __init__(self):
        self._constant_cm2keV2 = 7.92e-20

    def ics_nm2(self, atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell):
        if electronEnergy_eV/ionisationEnergy_eV < 1.0:
            return 0.0

        C = self._computeC(atomicNumber, shell)

        ionisationEnergy_keV = units.eV_to_keV(ionisationEnergy_eV)
        electronEnergy_keV = units.eV_to_keV(electronEnergy_eV)

        factor1 = C/(ionisationEnergy_keV*electronEnergy_keV)
        factor2 = np.log(electronEnergy_keV/ionisationEnergy_keV)

        sigma_cm2 = self._constant_cm2keV2*factor1*factor2

        sigma_nm2 = units.cm2_to_nm2(sigma_cm2)
        return sigma_nm2

    def _computeC(self, atomicNumber, shell):
        if shell == atomic_shell.SHELL_K:
            return self._computeCK(atomicNumber)
        elif shell == atomic_shell.SHELL_LI:
            return self._computeCLI(atomicNumber)
        elif shell == atomic_shell.SHELL_LII:
            # Same formula for LI and LII.
            return self._computeCLI(atomicNumber)
        elif shell == atomic_shell.SHELL_LIII:
            return self._computeCLIII(atomicNumber)

    def _computeCK(self, atomicNumber):
        Z = atomicNumber

        C = 0.85 + 0.0047*Z

        return C

    def SHELL_LI(self, atomicNumber):
        Z = atomicNumber

        C = 0.61 + 0.0058*Z

        return C

    def _computeCLIII(self, atomicNumber):
        Z = atomicNumber

        C = 2.19 + 0.0098*Z

        return C

def dataFigure5Casnati1982():
    # N
    atomicNumber = 7
    ionisationEnergy_eV = 0.399e3

    shell = atomic_shell.SHELL_K

    uList = np.arange(1.0, 25.0, 0.1)
    energies_eV = [U*ionisationEnergy_eV for U in uList]

    modelICS = Brown1974()
    sigmaList_nm2 = [modelICS.ics_nm2(atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell) for electronEnergy_eV in energies_eV]

    return uList, sigmaList_nm2

def run():
    import matplotlib.pyplot as plt

    uList, sigmaList_nm2 = dataFigure5Casnati1982()
    sigmaList_m2 = [units.nm2_to_m2(sigma_nm2) for sigma_nm2 in sigmaList_nm2]

    plt.figure()
    plt.plot(uList, sigmaList_m2)

    plt.show()

if __name__ == '__main__':  #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
