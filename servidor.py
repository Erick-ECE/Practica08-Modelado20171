import sys
from PyQt4 import QtCore, QtGui, uic


servidor = uic.loadUiType("servidor.ui")

class Ventana_Servidor(QMainWindow, servidor):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.arreglarTabla()
        self.show()

    def arreglarTabla(self):
    	self.Tabla.horizontalHeader().setStretchLastSection(True)
    	self.Tabla.verticalHeader().setStretchLastSection(True)
    	self.Tabla.horizontalHeader().setResizeMode(QHeaderView.Stretch)
    	self.Tabla.verticalHeader().setResizeMode(QHeaderView.Stretch)

def main():
    app = QtGui.QApplication(sys.argv)
    ventana = Ventana_Servidor()
    sys.exit(app.exec_())

main()
