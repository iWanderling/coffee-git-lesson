import sys
import sqlite3
from mainUI import UI_Main
from addEditCoffeeForm import UI_Form
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtWidgets


class AddCoffeeWidget(QMainWindow, UI_Form):
    def __init__(self, parent=None, film_id=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.setWindowTitle('Добавить')  # title
        self.pushButton.setText('Добавить')  # текст кнопки

        # подключение к БД
        self.connect = sqlite3.connect('../data/coffee.sqlite')
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
        self.con = sqlite3.connect('../data/coffee.sqlite')
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
