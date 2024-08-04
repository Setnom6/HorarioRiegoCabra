import sys

from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QComboBox
from codigo.BuscadorHorario import BuscadorHorario


class AppHorario(QDialog):

    def __init__(self, parent=None):
        super(AppHorario, self).__init__(parent)
        self.setWindowTitle('Horario de riego')

        self.propietarioLabel = QLabel("Seleccione propietario: ")
        self.propietarioSelector = QComboBox()
        self.mesLabel = QLabel("Seleccione un mes: ")
        self.mesSelector = QComboBox()
        self.diaLabel = QLabel("Seleccione un día: ")
        self.diaEdit = QLineEdit()
        self.botonDeCarga = QPushButton("Obtener")
        self.resultadoLabel = QLabel("")

        self.verticalLayout = QVBoxLayout()

        self.propietarioLayout = QHBoxLayout()
        self.propietarioLayout.addWidget(self.propietarioLabel)
        self.propietarioLayout.addWidget(self.propietarioSelector)
        self.verticalLayout.addLayout(self.propietarioLayout)

        self.mesLayout = QHBoxLayout()
        self.mesLayout.addWidget(self.mesLabel)
        self.mesLayout.addWidget(self.mesSelector)
        self.verticalLayout.addLayout(self.mesLayout)

        self.diaLayout = QHBoxLayout()
        self.diaLayout.addWidget(self.diaLabel)
        self.diaLayout.addWidget(self.diaEdit)
        self.verticalLayout.addLayout(self.diaLayout)

        self.botonLayout = QHBoxLayout()
        self.botonLayout.addWidget(self.botonDeCarga)
        self.verticalLayout.addLayout(self.botonLayout)

        self.outputLayout = QHBoxLayout()
        self.outputLayout.addWidget(self.resultadoLabel)
        self.verticalLayout.addLayout(self.outputLayout)

        self.setSelectores()
        self.botonDeCarga.clicked.connect(self.calcularHorario)

        self.setLayout(self.verticalLayout)

    def calcularHorario(self) -> None:
        propietario = self.propietarioSelector.currentIndex()
        mes = self.mesSelector.currentIndex()
        dia = int(self.diaEdit.text())

        self.resultadoLabel.setText(BuscadorHorario.calcularTurno(propietario, dia, mes))

    def setSelectores(self) -> None:
        self.propietarioSelector.addItems(BuscadorHorario.PERSONAS)
        self.mesSelector.addItems(BuscadorHorario.MESES)


if __name__ == '__main__':
    # Create QApplication
    app = QApplication(sys.argv)

    # Create the showw of the form
    form = AppHorario()
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec())
