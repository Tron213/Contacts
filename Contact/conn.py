import sqlite3
import interf
from PyQt5 import QtWidgets, QtSql
import sys
from PyQt5.QtSql import *

db = sqlite3.connect('contactss.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usera(
    num TEXT,
    name TEXT,
    job TEXT
)''')
db.commit()

class Registration(QtWidgets.QMainWindow, interf.Ui_MainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.label.setText('')
        self.lineEdit.setPlaceholderText('Введите номер')
        self.lineEdit_2.setPlaceholderText('Введите имя')
        self.lineEdit_3.setPlaceholderText('Еще')
        self.lineEdit_4.setPlaceholderText('Поиск')
        self.setWindowTitle('Contact')
        

        self.pushButton.pressed.connect(self.reg)
    def reg(self):
        num = self.lineEdit.text()
        name = self.lineEdit_2.text()
        job = self.lineEdit_3.text()

        cursor.execute(f'SELECT num FROM usera WHERE num="{num}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO usera VALUES ("{num}", "{name}", "{job}")')
            self.label.setText(f'Номер записан')
            db.commit()
        else:
            self.label.setText('Номер уже записан')
db_name = 'C:/Users/f4nan/OneDrive/Документы/GitHub/Contacts/Contact/contactss.db'

def connect(db_name):
    db=QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(db_name)
    if not db.open():
        print('не удалось подключиться к базе ')
        return False 
    return db

if not connect(db_name):
    sys.exit(-1)
else:
    print('Подключено')


userd = QSqlTableModel()
userd.setTable('usera')
userd.select()

App = QtWidgets.QApplication([])
window = Registration()
window.tableView.setModel(userd)
window.show()
App.exec()
