import sys
import sqlite3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox


class UI_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 358)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 0, 160, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.type = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.type.setMaximumSize(QtCore.QSize(200, 30))
        self.type.setObjectName("type")
        self.verticalLayout.addWidget(self.type)
        self.roasting = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.roasting.setMaximumSize(QtCore.QSize(200, 30))
        self.roasting.setObjectName("roasting")
        self.verticalLayout.addWidget(self.roasting)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.taste = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.taste.setMaximumSize(QtCore.QSize(200, 30))
        self.taste.setObjectName("taste")
        self.verticalLayout.addWidget(self.taste)
        self.price = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.price.setMaximumSize(QtCore.QSize(200, 30))
        self.price.setObjectName("price")
        self.verticalLayout.addWidget(self.price)
        self.volume = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.volume.setMaximumSize(QtCore.QSize(200, 30))
        self.volume.setObjectName("volume")
        self.verticalLayout.addWidget(self.volume)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 160, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 111, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 349, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Молотый"))
        self.comboBox.setItemText(1, _translate("MainWindow", "В зёрнах"))
        self.label.setText(_translate("MainWindow", "Сорт"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "Молотый / в зёрнах"))
        self.label_4.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Объём/гр"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))


class UI_Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 466, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addButton.setMinimumSize(QtCore.QSize(150, 25))
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.editButton.setMinimumSize(QtCore.QSize(150, 25))
        self.editButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteButton.setMinimumSize(QtCore.QSize(150, 25))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 831, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Добавить ячейку"))
        self.editButton.setText(_translate("MainWindow", "Редактировать ячейку"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить ячейку"))


class AddCoffeeWidget(QMainWindow, UI_Form):
    def __init__(self, parent=None, film_id=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.setWindowTitle('Добавить')  # title
        self.pushButton.setText('Добавить')  # текст кнопки

        # подключение к БД
        self.connect = sqlite3.connect('coffee.sqlite')
        self.cursor = self.connect.cursor()

        # соединяем кнопку с соответствующей функцией в зависимости от назначения
        if film_id is None:
            self.pushButton.clicked.connect(self.do_adding)
        else:
            self.setWindowTitle('Редактировать')  # title
            self.pushButton.setText('Редактировать')  # текст кнопки

            self.item_id = self.parent.tableWidget.item(film_id, 0).text()
            self.type.setPlainText(self.parent.tableWidget.item(film_id, 1).text())
            self.roasting.setPlainText(self.parent.tableWidget.item(film_id, 2).text())
            self.comboBox.setCurrentText(self.parent.tableWidget.item(film_id, 3).text())
            self.taste.setPlainText(self.parent.tableWidget.item(film_id, 4).text())
            self.price.setPlainText(self.parent.tableWidget.item(film_id, 5).text())
            self.volume.setPlainText(self.parent.tableWidget.item(film_id, 6).text())
            self.pushButton.clicked.connect(self.do_editing)

    def get_verdict(self) -> bool:
        # вкус можно не добавлять
        if self.type.toPlainText() and self.roasting.toPlainText():
            try:
                price = int(self.price.toPlainText())
                volume = int(self.volume.toPlainText())
                if price <= 0 or volume <= 0:
                    return False
            except ValueError:
                return False
            return True
        return False

    def do_adding(self):
        if self.get_verdict():
            self.statusbar.clearMessage()
            self.cursor.execute(f'''INSERT INTO cafe(type, roasting, texture, taste, price, volume)
                                    VALUES("{self.type.toPlainText()}", "{self.roasting.toPlainText()}", 
                                           "{self.comboBox.currentText()}", "{self.taste.toPlainText()}",
                                           "{self.price.toPlainText()}", "{self.volume.toPlainText()}")
                                 ''')
            self.connect.commit()
            self.parent.update_table()
            self.close()

        else:
            self.statusbar.showMessage('Неправильно заполнена форма')

    def do_editing(self):
        if self.get_verdict():
            self.statusbar.clearMessage()

            self.cursor.execute(f'''
                                UPDATE cafe
                                SET type = "{self.type.toPlainText()}", 
                                    roasting = "{self.roasting.toPlainText()}",
                                    texture = "{self.comboBox.currentText()}", 
                                    taste = "{self.taste.toPlainText()}",
                                    price = "{self.price.toPlainText()}",
                                    volume = "{self.volume.toPlainText()}"
                                WHERE id = {self.item_id}''')
            self.connect.commit()
            self.parent.update_table()
            self.close()
        else:
            self.statusbar.showMessage('Неправильно заполнена форма')


class Coffee(QMainWindow, UI_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Кофе')

        # соединение с БД
        self.con = sqlite3.connect('coffee.sqlite')
        self.cursor = self.con.cursor()

        self.add_coffee_widget = AddCoffeeWidget(parent=self)

        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)
        self.deleteButton.clicked.connect(self.delete)

        self.update_table()

    # обновить таблицу
    def update_table(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(('ID', 'Сорт', 'Обжарка', 'Молотый/В зёрнах', 'Вкус', 'Цена',
                                                   'Объём/гр'))

        arr = self.cursor.execute('SELECT * from cafe').fetchall()

        # Заполняем таблицу элементами
        for i, row in enumerate(arr):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)

            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
                self.tableWidget.item(i, j)

    def add(self):
        self.statusbar.clearMessage()
        self.add_coffee_widget.show()

    def edit(self):
        self.statusbar.clearMessage()
        # редактируем только если выбран хотя-бы один элемент:
        if self.tableWidget.selectedItems():
            i = self.tableWidget.selectedItems()[0].row()
            self.edit_coffee_widget = AddCoffeeWidget(parent=self, film_id=i)
            self.edit_coffee_widget.show()
        else:
            self.statusbar.showMessage('Ничего не выбрано')

    def delete(self):
        # Получаем список элементов без повторов и их id
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]

        # если не выбран ни один элемент - ничего не делаем
        if not ids:
            self.statusbar.showMessage('Ничего не выбрано')

        else:
            self.statusbar.clearMessage()
            # Спрашиваем у пользователя подтверждение на удаление элементов
            valid = QMessageBox.question(
                self, '', "Действительно удалить элементы с id " + ",".join(ids),
                QMessageBox.Yes, QMessageBox.No)
            # Если пользователь ответил утвердительно, удаляем элементы.
            # Не забываем зафиксировать изменения
            if valid == QMessageBox.Yes:
                self.cursor.execute("DELETE FROM cafe WHERE id IN (" + ", ".join(
                    '?' * len(ids)) + ")", ids)
                self.con.commit()

                # обновляем таблицу
                self.update_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
