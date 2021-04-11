from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from administrador.particula import Particula
from administrador.particulas import Particulas


class Mainwindow(QMainWindow) :
    def __init__(self) :
        super(Mainwindow, self).__init__()
        self.particulas = Particulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)


    
    @Slot()
    def click_mostrar(self) :
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))

    @Slot()
    def click_agregar_final(self) :
        i_d = self.ui.id_lineEdit.text()
        origen_x  = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula1 = Particula(i_d, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_final(particula1)

    @Slot()
    def click_agregar_inicio(self) :
        print("Agregado Correctamente :)")
        i_d = self.ui.id_lineEdit.text()
        origen_x  = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula1 = Particula(i_d, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula1)
