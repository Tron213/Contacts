from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtSql import *
import sqlite3

#------------sql

db=sqlite3.connect('contactss.db')
sql=db.cursor()
def add(self):
    num=self.lineEdit.text()
    name=self.lineEdit_2.text()
    job=self.lineEdit_3.text()
    sql.execute(f"INSERT INTO contacts VALUES ('{num}','{name}',{job})")
    db.commit
#--------------pyqt


Form, Window = uic.loadUiType('cont.ui')

db_name = 'C:\Contact\contactss.db'


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

cont=QSqlTableModel()
cont.setTable('contacts')
cont.select()

app = QApplication([])
window = Window()
form=Form()
form.setupUi(window)
form.pushButton.clicked.connect(add)
form.tableView.setModel(cont)

window.show()
app.exec()