from interfazGrafica import *

class Main(QObject):

    def __init__(self):

        # Se muestra en pantalla el menu de bienvenida
        self.mainWindow = MainWindow()
        self.mainWindow.show()

        # Se añaden los informes al ComboBox
        self.informes = [
            'Conciliacion Contable SYPCON, BANCWARE & MAT',
            'Sensibilidad GAP de Interes BANCWARE & MAT',
            'Reporte R13 BANCWARE & MAT'
        ]
        self.mainWindow.informe.addItems(self.informes)

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    _main = Main()
    sys.exit(app.exec_())