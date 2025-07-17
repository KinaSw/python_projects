import sys
import numpy as np
import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paprotka Barnsleya")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        input_layout = QHBoxLayout()
        self.iter_label = QLabel("Liczba iteracji")
        self.iter_value = QLineEdit()
        self.iter_value.setText("100000")
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.draw)

        self.layout.addLayout(input_layout)
        input_layout.addWidget(self.iter_label)
        input_layout.addWidget(self.iter_value)
        input_layout.addWidget(self.start_button)

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setLabel("left", "Y")
        self.plot_widget.setLabel("right", "X")
        self.layout.addWidget(self.plot_widget)

        self.plot_widget.setXRange(-3, 3)
        self.plot_widget.setYRange(0, 10)

    def draw(self):
        n = int(self.iter_value.text())
        x = np.zeros(n+1)
        y = np.zeros(n+1)

        for i in range(n):
            r = random.random()
            if r <= 0.01:
                x[i + 1] = 0
                y[i + 1] = 0.16 * y[i]
            elif r <= 0.08:
                x[i + 1] = 0.2 * x[i] - 0.26 * y[i]
                y[i + 1] = 0.23 * x[i] + 0.22 * y[i] + 1.6
            elif r <= 0.15:
                x[i + 1] = -0.15 * x[i] + 0.28 * y[i]
                y[i + 1] = 0.26 * x[i] + 0.24 * y[i] + 0.44
            else:
                x[i + 1] = 0.85 * x[i] + 0.04 * y[i]
                y[i + 1] = -0.04 * x[i] + 0.85 * y[i] + 1.6

        self.plot_widget.plot(x, y, pen=None, symbol='o', symbolSize=1, symbolBrush=(0, 255, 0))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
