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
import pyIonisationCrossSection.units

# Globals and constants variables.

class Jakoby1987(object):
    def __init__(self):
        self._mc2_eV = 511.0e3

    def ics_nm2(self, atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell):
        beta2 = self._computeBeta2(electronEnergy_eV)
        beta02 = self._computeBeta2(ionisationEnergy_eV)

        F1 = self._computeF1(ionisationEnergy_eV, beta2)
        F2 = self._computeF2(beta2)
        F3 = self._computeF3(beta2, beta02)
        F4 = self._computeF4(beta02)
        F5 = self._computeF5(beta2, beta02)

        a = self._computeA(atomicNumber)
        b = self._computeB(atomicNumber)
        c = self._computeC(atomicNumber)

        factor1 = a*F1
        factor2 = F2 + b*F3 + F4*np.power(F5, c)

        sigma_barn = factor1*factor2

        sigma_nm2 = units.barn_to_nm2(sigma_barn)

        return sigma_nm2

    def _computeBeta2(self, energy_eV):
        beta2 = 1.0 - np.power((1.0 + energy_eV/self._mc2_eV), -2.0)
        return beta2

    def _computeF1(self, ionisationEnergy_eV, beta2):
        IK_keV = units.eV_to_keV(ionisationEnergy_eV)
        F1 = 254.9/(IK_keV*beta2)
        return F1

    def _computeF2(self, beta2):
        F2 = np.log(beta2/(1.0 - beta2)) - beta2
        return F2

    def _computeF3(self, beta2, beta02):
        F3 = 1.0 - beta02/beta2
        return F3

    def _computeF4(self, beta02):
        F4 = np.log(1.0/beta02)
        return F4

    def _computeF5(self, beta2, beta02):
        F5 = beta02/beta2
        return F5

    def _computeA(self, atomicNumber):
        Z = atomicNumber
        a = 5.14*np.power(Z, -0.48)
        return a

    def _computeB(self, atomicNumber):
        Z = atomicNumber
        b = 5.76 - 0.04*Z
        return b

    def _computeC(self, atomicNumber):
        Z = atomicNumber
        c = 0.72 + 0.039*Z - 0.0006*Z*Z
        return c

def dataFigure1Jakoby1987():
    # N
    atomicNumber = 47
    ionisationEnergy_eV = 25517.0

    shell = None

    uList = np.arange(1.0, 50.0, 0.1).tolist()
    uList.extend(np.arange(50.0, 1.0e9/ionisationEnergy_eV, 10.0).tolist())
    energies_eV = [U*ionisationEnergy_eV for U in uList]

    modelICS = Jakoby1987()
    sigmaList_nm2 = [modelICS.ics_nm2(atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell) for electronEnergy_eV in energies_eV]

    return energies_eV, sigmaList_nm2

def run():
    import matplotlib.pyplot as plt

    energies_eV, sigmaList_nm2 = dataFigure1Jakoby1987()
    energies_keV = [units.eV_to_keV(energy_eV) for energy_eV in energies_eV]
    sigmaList_barn = [units.nm2_to_barn(sigma_nm2) for sigma_nm2 in sigmaList_nm2]

    plt.figure()
    plt.semilogx(energies_keV, sigmaList_barn)
    plt.xlim((1.0, 1.0e6))
    plt.ylim((0, 200))

    plt.show()

if __name__ == '__main__':  #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
