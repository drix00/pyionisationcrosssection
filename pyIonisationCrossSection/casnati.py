#!/usr/bin/env python
"""
.. py:currentmodule:: casnati
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Electron ionisation cross section from Casnati (1982).
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
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
import pyIonisationCrossSection.atomic_shell

# Globals and constants variables.

class Casnati(object):
    def __init__(self):
        self._firstBohrRadius_m = 5.292e-11
        self._mc2_eV = 511.0e3
        self._RydbergEnergy_eV = 13.606

    def ics_nm2(self, atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell):
        U = electronEnergy_eV/ionisationEnergy_eV
        if U < 1.0:
            return 0.0

        R = self._computeRelativisticFactor(ionisationEnergy_eV, U)

        numberElectronsShell = self._getNumberElectronsShell(atomicNumber, shell)
        n = numberElectronsShell

        a0_nm = self._firstBohrRadius_m*1.0e9

        psi = self._computePsi(ionisationEnergy_eV, U)

        phi = self._computePhi(U)

        factor1 = np.power(self._RydbergEnergy_eV/ionisationEnergy_eV, 2.0)

        sigma_nm2 = n*a0_nm*a0_nm*R*factor1*psi*phi*np.log(U)/U

        return sigma_nm2

    def _computeRelativisticFactor(self, ionisationEnergy_eV, U):
        J = self._mc2_eV/ionisationEnergy_eV

        nominator = 1.0 + 2.0*J
        denominator = U + 2.0*J
        factor1 = nominator/denominator

        nominator = U + J
        denominator = 1.0 + J
        factor2 = np.power(nominator/denominator, 2.0)

        nominator = (1.0 + U)*(U + 2.0*J)*(1.0 + J)*(1.0 + J)
        denominator = J*J*(1.0 + 2.0*J) + U*(U + 2.0*J)*(1.0 + J)*(1.0 + J)
        factor3 = np.power(nominator/denominator, 3.0/2.0)

        R = factor1*factor2*factor3

        return R

    def _getNumberElectronsShell(self, atomicNumber, shell):
        if shell == atomic_shell.SHELL_K:
            return 2
        elif shell == atomic_shell.SHELL_LIII:
            return 4
        elif shell == atomic_shell.SHELL_MV:
            return 9

    def _computePsi(self, ionisationEnergy_eV, U):
        # d0 = d0' + 2
        d0 = -0.0318
        d1 = 0.3160
        d2 = -0.1135

        exponant = d0 + d1/U + d2/(U*U)
        ratio = ionisationEnergy_eV/self._RydbergEnergy_eV

        psi = np.power(ratio, exponant)

        return psi

    def _computePhi(self, U):
        # b0 = b0'/(a0*a0)
        # b0' = 2.960e-20 m2
        b0 = 10.57
        b1 = -1.736
        b2 = 0.317

        phi = b0*np.exp(b1/U + b2/(U*U))

        return phi

def dataFigure5():
    # N
    atomicNumber = 7
    ionisationEnergy_eV = 0.399e3

    shell = atomic_shell.SHELL_K

    uList = np.arange(1.0, 25.0, 0.1)
    energies_eV = [U*ionisationEnergy_eV for U in uList]

    modelICS = Casnati()
    sigmaList_nm2 = [modelICS.ics_nm2(atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell) for electronEnergy_eV in energies_eV]

    return uList, sigmaList_nm2

def dataFigure6():
    # N
    atomicNumber = 28
    ionisationEnergy_eV = 8.33100e3

    shell = atomic_shell.SHELL_K

    uList = np.arange(1.0, 25.0, 0.1)
    energies_eV = [U*ionisationEnergy_eV for U in uList]

    modelICS = Casnati()
    sigmaList_nm2 = [modelICS.ics_nm2(atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell) for electronEnergy_eV in energies_eV]

    return uList, sigmaList_nm2

def dataFigure7():
    # N
    atomicNumber = 79
    ionisationEnergy_eV = 80713.0

    shell = atomic_shell.SHELL_K

    uList = np.arange(1.0, 25.0, 0.1)
    energies_eV = [U*ionisationEnergy_eV for U in uList]

    modelICS = Casnati()
    sigmaList_nm2 = [modelICS.ics_nm2(atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell) for electronEnergy_eV in energies_eV]

    return uList, sigmaList_nm2

def run():
    import matplotlib.pyplot as plt
    import units

    for dataFigure in [dataFigure5, dataFigure6, dataFigure7]:
        uList, sigmaList_nm2 = dataFigure()
        sigmaList_m2 = [units.nm2_to_m2(sigma_nm2) for sigma_nm2 in sigmaList_nm2]
        plt.figure()
        plt.plot(uList, sigmaList_m2)

    plt.show()

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
