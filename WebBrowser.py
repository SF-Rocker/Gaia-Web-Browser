from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys

app = QApplication(sys.argv)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 873)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layout = QVBoxLayout(self.centralwidget)

        # Create a QPushButton to load the URL from the QLineEdit
        self.loadButton = QPushButton("Load")
        self.loadButton.clicked.connect(self.loadUrl)
        self.layout.addWidget(self.loadButton)

        # Create a QPushButton to load a specific URL ("http://www.gaiaonline.com/rallytest")
        self.rally3Button = QPushButton("Rally 3")
        self.rally3Button.clicked.connect(self.loadRally3Url)
        self.layout.addWidget(self.rally3Button)

        # Create a QLineEdit for entering the URL
        self.urlInput = QLineEdit()
        self.urlInput.setPlaceholderText("Enter URL")
        self.layout.addWidget(self.urlInput)

        # Create the QWebEngineView
        self.webEngineView = QWebEngineView()
        self.layout.addWidget(self.webEngineView)

        self.webEngineView.setUrl(QUrl("https://www.gaiaonline.com/"))
        self.webEngineView.setObjectName("webEngineView")
        MainWindow.setCentralWidget(self.centralwidget)

    def loadUrl(self):
        url = self.urlInput.text()
        if url:
            self.webEngineView.setUrl(QUrl(url))

    def loadRally3Url(self):
        self.webEngineView.setUrl(QUrl("http://www.gaiaonline.com/rallytest"))

    def retranslateUi(self, MainWindow):
        pass

if __name__ == "__main__":
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
