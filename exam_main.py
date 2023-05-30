from PySide6 import QtWidgets
from typing import Union, Optional
from operator import add, sub, mul, truediv

from exam_culcul import Ui_Culculator  # Импортируем класс формы

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Culculator()
        self.ui.setupUi(self)
        self.ui.lbl_temp.clear()
        self.commands = []
        self.initSignals()

    def initSignals(self):
        for val in range(10):
            eval(f"self.ui.btn_{val}.clicked.connect(self.setVal)")
        # self.ui.btn_plus.clicked.connect(self.funcPlus)
        # self.ui.btn_equal.clicked.connect(self.funcEq)

        # Действия
        self.ui.btn_c.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)

        # Математические операции
        self.ui.btn_equal.clicked.connect(self.calculate)
        self.ui.btn_plus.clicked.connect(lambda: self.math_operation('+'))
        self.ui.btn_minus.clicked.connect(lambda: self.math_operation('-'))
        self.ui.btn_multi.clicked.connect(lambda: self.math_operation('*'))
        self.ui.btn_slash.clicked.connect(lambda: self.math_operation('/'))


    def setVal(self):
        buttonText = self.sender().text()
        le_text = self.ui.le_entry.text()
        if le_text and le_text !="0":
            self.ui.le_entry.setText(self.ui.le_entry.text()+buttonText)
        else:
            self.ui.le_entry.setText(buttonText)

    # Прописываем метод для добавления точки
    def add_point(self):
        if '.' not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + '.')

    # Прописываем метод для чистки всех полей
    def clear_all(self):
        self.ui.le_entry.setText('0')
        self.ui.lbl_temp.clear()

    # Прописываем метод чистки поля ввода
    def clear_entry(self):
        self.ui.le_entry.setText('0')

    # Прописываем статический метод чтобы обрезать лишние нули в числе
    @staticmethod
    def remove_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    # Прописываем метод для добавления временного выражения
    def add_temp(self, math_sign: str):
        if not self.ui.lbl_temp.text() or self.get_math_sing() == '=':
            self.ui.lbl_temp.setText(self.remove_zeros(self.ui.le_entry.text()) + f' {math_sign} ')
            self.ui.le_entry.setText('0')

    # Получение числа из поля ввода
    def get_entry(self) -> Union[int, float]:
        entry = self.ui.le_entry.text().strip('.')

        return float(entry) if '.' in entry else int(entry)

    # Получение числа из временного выражения
    def get_temp(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    # Получение знака из временного выражения
    def get_math_sing(self) -> Optional[str]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip('.').split()[-1]

    # Создание функции вычисления
    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        temp =  self.ui.lbl_temp.text()

        if temp:
            result = self.remove_zeros(str(operations[self.get_math_sing()](self.get_temp(), self.get_entry())))
            self.ui.lbl_temp.setText(temp + self.remove_zeros(entry) + ' =')
            self.ui.le_entry.setText(result)
            return result

    # Функция для математических операций
    def math_operation(self, math_sign: str):
        temp = self.ui.lbl_temp.text()
        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sing() != math_sign:
                if self.get_math_sing() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{math_sign} ')
            else:
                self.ui.lbl_temp.setText(self.calculate() + f'{math_sign}')



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
