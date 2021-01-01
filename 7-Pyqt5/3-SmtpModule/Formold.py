import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
def Form(self):
    
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    form.setWindowTitle('E-Mail Form')
    form.setGeometry(300, 100, 600, 600)

    self.lbKimden = QtWidgets.QLabel(form)
    self.lbKimden.setText('Kimden :')
    self.lbKimden.move(5,20)
    self.txtBoxKimden= QtWidgets.QLineEdit(form)
    self.txtBoxKimden.move(50,20)

    lbKime = QtWidgets.QLabel(form)
    lbKime.setText('Kime :')
    lbKime.move(5,42)
    txtBoxKime= QtWidgets.QLineEdit(form)
    txtBoxKime.move(50,42)
    
    lbSubject = QtWidgets.QLabel(form)
    lbSubject.setText('Konu :')
    lbSubject.move(5,64)
    txtBoxSubject= QtWidgets.QLineEdit(form)
    txtBoxSubject.move(50,64)

    lbIcerik = QtWidgets.QLabel(form)
    lbIcerik.setText('İçerik :')
    lbIcerik.move(5,86)
    txtBoxSubject= QtWidgets.QLineEdit(form)
    txtBoxSubject.resize(300,200)
    txtBoxSubject.move(50,86)

    lbUser = QtWidgets.QLabel(form)
    lbUser.setText('User :')
    lbUser.move(5,290)
    txtBoxUser= QtWidgets.QLineEdit(form)
    txtBoxUser.move(50,290)

    lbPassword= QtWidgets.QLabel(form)
    lbPassword.setText('Şifre :')
    lbPassword.move(5,312)
    txtBoxPassword= QtWidgets.QLineEdit(form)
    txtBoxPassword.move(50,312)

    btn = QtWidgets.QPushButton(form)
    btn.setText('Gönder')
    btn.move(5,340)
    btn.clicked.connect(gonder)


    form.show()
    sys.exit(app.exec_())
def gonder(self):
    mesaj = MIMEMultipart() 
    mesaj["From"] = self.tx