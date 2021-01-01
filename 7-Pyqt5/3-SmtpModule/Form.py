import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QMessageBox

class Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 100, 600, 600)
        self.ui()
    def ui(self):
        self.sayac = 0
        self.lbkimden =  QtWidgets.QLabel("Kimden :")
        self.lbkime =  QtWidgets.QLabel("Kime :")
        self.lbkonu =  QtWidgets.QLabel("Konu :")
        self.lbicerik =  QtWidgets.QLabel("İçerik :")
        self.lbkullanici =  QtWidgets.QLabel("Kullanıcı :")
        self.lbsifre= QtWidgets.QLineEdit("Şifre :") 

        self.txtboxkimden = QtWidgets.QLineEdit()
        self.txtboxkime = QtWidgets.QLineEdit()
        self.txtboxkonu = QtWidgets.QLineEdit()
        self.txtboxicerik = QtWidgets.QLineEdit()
        self.txtbox = QtWidgets.QLineEdit()
        self.txtboxicerik = QtWidgets.QLineEdit()
        self.txtboxkullanici = QtWidgets.QLineEdit()
        self.txtboxsifre = QtWidgets.QLineEdit()
        self.txtboxsifre.setEchoMode(self.txtboxsifre.Password)
        self.btngonder  = QtWidgets.QPushButton("Gönder")

        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.addWidget(self.lbkimden)
        self.vBox.addWidget(self.txtboxkimden)
        self.vBox.addWidget(self.lbkime)
        self.vBox.addWidget(self.txtboxkime)
        self.vBox.addWidget(self.lbkonu)
        self.vBox.addWidget(self.txtboxkonu)
        self.vBox.addWidget(self.lbicerik)
        self.vBox.addWidget(self.txtboxicerik)
        self.vBox.addWidget(self.lbkullanici)
        self.vBox.addWidget(self.txtboxkullanici)
        self.vBox.addWidget(self.lbsifre)
        self.vBox.addWidget(self.txtboxsifre)
        self.vBox.addWidget(self.btngonder)
        self.vBox.addStretch()

        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.addStretch()
        self.hBox.addLayout(self.vBox)
        self.hBox.addStretch()
        

        self.setLayout(self.hBox)
        self.show()
        self.btngonder.clicked.connect(self.gonder)
        # self.btnSifir.clicked.connect(self.sayacSifir)

    def gonder(self):
        mesaj = MIMEMultipart() 
        mesaj["From"] =  self.txtboxkimden.text()
        mesaj["To"]  =  self.txtboxkime.text()
        mesaj["Subject"] = self.txtboxkonu.text()
        yazi = self.txtboxicerik.text()
        kulanici = self.txtboxkullanici.text()
        sifre = self.txtboxsifre.text()
        mesaj_govdesi =  MIMEText(yazi,"plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail =  smtplib.SMTP("smtp.gmail.com",587) # bağlantı
            mail.ehlo() # stmp tanıtım
            mail.starttls() # kullanıcı adı ve şifre
            mail.login(kulanici,sifre)
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())  # mail gönderme
            QMessageBox.about(self, "Mesaj ", "Mail Başarı ile gönderildi ...")
            mail.close()
        except:
            QMessageBox.about(self, "Mesaj ", "Mail  gönderilemedi ...")

    #     self.sayac += 1
    #     self.lbyazi.setText("Tıkama Sayısı :" + str(self.sayac))
    # def sayacSifir(self):
    #     self.sayac  = 0
    #     self.lbyazi.setText("Tıkama Sayısı :" + str(self.sayac))
        

app = QtWidgets.QApplication(sys.argv)
frm = Form()
sys.exit(app.exec_())



        
        
