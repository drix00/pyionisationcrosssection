#!/usr/bin/env python
"""
.. py:currentmodule:: bote2009
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Implementation of Bote Salvat ionization cross section.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import logging
import os.path
import csv

# Third party modules.
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import physical_constants

# Local modules.
import pyHendrixDemersTools.Files as Files
import pyHendrixDemersTools.NumericConversion as NumericConversion

# Project modules

# Globals and constants variables.
KEY_FACTORS_A = "Z,S,,a1,a2,a3,a4,a5"
KEY_FACTORS_D = "Z,S,,d1,d2,d3,d4,d5"
KEY_FACTORS_G = "Z,S,b-,b+,Anlj,g1,g2,g3,g4"

KEY_NEW_ATOMIC_NUMBER = ",,,,,,,"

PARTICLE_ELECTRON = "Electron"
PARTICLE_POSITRON = "Positron"

SUBSHELL_K = "K"
SUBSHELL_L1 = "L1"
SUBSHELL_L2 = "L2"
SUBSHELL_L3 = "L3"
SUBSHELL_M1 = "M1"
SUBSHELL_M2 = "M2"
SUBSHELL_M3 = "M3"
SUBSHELL_M4 = "M4"
SUBSHELL_M5 = "M5"

KEY_ATOMIC_NUMBER = "Z"
KEY_SUBSHELL = "Subshell"
KEY_Eca_eV = "Ec (eV)"
KEY_Ecd_eV = "Ecd (eV)"
KEY_a1 = "a1"
KEY_a2 = "a2"
KEY_a3 = "a3"
KEY_a4 = "a4"
KEY_a5 = "a5"

KEY_d1 = "d1"
KEY_d2 = "d2"
KEY_d3 = "d3"
KEY_d4 = "d4"
KEY_d5 = "d5"

KEY_B_ELECTRON = "b-"
KEY_B_POSITRON = "b+"
KEY_A_SUBSHELL = "Anlj"
KEY_g1 = "g1"
KEY_g2 = "g2"
KEY_g3 = "g3"
KEY_g4 = "g4"

class Bote2009(object):
    def __init__(self):
        self.data = {}

    def readOriginalDataFile(self, dataFilepath):
        lines = open(dataFilepath, "r").readlines()

        isReadingFactorsA = False
        isReadingFactorsD = False
        isReadingFactorsG = False
        isNewAtomicNumber = False

        _lineNumber = 1
        for line in lines:
            line = line.strip()
            #logging.debug("%4i %s", _lineNumber, line)
            _lineNumber += 1

            if line == KEY_FACTORS_A:
                isReadingFactorsA = True
                isReadingFactorsD = False
                isReadingFactorsG = False
                isNewAtomicNumber = True
                continue
            elif line == KEY_FACTORS_D:
                isReadingFactorsA = False
                isReadingFactorsD = True
                isReadingFactorsG = False
                isNewAtomicNumber = True
                continue
            elif line == KEY_FACTORS_G:
                isReadingFactorsA = False
                isReadingFactorsD = False
                isReadingFactorsG = True
                isNewAtomicNumber = True
                continue
            elif line == KEY_NEW_ATOMIC_NUMBER:
                isNewAtomicNumber = True
                continue
            elif line == "":
                if isReadingFactorsD or isReadingFactorsG:
                    isNewAtomicNumber = True
                continue
            elif line.startswith("Table"):
                isReadingFactorsA = False
                isReadingFactorsD = False
                isReadingFactorsG = False
                continue

            if isReadingFactorsA:
                items = line.split(',')
                if isNewAtomicNumber:
                    atomicNumber = int(items[0])
                    subshell = str(items[1])
                    ionizationEnergy_eV = float(items[2])
                    a1 = float(items[3])
                    a2 = float(items[4])
                    a3 = float(items[5])
                    a4 = float(items[6])
                    a5 = float(items[7])
                    isNewAtomicNumber = False
                else:
                    subshell = str(items[0])
                    ionizationEnergy_eV = float(items[1])
                    a1 = float(items[2])
                    a2 = float(items[3])
                    a3 = float(items[4])
                    a4 = float(items[5])
                    a5 = float(items[6])

                self.data.setdefault(atomicNumber, {})
                self.data[atomicNumber].setdefault(subshell, {})
                self.data[atomicNumber][subshell][KEY_Eca_eV] = ionizationEnergy_eV
                self.data[atomicNumber][subshell][KEY_a1] = a1
                self.data[atomicNumber][subshell][KEY_a2] = a2
                self.data[atomicNumber][subshell][KEY_a3] = a3
                self.data[atomicNumber][subshell][KEY_a4] = a4
                self.data[atomicNumber][subshell][KEY_a5] = a5

            if isReadingFactorsD:
                items = line.split(',')
                if isNewAtomicNumber:
                    atomicNumber = int(items[0])
                    subshell = str(items[1])
                    ionizationEnergy_eV = float(items[2])
                    d1 = float(items[3])
                    d2 = float(items[4])
                    d3 = float(items[5])
                    d4 = float(items[6])
                    d5 = float(items[7])
                    isNewAtomicNumber = False
                else:
                    subshell = str(items[0])
                    ionizationEnergy_eV = float(items[1])
                    d1 = float(items[2])
                    d2 = float(items[3])
                    d3 = float(items[4])
                    d4 = float(items[5])
                    d5 = float(items[6])

                self.data.setdefault(atomicNumber, {})
                self.data[atomicNumber].setdefault(subshell, {})
                self.data[atomicNumber][subshell][KEY_Ecd_eV] = ionizationEnergy_eV
                self.data[atomicNumber][subshell][KEY_d1] = d1
                self.data[atomicNumber][subshell][KEY_d2] = d2
                self.data[atomicNumber][subshell][KEY_d3] = d3
                self.data[atomicNumber][subshell][KEY_d4] = d4
                self.data[atomicNumber][subshell][KEY_d5] = d5

            if isReadingFactorsG:
                items = line.split(',')
                if isNewAtomicNumber:
                    atomicNumber = int(items[0])
                    subshell = str(items[1])
                    bElectron = float(items[2])
                    bPositron = float(items[3])
                    Anlj = float(items[4])
                    g1 = float(items[5])
                    g2 = float(items[6])
                    g3 = float(items[7])
                    g4 = float(items[8])
                    isNewAtomicNumber = False
                else:
                    subshell = str(items[0])
                    bElectron = float(items[1])
                    bPositron = float(items[2])
                    Anlj = float(items[3])
                    g1 = float(items[4])
                    g2 = float(items[5])
                    g3 = float(items[6])
                    g4 = float(items[7])

                self.data.setdefault(atomicNumber, {})
                self.data[atomicNumber].setdefault(subshell, {})
                self.data[atomicNumber][subshell][KEY_B_ELECTRON] = bElectron
                self.data[atomicNumber][subshell][KEY_B_POSITRON] = bPositron
                self.data[atomicNumber][subshell][KEY_A_SUBSHELL] = Anlj
                self.data[atomicNumber][subshell][KEY_g1] = g1
                self.data[atomicNumber][subshell][KEY_g2] = g2
                self.data[atomicNumber][subshell][KEY_g3] = g3
                self.data[atomicNumber][subshell][KEY_g4] = g4

    def createTabulatedDataFile(self, dataFilepath):
        self.readOriginalDataFile(dataFilepath)

        path = os.path.dirname(dataFilepath)
        filename = "bote2009_Parameters.csv"
        filepath = os.path.join(path, filename)
        assert filepath != dataFilepath

        fieldsname = [KEY_ATOMIC_NUMBER, KEY_SUBSHELL, KEY_Eca_eV, KEY_a1, KEY_a2, KEY_a3, KEY_a4, KEY_a5,
                      KEY_d1, KEY_d2, KEY_d3, KEY_d4, KEY_d5,
                      KEY_B_ELECTRON, KEY_B_POSITRON, KEY_A_SUBSHELL, KEY_g1, KEY_g2, KEY_g3, KEY_g4]

        writer = csv.DictWriter(open(filepath, 'wb'), fieldsname)

        for atomicNumber in self.data:
            for subshell in self.data[atomicNumber]:
                data = self.data[atomicNumber][subshell]
                del data[KEY_Ecd_eV]
                data[KEY_ATOMIC_NUMBER] = atomicNumber
                data[KEY_SUBSHELL] = subshell

                writer.writerow(data)

    def readTabulatedDataFile(self, dataFilepath):
        fieldsname = [KEY_ATOMIC_NUMBER, KEY_SUBSHELL, KEY_Eca_eV, KEY_a1, KEY_a2, KEY_a3, KEY_a4, KEY_a5,
                      KEY_d1, KEY_d2, KEY_d3, KEY_d4, KEY_d5,
                      KEY_B_ELECTRON, KEY_B_POSITRON, KEY_A_SUBSHELL, KEY_g1, KEY_g2, KEY_g3, KEY_g4]

        reader = csv.DictReader(open(dataFilepath, 'r'), fieldsname)

        for row in reader:
            atomicNumber = int(row[KEY_ATOMIC_NUMBER])
            subshell = row[KEY_SUBSHELL]
            self.data.setdefault(atomicNumber, {})
            self.data[atomicNumber].setdefault(subshell, {})

            self.data[atomicNumber][subshell] = row
            self.data[atomicNumber][subshell][KEY_Ecd_eV]  = row[KEY_Eca_eV]
            del self.data[atomicNumber][subshell][KEY_ATOMIC_NUMBER]
            del self.data[atomicNumber][subshell][KEY_SUBSHELL]
            for key in self.data[atomicNumber][subshell]:
                self.data[atomicNumber][subshell][key] = float(self.data[atomicNumber][subshell][key])

    def crossSection_cm2(self, energy_eV, atomicNumber, subshell, particle):
        if particle == PARTICLE_ELECTRON:
            ionizationEnergy_eV = self.data[atomicNumber][subshell][KEY_Eca_eV]
            factorB = self.data[atomicNumber][subshell][KEY_B_ELECTRON]
        elif particle == PARTICLE_POSITRON:
            ionizationEnergy_eV = self.data[atomicNumber][subshell][KEY_Ecd_eV]
            factorB = self.data[atomicNumber][subshell][KEY_B_POSITRON]

        if energy_eV > 16.0 * ionizationEnergy_eV:
            crossSectionPWBA_cm2 = self._computeCrossSectionPWBA(energy_eV, atomicNumber, subshell)
            scalingFactor = energy_eV / (energy_eV + factorB*ionizationEnergy_eV)
            crossSection_cm2 = scalingFactor * crossSectionPWBA_cm2
        else:
            if particle == PARTICLE_ELECTRON:
                overvoltage = energy_eV/ionizationEnergy_eV
                crossSection_cm2 = self._computeCrossSectionDWBAElectron(overvoltage, atomicNumber, subshell)
            elif particle == PARTICLE_POSITRON:
                overvoltage = energy_eV/ionizationEnergy_eV
                crossSection_cm2 = self._computeCrossSectionDWBAPositron(overvoltage, atomicNumber, subshell)

        return crossSection_cm2

    def _computeCrossSectionDWBAElectron(self, overvoltage, atomicNumber, subshell):
        if overvoltage < 1.0:
            return 0.0

        U = overvoltage

        a0_m = physical_constants["Bohr radius"][0]
        a0_cm = NumericConversion.m_To_cm(a0_m)

        a1 = self.data[atomicNumber][subshell][KEY_a1]
        a2 = self.data[atomicNumber][subshell][KEY_a2]
        a3 = self.data[atomicNumber][subshell][KEY_a3]
        a4 = self.data[atomicNumber][subshell][KEY_a4]
        a5 = self.data[atomicNumber][subshell][KEY_a5]

        factorA_cm2 = 4.0 * np.pi * a0_cm * a0_cm * (U - 1.0) / (U * U)
        factorB = a1 + a2 * U + a3 / (1.0 + U) + a4 / np.power(1.0 + U, 3.0) + a5 / np.power(1.0 + U, 5.0)

        crossSection_cm2 = factorA_cm2 * factorB * factorB
        assert crossSection_cm2 >= 0.0

        return crossSection_cm2

    def _computeCrossSectionDWBAPositron(self, overvoltage, atomicNumber, subshell):
        if overvoltage < 1.0:
            return 0.0

        U = overvoltage

        a0_m = physical_constants["Bohr radius"][0]
        a0_cm = NumericConversion.m_To_cm(a0_m)

        d1 = self.data[atomicNumber][subshell][KEY_d1]
        d2 = self.data[atomicNumber][subshell][KEY_d2]
        d3 = self.data[atomicNumber][subshell][KEY_d3]
        d4 = self.data[atomicNumber][subshell][KEY_d4]
        d5 = self.data[atomicNumber][subshell][KEY_d5]

        factorA_cm2 = 4.0 * np.pi * a0_cm * a0_cm * (U - 1.0) / (U * U)
        factorB = d1 + d2 * U + d3 / (1.0 + U) + d4 * np.sqrt(U) / np.power(1.0 + U, 3.0) + d5 * U / np.power(1.0 + U, 5.0)

        crossSection_cm2 = factorA_cm2 * factorB * factorB * factorB * factorB
        assert crossSection_cm2 >= 0.0

        return crossSection_cm2

    def _computeCrossSectionPWBA(self, energy_eV, atomicNumber, subshell):
        ionizationEnergy_eV = self.data[atomicNumber][subshell][KEY_Eca_eV]
        overvoltage = energy_eV / ionizationEnergy_eV
        if overvoltage < 16.0:
            return 0.0

        a0_m = physical_constants["Bohr radius"][0]
        a0_cm = NumericConversion.m_To_cm(a0_m)

        Anlj = self.data[atomicNumber][subshell][KEY_A_SUBSHELL]

        beta = self._computeBeta(energy_eV)

        xi = self._computeXi(energy_eV)

        g1 = self.data[atomicNumber][subshell][KEY_g1]
        g2 = self.data[atomicNumber][subshell][KEY_g2]
        g3 = self.data[atomicNumber][subshell][KEY_g3]
        g4 = self.data[atomicNumber][subshell][KEY_g4]

        factorA_cm2 = 4.0 * np.pi * a0_cm * a0_cm * Anlj / (beta * beta)

        term1 = (np.log(xi * xi) - beta * beta) * (1.0 + g1 / xi)
        term2 = g2
        term3 = g3 * np.power(1.0 - beta * beta, 1.0/4.0)
        term4 = g4 / xi
        factorB = term1 + term2 + term3 + term4

        crossSection_cm2 = factorA_cm2 * factorB
        assert crossSection_cm2 >= 0.0

        return crossSection_cm2

    def _computeBeta(self, energy_eV):
        restMass_MeV = physical_constants["electron mass energy equivalent in MeV"][0]
        restMass_eV = NumericConversion.MeV_To_eV(restMass_MeV)

        E_eV = energy_eV
        mc2_eV = restMass_eV
        nominator = np.sqrt(E_eV * (E_eV + 2.0 * mc2_eV))
        denominator = E_eV + mc2_eV

        beta = nominator/denominator
        assert beta >= 0.0
        assert beta <= 1.0

        return beta

    def _computeXi(self, energy_eV):
        restMass_MeV = physical_constants["electron mass energy equivalent in MeV"][0]
        restMass_eV = NumericConversion.MeV_To_eV(restMass_MeV)

        E_eV = energy_eV
        mc2_eV = restMass_eV
        nominator = np.sqrt(E_eV * (E_eV + 2.0 * mc2_eV))
        denominator = mc2_eV

        xi = nominator/denominator
        assert xi >= 0.0

        return xi

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data):
        self._data = data

def runCreateDataFile():
    dataFilepath = Files.getCurrentModulePath(__file__, "../data/bote2009_tables.csv")

    model = Bote2009()
    model.createTabulatedDataFile(dataFilepath)

def getModel():
    dataFilepath = Files.getCurrentModulePath(__file__, "../data/bote2009_Parameters.csv")

    model = Bote2009()
    model.readTabulatedDataFile(dataFilepath)

    return model

def runGraphicsBote2009():
    model = getModel()

    energies_eV = np.logspace(3.0, 9.0, 1000)
    subshells = [SUBSHELL_K, SUBSHELL_L1, SUBSHELL_L2, SUBSHELL_L3, SUBSHELL_M1, SUBSHELL_M2, SUBSHELL_M3, SUBSHELL_M4, SUBSHELL_M5]
    atomicNumber = 79
    particle = PARTICLE_ELECTRON

    plt.figure()
    for subshell in subshells:
        crossSections_cm2 = [model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle) for energy_eV in energies_eV]

        plt.loglog(energies_eV, crossSections_cm2, label=subshell)

    plt.xlabel(r"E (eV)")
    plt.ylabel(r"$\sigma_{-}$ (cm$^{2}$)")
    plt.ylim((1.0e-24, 1.0e-19))

    plt.figure()
    for subshell in subshells:
        crossSections_cm2 = [model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle) for energy_eV in energies_eV]
        crossSections_barn = [NumericConversion.cm2_To_barn(crossSection_cm2) for crossSection_cm2 in crossSections_cm2]
        plt.loglog(energies_eV, crossSections_barn, label=subshell)

    plt.xlabel(r"E (eV)")
    plt.ylabel(r"$\sigma_{-}$ (barn)")
    plt.ylim((1.0, 1.0e5))

    plt.show()

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=runGraphicsBote2009)
