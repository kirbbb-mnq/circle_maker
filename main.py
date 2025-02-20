import sys
import random

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(150, 120, 100, 30)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Кнопка")
        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter, kor) in self.circles:
            painter.setBrush(QColor(kor[0], kor[1], kor[2]))
            painter.drawEllipse(QPoint(x + diameter // 2, y + diameter // 2), diameter // 2, diameter // 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CircleWidget()
    widget.show()
    sys.exit(app.exec())