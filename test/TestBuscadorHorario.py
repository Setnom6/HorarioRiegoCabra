import unittest
import numpy as np

from typing import List

from codigo.BuscadorHorario import BuscadorHorario


class TestBuscadorHorario(unittest.TestCase):
    INPUTS_DE_PRUEBA: List[List[int]]  # Propietario, Dia, Mes
    OUTPUTS_DE_PRUEBA: List[List[int]]  # Dia, Mes, HoraInicio, MinInicio, HoraFin, MinFin

    @classmethod
    def setUpClass(cls):
        cls.INPUTS_DE_PRUEBA = [[5, 5, 4], [6, 3, 0], [11, 31, 8], [5, 24, 2], [7, 15, 4], [13, 26, 5], [14, 31, 1]]
        cls.OUTPUTS_DE_PRUEBA = [[5, 4, 9, 19, 11, 19], [3, 0, 13, 47, 15, 47], [31, 8, 19, 4, 20, 58],
                                 [24, 2, 19, 20, 21, 20], [15, 4, 4, 30, 7, 8], [26, 5, 3, 39, 8, 1],
                                 [31, 1, 3, 38, 7, 53]]

        super().setUpClass()

    def testSiDevuelveBienHorario(self) -> None:
        for index, element in enumerate(TestBuscadorHorario.INPUTS_DE_PRUEBA):
            mensajeDeSalida = BuscadorHorario.calcularTurno(element[0], element[1], element[2])
            mensajeEsperado = "Para el {} de {} le corresponde de {}:{:02d} a {}:{:02d}".format(
                TestBuscadorHorario.OUTPUTS_DE_PRUEBA[index][0],
                BuscadorHorario.MESES[TestBuscadorHorario.OUTPUTS_DE_PRUEBA[index][1]],
                TestBuscadorHorario.OUTPUTS_DE_PRUEBA[index][2],
                TestBuscadorHorario.OUTPUTS_DE_PRUEBA[index][3],
                TestBuscadorHorario.OUTPUTS_DE_PRUEBA[index][4],
                TestBuscadorHorario.OUTPUTS_DE_PRUEBA[index][5])

            self.assertEqual(mensajeEsperado, mensajeDeSalida)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

        del TestBuscadorHorario.OUTPUTS_DE_PRUEBA
        del TestBuscadorHorario.INPUTS_DE_PRUEBA


if __name__ == '__main__':
    unittest.main()
