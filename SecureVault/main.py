import sys
from PySide6.QtWidgets import QApplication

from login_ui import LoginWindow
from boot_screen import BootScreen
from dashboard import Dashboard


def open_dashboard():
    global dash
    dash = Dashboard()
    dash.show()


def start_boot():
    global boot
    boot = BootScreen(on_finished=open_dashboard)
    boot.show()


app = QApplication(sys.argv)

login = LoginWindow(on_success=start_boot)
login.show()

sys.exit(app.exec())