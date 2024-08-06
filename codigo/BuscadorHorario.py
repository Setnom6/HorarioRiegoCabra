from typing import List, Tuple

import numpy as np

import os
import sys


class BuscadorHorario:
    if hasattr(sys, '_MEIPASS'):
            rutaDirectorio = os.path.join(sys._MEIPASS, "datos")
    else:
            rutaDirectorio = os.path.dirname(os.path.abspath(__file__))
    diasRuta = os.path.join(rutaDirectorio, "datos/diasYTurnos.txt")
    horariosRuta = os.path.join(rutaDirectorio, "datos/horasYTurnos.txt")

    MATRIZ_DE_DIAS: np.ndarray = np.loadtxt(diasRuta)
    MATRIZ_DE_HORARIOS: np.ndarray = np.loadtxt(horariosRuta)
    PERSONAS: List[str] = ["1", "2", "3", "4", "5", "Soledad", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    MESES: List[str] = ["Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    propietario: int
    dia: int
    mes = int

    @staticmethod
    def calcularTurno(propietario: int, dia: int, mes: int) -> str:
        buscador = BuscadorHorario(propietario, dia, mes)
        inicio, final = buscador.obtenerHorario()
        if inicio == -1:
            return "Para el {} de {} no le corresponde ningún horario".format(dia,
                                                                              BuscadorHorario.MESES[mes])
        else:
            inicio = buscador.convertirMinutosAHorasYMinutos(inicio)
            final = buscador.convertirMinutosAHorasYMinutos(final)
            return "Para el {} de {} le corresponde de {}:{:02d} a {}:{:02d}".format(dia,
                                                                                     BuscadorHorario.MESES[mes],
                                                                                     inicio[0],
                                                                                     inicio[1],
                                                                                     final[0],
                                                                                     final[1])

    def __init__(self, propietario: int, dia: int, mes: int) -> None:
        self.propietario = propietario
        if 31 == dia:
            self.dia = 1
        else:
            self.dia = dia
        self.mes = mes

    def cargarMatriz(self, tipo: str) -> np.ndarray:
        if "dias" == tipo:
            return np.loadtxt("codigo/datos/diasYTurnos.txt")
        elif "horarios" == tipo:
            return np.loadtxt("codigo/datos/horasYTurnos.txt")

    def convertirMinutosAHorasYMinutos(self, minutos: int) -> Tuple[int, int]:
        return minutos // 60, minutos % 60

    def obtenerHorario(self) -> Tuple[int, int]:
        try:
            turno = int(np.where(self.dia == BuscadorHorario.MATRIZ_DE_DIAS[:, self.mes])[0][0])
            inicio = int(BuscadorHorario.MATRIZ_DE_HORARIOS[self.propietario][turno])
            if inicio == -1:
                return -1, -1
            if self.propietario == (BuscadorHorario.MATRIZ_DE_HORARIOS.shape[0] - 1):
                final = int(BuscadorHorario.MATRIZ_DE_HORARIOS[0][turno])
                if final == -1:
                    final = int(BuscadorHorario.MATRIZ_DE_HORARIOS[1][turno])
            else:
                final = int(BuscadorHorario.MATRIZ_DE_HORARIOS[self.propietario + 1][turno])
                if final == -1:
                    try:
                        final = int(BuscadorHorario.MATRIZ_DE_HORARIOS[self.propietario + 2][turno])

                    except:
                        final = int(BuscadorHorario.MATRIZ_DE_HORARIOS[0][turno])
            return inicio, final
        except:
            return -1, -1
