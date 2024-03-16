# from PySide2.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
# from PySide2.QtGui import QImage, QPixmap, QPainter, QColor, QBrush, QPen, QPainterPath
# from PySide2.QtCore import Qt, QRectF

# app = QApplication([])

# # Create a widget and a layout
# widget = QWidget()
# layout = QVBoxLayout()
# widget.setLayout(layout)

# # Load an image
# image = QImage("./resources/others/brand-name.png")

# # Create a QPixmap from the QImage
# pixmap = QPixmap.fromImage(image)

# # Create a QPainter to perform the drawing
# # painter = QPainter(pixmap)

# # # Set the brush to a semi-transparent, white color
# # painter.setBrush(QColor(255, 255, 255, 127))

# # # Draw a rectangle over the entire image
# # painter.drawRect(pixmap.rect())

# # # End the QPainter's drawing
# # painter.end()

# # Create a QLabel and set its pixmap to the blurred image
# label = QLabel()
# label.setPixmap(pixmap)

# # Add the QLabel to the layout
# layout.addWidget(label)

# # Show the widget
# widget.show()

# # Start the application
# app.exec_()


# from PySide2.QtWidgets import QGraphicsBlurEffect, QFrame, QApplication, QVBoxLayout, QWidget
# from PySide2.QtGui import QPixmap, QPainter
# import sys

# class ImageFrame(QFrame):
#     def __init__(self, image_path, parent=None):
#         super().__init__(parent)
#         self.pixmap = QPixmap(image_path)
#         self.blur_effect = QGraphicsBlurEffect()
#         self.blur_effect.setBlurRadius(10)  # Set the blur radius
#         self.setGraphicsEffect(self.blur_effect)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.drawPixmap(self.rect(), self.pixmap)

# app = QApplication(sys.argv)

# # Create a frame with the image
# frame = ImageFrame("./resources/others/brand-name.png")

# # Create a layout and add the frame to it
# layout = QVBoxLayout()
# layout.addWidget(frame)

# # Create a window, set its layout and show it
# window = QWidget()
# window.setLayout(layout)
# window.show()

# sys.exit(app.exec_())


# from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGraphicsBlurEffect, QFrame
# from PySide2.QtGui import QPixmap, QPainter
# from PySide2.QtCore import Qt

# class BlurBackgroundWidget(QWidget):
#     def __init__(self, parent=None):
#         super(BlurBackgroundWidget, self).__init__(parent)
#         self.frame = QFrame(self)
#         self.frame.setGeometry(50, 50, 200, 200)
#         self.label = QLabel("Hello, World!", self.frame)
#         self.label.move(50, 50)

#     def resizeEvent(self, event):
#         # Create a QPixmap of the current frame
#         pixmap = QPixmap(self.frame.size())
#         self.frame.render(pixmap)

#         # Apply the blur effect
#         blur_effect = QGraphicsBlurEffect()
#         blur_effect.setBlurRadius(10)
#         pixmap = blur_effect.sourcePixmap(Qt.DeviceCoordinates, pixmap.rect())

#         # Create a semi-transparent QPixmap and paint the blurred QPixmap onto it
#         semi_transparent_pixmap = QPixmap(self.frame.size())
#         semi_transparent_pixmap.fill(Qt.transparent)
#         painter = QPainter(semi_transparent_pixmap)
#         painter.setOpacity(0.5)
#         painter.drawPixmap(0, 0, pixmap)
#         painter.end()

#         # Set the semi-transparent QPixmap as the background of the frame
#         self.frame.setStyleSheet("background-image: url(%s);" % semi_transparent_pixmap)

# if __name__ == "__main__":
#     app = QApplication([])
#     widget = BlurBackgroundWidget()
#     widget.show()
#     app.exec_()


import getmac