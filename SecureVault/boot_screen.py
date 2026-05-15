from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer


class BootScreen(QWidget):
    def __init__(self, on_finished):
        super().__init__()

        self.on_finished = on_finished

        self.setWindowTitle("Boot Sequence")
        self.setFixedSize(1280, 720)

        layout = QVBoxLayout()

        self.label = QLabel("")
        self.label.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #00ff99;
        """)

        layout.addWidget(self.label)
        self.setLayout(layout)

        self.messages = [
            "Initializing Secure Vault...",
            "Loading encryption modules...",
            "Verifying system integrity...",
            "Connecting secure kernel...",
            "ACCESS GRANTED ✔"
        ]

        self.i = 0
        self.p = 0

        self.t = QTimer()
        self.t.timeout.connect(self.text)
        self.t.start(700)

        self.b = QTimer()
        self.b.timeout.connect(self.bar)
        self.b.start(100)

    def text(self):
        if self.i < len(self.messages):
            self.label.setText(self.label.text() + self.messages[self.i] + "\n")
            self.i += 1
        else:
            self.t.stop()

    def bar(self):
        self.p += 5

        bar = "█" * (self.p // 10)
        empty = "░" * (10 - self.p // 10)

        self.label.setText(
            "\n".join(self.messages[:self.i]) +
            f"\n\n[{bar}{empty}] {self.p}%"
        )

        if self.p >= 100:
            self.b.stop()
            self.on_finished()
            self.close()