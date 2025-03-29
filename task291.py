from sys import *
from math import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton)


class PhysicsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Траектория полета тела")
        self.setFixedSize(800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        input_layout = QHBoxLayout()

        speed_layout = QVBoxLayout()
        speed_label = QLabel("Начальная скорость (м/с):")
        self.speed_input = QLineEdit()
        self.speed_input.setText("10")
        speed_layout.addWidget(speed_label)
        speed_layout.addWidget(self.speed_input)

        angle_layout = QVBoxLayout()
        angle_label = QLabel("Угол броска (градусы):")
        self.angle_input = QLineEdit()
        self.angle_input.setText("45")
        angle_layout.addWidget(angle_label)
        angle_layout.addWidget(self.angle_input)

        input_layout.addLayout(speed_layout)
        input_layout.addLayout(angle_layout)

        self.plot_button = QPushButton("Построить траекторию")
        self.plot_button.clicked.connect(self.plot_trajectory)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)


    def plot_trajectory(self):
        try:
            speed = float(self.speed_input.text())
            angle_deg = float(self.speed_input.text())
            angle_rad = radians(angle_deg)
            g=10

            t_total = 2 * speed * sin(angle_rad) / g


            time_points = []
            t = 0
            while t <= t_total:
                time_points.append(t)
                t += 0.01

            x_points = []
            y_points = []
            for t in time_points:
                x = speed * cos(angle_rad) * t
                y = speed * sin(angle_rad) * t - 0.5 * g * t ** 2
                x_points.append(x)
                y_points.append(y)

            self.ax.clear()
            self.ax.plot(x_points, y_points, 'b-')
            self.ax.set_xlabel('Расстояние (м)')
            self.ax.set_ylabel('Высота (м)')
            self.ax.set_title('Траектория полета тела')
            self.ax.grid(True)


            self.canvas.draw()

        except ValueError:
            self.ax.clear()
            self.ax.text(0.5, 0.5, 'Ошибка! Введите числа в поля ввода',
                         ha='center', va='center')
            self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(argv)
    window = PhysicsApp()
    window.show()
    exit(app.exec_())