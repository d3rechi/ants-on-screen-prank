import sys
import random
import math
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap, QPainter, QColor, QTransform
from PyQt6.QtCore import Qt, QTimer, QPointF, QRectF

class Ant:
    def __init__(self, x, y, image):
        self.pos = QPointF(x, y)
        self.image = image
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 3)
        self.turn_rate = random.uniform(0.1, 0.5)
        self.rotation = 0  
    def move(self, width, height):
        self.angle += random.uniform(-self.turn_rate, self.turn_rate)
        
        self.pos += QPointF(math.cos(self.angle) * self.speed, 
                            math.sin(self.angle) * self.speed)
        
        self.pos.setX(self.pos.x() % width)
        self.pos.setY(self.pos.y() % height)

        target_rotation = math.degrees(self.angle) + 90  
        rotation_diff = (target_rotation - self.rotation + 180) % 360 - 180
        self.rotation += rotation_diff * 0.1  

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crawling Ants")
        self.setGeometry(100, 100, 1920, 1080)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.ant_image = QPixmap("ant.png").scaled(20, 10, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        
        self.ants = [Ant(random.choice([-20, self.width() + 20]), 
                         random.choice([-20, self.height() + 20]), 
                         self.ant_image) for _ in range(10)]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_ants)
        
        QTimer.singleShot(100, self.start_animation)

    def start_animation(self):
        self.timer.start(45)  

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        
        painter.fillRect(self.rect(), QColor(0, 0, 0, 0))
        
        for ant in self.ants:
            painter.save()
            painter.translate(ant.pos)
            painter.rotate(ant.rotation)
            painter.drawPixmap(QRectF(-self.ant_image.width() / 2, -self.ant_image.height() / 2, 
                                      self.ant_image.width(), self.ant_image.height()), self.ant_image, 
                               QRectF(self.ant_image.rect()))
            painter.restore()

    def move_ants(self):
        for ant in self.ants:
            ant.move(self.width(), self.height())
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec())
