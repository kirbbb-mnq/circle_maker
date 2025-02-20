import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(QPoint(x + diameter // 2, y + diameter // 2), diameter // 2, diameter // 2)  # Рисуем окружность

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CircleWidget()
    widget.show()
    sys.exit(app.exec())