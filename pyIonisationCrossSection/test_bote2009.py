#!/usr/bin/env python
"""
.. py:currentmodule:: test_bote2009
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the implementation of Bote Salvat ionization cross section.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest
import logging
import os.path

# Third party modules.

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules
import pyIonisationCrossSection.bote2009 as bote2009

# Globals and constants variables.

class Test_bote2009(unittest.TestCase):
    """
    TestCase class for the module `bote2009`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        dataFilepath = Files.getCurrentModulePath(__file__, "../data/bote2009_tables.csv")
        self.assertTrue(os.path.isfile(dataFilepath))

        self.model = bote2009.Bote2009()
        self.model.readOriginalDataFile(dataFilepath)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_readOriginalDataFile(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        dataFilepath = Files.getCurrentModulePath(__file__, "../data/bote2009_tables.csv")
        self.assertTrue(os.path.isfile(dataFilepath))

        model = bote2009.Bote2009()
        model.readOriginalDataFile(dataFilepath)

        self.assertEquals(99, len(model.data))
        self.assertEquals(1, len(model.data[1]))
        self.assertEquals(9, len(model.data[99]))

        self.assertAlmostEquals(-4.301e-2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_a5])
        self.assertAlmostEquals(-1.070e-1, model.data[37][bote2009.SUBSHELL_M1][bote2009.KEY_a5])
        self.assertAlmostEquals(2.783e2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_Eca_eV])
        self.assertAlmostEquals(3.133e2, model.data[37][bote2009.SUBSHELL_M1][bote2009.KEY_Eca_eV])

        self.assertAlmostEquals(3.009, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_d5])
        self.assertAlmostEquals(2.086, model.data[37][bote2009.SUBSHELL_M1][bote2009.KEY_d5])
        self.assertAlmostEquals(2.783e2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_Ecd_eV])
        self.assertAlmostEquals(3.133e2, model.data[37][bote2009.SUBSHELL_M1][bote2009.KEY_Ecd_eV])

        self.assertAlmostEquals(1.540, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_B_ELECTRON])
        self.assertAlmostEquals(8.381e-1, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_B_POSITRON])
        self.assertAlmostEquals(1.120e-6, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_A_SUBSHELL])
        self.assertAlmostEquals(3.059e-2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_g1])
        self.assertAlmostEquals(7.582e-2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_g4])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_readTabulatedDataFile(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        dataFilepath = Files.getCurrentModulePath(__file__, "../data/bote2009_Parameters.csv")
        self.assertTrue(os.path.isfile(dataFilepath))

        model = bote2009.Bote2009()
        model.readTabulatedDataFile(dataFilepath)

        self.assertEquals(99, len(model.data))
        self.assertEquals(1, len(model.data[1]))
        self.assertEquals(9, len(model.data[99]))

        self.assertAlmostEquals(-4.301e-2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_a5])
        self.assertAlmostEquals(-1.070e-1, model.data[37][bote2009.SUBSHELL_M1][bote2009.KEY_a5])
        self.assertAlmostEquals(2.783e2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_Eca_eV])
        self.assertAlmostEquals(3.133e2, model.data[37][bote2009.SUBSHELL_M1][bote2009.KEY_Eca_eV])

        self.assertAlmostEquals(3.009, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_d5])
        self.assertAlmostEquals(2.086, model.data[37][bote2009.SUBSHELL_M1][bote2009.KEY_d5])
        self.assertAlmostEquals(2.783e2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_Ecd_eV])
        self.assertAlmostEquals(3.133e2, model.data[37][bote2009.SUBSHELL_M1][bote2009.KEY_Ecd_eV])

        self.assertAlmostEquals(1.540, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_B_ELECTRON])
        self.assertAlmostEquals(8.381e-1, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_B_POSITRON])
        self.assertAlmostEquals(1.120e-6, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_A_SUBSHELL])
        self.assertAlmostEquals(3.059e-2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_g1])
        self.assertAlmostEquals(7.582e-2, model.data[36][bote2009.SUBSHELL_M1][bote2009.KEY_g4])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_ionizationEnergies(self):
        """
        Tests for method `ionizationEnergies`.
        """

        for atomicNumber in self.model.data:
            for subshell in self.model.data[atomicNumber]:
                element = self.model.data[atomicNumber][subshell]
                self.assertAlmostEquals(element[bote2009.KEY_Eca_eV], element[bote2009.KEY_Ecd_eV])

        #self.fail("Test if the testcase is working.")

    def test__computeCrossSectionDWBAElectron(self):
        """
        Tests for method `_computeCrossSectionDWBAElectron`.
        """

        atomicNumber = 79
        subshell = bote2009.SUBSHELL_K
        overvoltage = 0.1
        crossSection_cm2 = self.model._computeCrossSectionDWBAElectron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.0
        crossSection_cm2 = self.model._computeCrossSectionDWBAElectron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.1
        crossSection_cm2 = self.model._computeCrossSectionDWBAElectron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.11724133713184771, crossSection_cm2*1.0e23)

        overvoltage = 12.35
        crossSection_cm2 = self.model._computeCrossSectionDWBAElectron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(1.0228468908595612, crossSection_cm2*1.0e23)

        overvoltage = 16.0
        crossSection_cm2 = self.model._computeCrossSectionDWBAElectron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(1.0973762571623711, crossSection_cm2*1.0e23)

        overvoltage = 16.1
        crossSection_cm2 = self.model._computeCrossSectionDWBAElectron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(1.099446345773381, crossSection_cm2*1.0e23)

        #self.fail("Test if the testcase is working.")

    def test__computeCrossSectionDWBAPositron(self):
        """
        Tests for method `_computeCrossSectionDWBAPositron`.
        """

        atomicNumber = 79
        subshell = bote2009.SUBSHELL_K
        overvoltage = 0.1
        crossSection_cm2 = self.model._computeCrossSectionDWBAPositron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.0
        crossSection_cm2 = self.model._computeCrossSectionDWBAPositron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.1
        crossSection_cm2 = self.model._computeCrossSectionDWBAPositron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.0090553258325375644, crossSection_cm2*1.0e23)

        overvoltage = 12.35
        crossSection_cm2 = self.model._computeCrossSectionDWBAPositron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.88130255940750024, crossSection_cm2*1.0e23)

        overvoltage = 16.0
        crossSection_cm2 = self.model._computeCrossSectionDWBAPositron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.98124977226526255, crossSection_cm2*1.0e23)

        overvoltage = 16.1
        crossSection_cm2 = self.model._computeCrossSectionDWBAPositron(overvoltage, atomicNumber, subshell)
        self.assertAlmostEquals(0.98396561046025066, crossSection_cm2*1.0e23)

        #self.fail("Test if the testcase is working.")

    def test__computeCrossSectionPWBA(self):
        """
        Tests for method `_computeCrossSectionPWBA`.
        """

        atomicNumber = 79
        subshell = bote2009.SUBSHELL_K
        ionizationEnergy_eV = 8.096e4
        overvoltage = 0.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model._computeCrossSectionPWBA(energy_eV, atomicNumber, subshell)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model._computeCrossSectionPWBA(energy_eV, atomicNumber, subshell)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 15.9999
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model._computeCrossSectionPWBA(energy_eV, atomicNumber, subshell)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 16.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model._computeCrossSectionPWBA(energy_eV, atomicNumber, subshell)
        self.assertAlmostEquals(1.0509364979843927, crossSection_cm2*1.0e23)

        overvoltage = 16.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model._computeCrossSectionPWBA(energy_eV, atomicNumber, subshell)
        self.assertAlmostEquals(1.0528518172445325, crossSection_cm2*1.0e23)

        overvoltage = 40.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model._computeCrossSectionPWBA(energy_eV, atomicNumber, subshell)
        self.assertAlmostEquals(1.3620052506575531, crossSection_cm2*1.0e23)

        overvoltage = 1000.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model._computeCrossSectionPWBA(energy_eV, atomicNumber, subshell)
        self.assertAlmostEquals(2.6375992446712284, crossSection_cm2*1.0e23)

        #self.fail("Test if the testcase is working.")

    def test__computeBeta(self):
        """
        Tests for method `_computeBeta`.
        """

        energy_eV = 10.0
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(0.0062560272129148341, beta)

        energy_eV = 0.1e6
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(0.54822087094248217, beta)

        energy_eV = 0.5e6
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(0.8628619684078338, beta)

        energy_eV = 1.0e6
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(0.94107923149011297, beta)

        c_m_s = 2.998e8
        energy_eV = 100.0e3
        betaRef = 1.644e8/c_m_s
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(betaRef, beta, places=3)

        energy_eV = 120.0e3
        betaRef = 1.759e8/c_m_s
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(betaRef, beta, places=3)

        energy_eV = 200.0e3
        betaRef = 2.086e8/c_m_s
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(betaRef, beta, places=3)

        energy_eV = 300.0e3
        betaRef = 2.330e8/c_m_s
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(betaRef, beta, places=2)

        energy_eV = 400.0e3
        betaRef = 2.484e8/c_m_s
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(betaRef, beta, places=2)

        energy_eV = 1000.0e3
        betaRef = 2.823e8/c_m_s
        beta = self.model._computeBeta(energy_eV)
        self.assertAlmostEquals(betaRef, beta, places=2)

        #self.fail("Test if the testcase is working.")

    def test__computeXi(self):
        """
        Tests for method `_computeXi`.
        """

        energy_eV = 10.0
        beta = self.model._computeXi(energy_eV)
        self.assertAlmostEquals(0.0062561496403186921, beta)

        energy_eV = 0.1e6
        beta = self.model._computeXi(energy_eV)
        self.assertAlmostEquals(0.65550502378565267, beta)

        energy_eV = 0.5e6
        beta = self.model._computeXi(energy_eV)
        self.assertAlmostEquals(1.707151379918922, beta)

        energy_eV = 1.0e6
        beta = self.model._computeXi(energy_eV)
        self.assertAlmostEquals(2.7827254266659138, beta)

        #self.fail("Test if the testcase is working.")

    def test_crossSection_cm2(self):
        """
        Tests for method `crossSection_cm2`.
        """

        particle = bote2009.PARTICLE_ELECTRON
        atomicNumber = 79
        subshell = bote2009.SUBSHELL_K
        ionizationEnergy_eV = 8.096e4
        overvoltage = 0.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.11724133713184771, crossSection_cm2*1.0e23)

        overvoltage = 12.35
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(1.0228468908595612, crossSection_cm2*1.0e23)

        overvoltage = 16.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(1.0973762571623711, crossSection_cm2*1.0e23)

        overvoltage = 0.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 15.9999
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(1.0973741879568479, crossSection_cm2*1.0e23)

        overvoltage = 16.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(1.0973762571623711, crossSection_cm2*1.0e23)

        overvoltage = 16.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(1.0990031222736776, crossSection_cm2*1.0e23)

        overvoltage = 16.5
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(1.1057356376000727, crossSection_cm2*1.0e23)

        overvoltage = 40.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(1.385422351961584, crossSection_cm2*1.0e23)

        overvoltage = 1000.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(2.6393837320124414, crossSection_cm2*1.0e23)

        particle = bote2009.PARTICLE_POSITRON
        atomicNumber = 79
        subshell = bote2009.SUBSHELL_K
        ionizationEnergy_eV = 8.096e4
        overvoltage = 0.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.0, crossSection_cm2*1.0e23)

        overvoltage = 1.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.0090553258325375644, crossSection_cm2*1.0e23)

        overvoltage = 12.35
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.88130255940750024, crossSection_cm2*1.0e23)

        overvoltage = 16.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.98124977226526255, crossSection_cm2*1.0e23)

        overvoltage = 16.1
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.98294660815523183, crossSection_cm2*1.0e23)

        overvoltage = 16.5
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(0.99161519726946945, crossSection_cm2*1.0e23)

        overvoltage = 40.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(1.3241028077847157, crossSection_cm2*1.0e23)

        overvoltage = 1000.0
        energy_eV = overvoltage * ionizationEnergy_eV
        crossSection_cm2 = self.model.crossSection_cm2(energy_eV, atomicNumber, subshell, particle)
        self.assertAlmostEquals(2.6345826475397951, crossSection_cm2*1.0e23)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, False)
