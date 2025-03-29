from sys import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, HBoxLayout, QLabel, QLineEdit, QPushButton,QComboBox)
from PyQt5.QtCore import Qt

class GasLawApp(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Закон Бойля-Мариотта")
        self.setFixedSize(800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        params_layout = QHBoxLayout()
        temp_layout = QVBoxLayout()
        temp_label = QLabel("Температура (К):")
        self.temp_input = QLineEdit("300")
        temp_layout.addWidget(temp_label)
        temp_layout.addWidget(self.temp_input)


        moles_layout = QVBoxLayout()
        moles_label = QLabel("Количество вещества (моль):")
        self.moles_input = QLineEdit("1")
        moles_layout.addWidget(moles_label)
        moles_layout.addWidget(self.moles_input)

        units_layout = QVBoxLayout()
        units_label = QLabel("Единицы давления:")
        self.units_combo = QComboBox()
        self.units_combo.addItems(["Па", "атм"])
        units_layout.addWidget(units_label)
        units_layout.addWidget(self.units_combo)

        params_layout.addLayout(temp_layout)
        params_layout.addLayout(moles_layout)
        params_layout.addLayout(units_layout)

        self.plot_button = QPushButton("Построить график")
        self.plot_button.clicked.connect(self.plot_graph)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        main_layout.addLayout(params_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)
        self.R = 8.314


    def plot_graph(self):
        try:
            T = float(self.temp_input.text())
            n = float(self.moles_input.text())
            unit = self.units_combo.currentText()
            if T <= 0 or n <= 0:
                raise ValueError("Значения должны быть положительными")
            volumes = [v * 0.1 for v in range(1, 101)]
            pressures = []
            for V in volumes:
                P = n * self.R * T / V
                if unit == "атм":
                    P = P / 101325
                pressures.append(P)
            self.ax.clear()
            self.ax.plot(volumes, pressures, 'g-')
            self.ax.set_xlabel('Объём (м³)')
            self.ax.set_ylabel(f'Давление ({unit})')
            self.ax.set_title('Зависимость давления от объёма (P-V диаграмма)')
            self.ax.grid(True)
            self.canvas.draw()
        except ValueError as e:
            self.ax.clear()
            error_msg = str(e) if str(e) else "Ошибка! Введите корректные числа"
            self.ax.text(0.5, 0.5, error_msg,
                         ha='center', va='center')
            self.canvas.draw()


if name == "main":
    app = QApplication(sys.argv)
    window = GasLawApp()
    window.show()
    sys.exit(app.exec_())