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
import pyIonisationCrossSection.atomic_shell as atomic_shell
from pyIonisationCrossSection.casnati import Casnati
from pyIonisationCrossSection.brown import Brown1974
from pyIonisationCrossSection.bote2009 import Bote2009, getModel
from pyIonisationCrossSection.jakoby import Jakoby1987

# Globals and constants variables.

def dataFigure(atomicNumber, ionisationEnergy_eV, modelICS):
    shell = atomic_shell.SHELL_K

    uList = np.arange(1.0, 25.0, 0.1)
    energies_eV = [U*ionisationEnergy_eV for U in uList]

    sigmaList_nm2 = [modelICS.ics_nm2(atomicNumber, ionisationEnergy_eV, electronEnergy_eV, shell) for electronEnergy_eV in energies_eV]

    return uList, sigmaList_nm2

def run():
    import matplotlib.pyplot as plt
    import pyIonisationCrossSection.units as units

    modelICSs = {"Casnati (1982)": Casnati(), "Brown (1974)": Brown1974(), "Bote (2009)": getModel(), "Jakoby (1987)": Jakoby1987()}

    atomicNumbers = [7, 28, 79]
    ionisationEnergies = {7: 0.399e3, 28: 8.33100e3, 79: 80713.0}

    for atomicNumber in atomicNumbers:
        plt.figure()
        plt.title(r"Z = %i" % (atomicNumber))
        for modelICSName in sorted(modelICSs):
            print(modelICSName)
            uList, sigmaList_nm2 = dataFigure(atomicNumber, ionisationEnergies[atomicNumber], modelICSs[modelICSName])
            sigmaList_m2 = [units.nm2_to_m2(sigma_nm2) for sigma_nm2 in sigmaList_nm2]
            plt.plot(uList, sigmaList_m2, label=modelICSName)

        plt.xlabel("U")
        plt.ylabel(r"$\sigma_{K}$ (m$^{2}$)")
        plt.legend(loc='best')

    plt.show()

if __name__ == '__main__':  #pragma: no cover
    run()
