import sys
from PyQt5 import QtWidgets
class Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 100, 600, 600)
        self.ui()
    def ui(self):
        self.sayac = 0
        self.lbyazi =  QtWidgets.QLabel("0 Kez tıkandı")
        self.btnEkle  = QtWidgets.QPushButton("Sayı Arttır")
        self.btnSifir = QtWidgets.QPushButton("Sıfırla")

        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.addWidget(self.lbyazi)
        self.vBox.addWidget(self.btnEkle)
        self.vBox.addWidget(self.btnSifir)
        self.vBox.addStretch()

        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.addStretch()
        self.hBox.addLayout(self.vBox)
        self.hBox.addStretch()

        self.setLayout(self.hBox)
        self.show()
        self.btnEkle.clicked.connect(self.sayacEkle)
        self.btnSifir.clicked.connect(self.sayacSifir)

    def sayacEkle(self):
        self.sayac += 1
        self.lbyazi.setText("Tıkama Sayısı :" + str(self.sayac))
    def sayacSifir(self):
        self.sayac  = 0
        self.lbyazi.setText("Tıkama Sayısı :" + str(self.sayac))
        

app = QtWidgets.QApplication(sys.argv)
frm = Form()
sys.exit(app.exec_())



        
        
