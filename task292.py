from sys import *
from math import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton)


class HarmonicApp(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("График гармонического колебания")
        self.setFixedSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        params_layout = QHBoxLayout()
        amp_box = QVBoxLayout()
        amp_label = QLabel("Амплитуда (м):")

        self.amp_edit = QLineEdit("1.0")
        amp_box.addWidget(amp_label)
        amp_box.addWidget(self.amp_edit)
        freq_box = QVBoxLayout()
        freq_label = QLabel("Частота (Гц):")

        self.freq_edit = QLineEdit("1.0")
        freq_box.addWidget(freq_label)
        freq_box.addWidget(self.freq_edit)
        phase_box = QVBoxLayout()
        phase_label = QLabel("Фаза (градусы):")

        self.phase_edit = QLineEdit("0")
        phase_box.addWidget(phase_label)
        phase_box.addWidget(self.phase_edit)

        params_layout.addLayout(amp_box)
        params_layout.addLayout(freq_box)
        params_layout.addLayout(phase_box)

        self.draw_button = QPushButton("Построить график")
        self.draw_button.clicked.connect(self.draw_graph)

        self.figure, self.axes = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        layout.addLayout(params_layout)
        layout.addWidget(self.draw_button)
        layout.addWidget(self.canvas)
        self.draw_graph()

    def draw_graph(self):
        try:
            amplitude = float(self.amp_edit.text())
            frequency = float(self.freq_edit.text())
            phase_deg = float(self.phase_edit.text())

            phase_rad =radians(phase_deg)

            time = [t * 0.01 for t in range(201)]
            puls = []
            for t in time:
                value = amplitude * sin(2 * pi * frequency * t + phase_rad)
                puls.append(value)

            self.axes.clear()
            self.axes.plot(time, puls, 'b-', linewidth=2)
            self.axes.set_xlabel('Время (с)', fontsize=10)
            self.axes.set_ylabel('Смещение (м)', fontsize=10)
            self.axes.set_title('График гармонического колебания', fontsize=12)
            self.axes.grid(True, linestyle='--', alpha=0.7)
            self.canvas.draw()

        except ValueError:
            self.axes.clear()
            self.axes.text(0.5, 0.5, 'Ошибка! Проверьте введенные значения',
                           horizontalalignment='center',
                           verticalalignment='center',
                           transform=self.axes.transAxes)
            self.canvas.draw()


if name == "main":
    app = QApplication(argv)
    window = HarmonicApp()
    window.show()
    sys.exit(app.exec_())