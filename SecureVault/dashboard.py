import os
import json
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QPushButton,
    QFileDialog, QInputDialog
)

from crypto_utils import get_cipher, encrypt_file, decrypt_file


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Secure Vault // CONTROL CENTER")
        self.setFixedSize(1280, 720)

        layout = QVBoxLayout()

        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        layout.addWidget(self.terminal)

        self.btn_select = QPushButton("SELECT FILE")
        self.btn_encrypt = QPushButton("ENCRYPT → VAULT")
        self.btn_decrypt = QPushButton("DECRYPT FILE")

        layout.addWidget(self.btn_select)
        layout.addWidget(self.btn_encrypt)
        layout.addWidget(self.btn_decrypt)

        self.setLayout(layout)

        self.file_path = None

        self.btn_select.clicked.connect(self.select_file)
        self.btn_encrypt.clicked.connect(self.encrypt_to_vault)
        self.btn_decrypt.clicked.connect(self.decrypt_file)

        self.setStyleSheet("""
            QWidget {
                background-color: #020202;
                color: #00ff99;
                font-family: Consolas;
                font-size: 16px;
                font-weight: bold;
            }

            QTextEdit {
                background-color: black;
                border: 1px solid #00ff99;
                font-size: 14px;
            }

            QPushButton {
                border: 2px solid #00ff99;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #00ff99;
                color: black;
            }
        """)

        self.log("SYSTEM ONLINE")

    def log(self, msg):
        self.terminal.append(f"> {msg}")

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file:
            self.file_path = file
            self.log(f"SELECTED: {file}")

    def encrypt_to_vault(self):
        if not self.file_path:
            self.log("NO FILE SELECTED")
            return

        password, ok = QInputDialog.getText(self, "Password", "Enter vault password:")
        if not ok:
            return

        cipher = get_cipher(password)

        with open(self.file_path, "rb") as f:
            data = f.read()

        filename = os.path.basename(self.file_path)

        metadata = json.dumps({"filename": filename}).encode()
        payload = metadata + b"|||" + data

        encrypted = encrypt_file(cipher, payload)

        os.makedirs("vault/encrypted", exist_ok=True)

        save_path = f"vault/encrypted/{filename}.vault"

        with open(save_path, "wb") as f:
            f.write(encrypted)

        self.log(f"ENCRYPTED → {save_path}")

    def decrypt_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Vault File")
        if not file:
            return

        password, ok = QInputDialog.getText(self, "Password", "Enter vault password:")
        if not ok:
            return

        cipher = get_cipher(password)

        with open(file, "rb") as f:
            encrypted = f.read()

        try:
            decrypted = decrypt_file(cipher, encrypted)

            meta, data = decrypted.split(b"|||", 1)
            filename = json.loads(meta.decode())["filename"]

            os.makedirs("vault/restored", exist_ok=True)

            output = f"vault/restored/{filename}"

            with open(output, "wb") as f:
                f.write(data)

            self.log(f"RESTORED → {filename}")

        except:
            self.log("ERROR: WRONG PASSWORD OR FILE CORRUPTED")