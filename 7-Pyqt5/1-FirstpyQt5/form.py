import sys
from PyQt5 import QtWidgets
def Form():
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    form.setWindowTitle('İlk Form')
    form.setGeometry(300, 100, 600, 600)
    label = QtWidgets.QLabel(form)
    label.setText("Adı Giriniz")
    label.move(5,20)

    txtBoxad = QtWidgets.QLineEdit(form)
    txtBoxad.move(55,20)

    btn = QtWidgets.QPushButton(form)
    btn.setText("Gönder")
    btn.move(5,60)

    form.show()
    sys.exit(app.exec_())
Form()
