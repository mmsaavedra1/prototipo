import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit,
                             QApplication, QComboBox, QDateEdit, QCheckBox,
                             QMessageBox, QListWidget)

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal, QObject, QDate

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
        self.setGeometry(500, 300, 640, 400)
        self.setFixedSize(640, 400)

        # Mensaje de bienvenida
        self.titulo = QLabel(self)
        self.titulo.setGeometry(40, 10, 440, 60)
        self.titulo.setText("Generacion de Conciliadores")
        self.titulo.setFont(QFont('Arial', 32, weight=QFont.Bold))

        self.subtitulo = QLabel(self)
        self.subtitulo.setGeometry(40, 40, 440, 60)
        self.subtitulo.setText("SYPCON, BANCWARE & MAT")
        self.subtitulo.setFont(QFont('Arial', 26))

        self.pie_pagina = QLabel(self)
        self.pie_pagina.setGeometry(45, 370, 170, 20)
        self.pie_pagina.setText("Riesgo Estructural - 2024")
        self.pie_pagina.setFont(QFont('Arial', 13))
        

        # Imagen de NEWEN
        self.imagenNewen = QLabel(self)
        self.imagenNewen.setGeometry(480, 0, 150, 150)
        self.imagenNewen.setPixmap(QPixmap("Images/NEWEN.png").scaled(150, 150))

        # Etiqueta de fecha
        self.etiqueta_fecha = QLabel(self)
        self.etiqueta_fecha.setGeometry(40, 110, 190, 15)
        self.etiqueta_fecha.setText("Fecha del informe (yy-mm-dd)")

        self.fecha = QDateEdit(self)
        self.fecha.setGeometry(245, 110, 100, 20)
        self.fecha.setDate(QDate.fromString("2024-01-01", "yyyy-MM-dd"))
        self.fecha.setDisplayFormat("yyyy-MM-dd")

        # Etiqueta de informe a generar
        self.etiqueta_informe = QLabel(self)
        self.etiqueta_informe.setGeometry(40, 140, 190, 15)
        self.etiqueta_informe.setText("Selecciona el reporte a generar")

        self.informe = QComboBox(self)
        self.informe.setGeometry(240, 135, 230, 25)

        # Lista de querys
        self.listado = QListWidget(self)
        self.listado.setGeometry(40, 170, 430, 180)

        # Boton para generar Query
        self.boton_generar = QPushButton(self)
        self.boton_generar.setGeometry(480, 190, 150, 40)
        self.boton_generar.setText("Generar Query")

        # Boton para copiar Query
        self.boton_copiar = QPushButton(self)
        self.boton_copiar.setGeometry(480, 240, 150, 40)
        self.boton_copiar.setText("Copiar")

        # Boton para limpiar query
        self.boton_limpiar = QPushButton(self)
        self.boton_limpiar.setGeometry(480, 290, 150, 40)
        self.boton_limpiar.setText("Limpiar")
