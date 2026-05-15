from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from auth import authenticate


class LoginWindow(QWidget):
    def __init__(self, on_success):
        super().__init__()

        self.on_success = on_success

        self.setWindowTitle("Secure Vault Login")
        self.setFixedSize(1280, 720)

        layout = QVBoxLayout()

        title = QLabel("--[SECURE ACCESS TERMINAL]--")
        layout.addWidget(title)

        self.username = QLineEdit()
        self.username.setPlaceholderText("--[USERNAME]--")
        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("--[PASSWORD]--")
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        btn = QPushButton("LOGIN")
        btn.clicked.connect(self.check)
        layout.addWidget(btn)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: #00ff99;
                font-family: Consolas;
                font-size: 22px;
                font-weight: bold;
            }

            QLineEdit {
                background-color: #111;
                border: 1px solid #00ff99;
                padding: 10px;
                font-size: 16px;
            }

            QPushButton {
                border: 2px solid #00ff99;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #00ff99;
                color: black;
            }
        """)

    def check(self):
        if authenticate(self.username.text(), self.password.text()):
            QMessageBox.information(self, "ACCESS", "GRANTED")
            self.on_success()
            self.close()
        else:
            QMessageBox.critical(self, "ACCESS", "DENIED")