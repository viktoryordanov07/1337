==[SecureVault]==


**DISCLAIMER**
This application is made for educational purposes only. It DOES NOT INTEND to replace any existing encryption programs and softwares. It is simply made for fun and education.

A cybersecurity-inspired encrypted file vault built with Python and PySide6.

SecureVault is a desktop application that allows users to securely encrypt and decrypt files through a cyber-themed graphical interface inspired by terminal and control-center systems.


--{Features}--
Secure file encryption using Fernet encryption
Password-based encryption system
File decryption and restoration
Encrypted vault folder system
Login authentication system
Boot sequence simulation
Cybersecurity-inspired GUI
Cross-platform support (Windows + macOS)
Modular Python project structure
Technologies Used
Python
PySide6
Cryptography (Fernet)
SHA-256 hashing
VS Code

--{Project Structure}--
SecureVault/
│
├── main.py
├── auth.py
├── login_ui.py
├── boot_screen.py
├── dashboard.py
├── crypto_utils.py
│
└── vault/
    ├── encrypted/
    └── restored/

==[How It Works]==
--{Authentication}--

The user logs into the system using a username and password.

These passwords are INSIDE of the source code and can be changed to YOUR liking.
Current USERNAME and PASSWORD are:
admin
admin123

Passwords are hashed using SHA-256 before verification.

==[Encryption]==

When a file is selected:

The file is read as binary data
A key is generated from the user password
The file is encrypted using Fernet encryption
The encrypted file is stored inside the vault

Encrypted files cannot be opened normally without decryption.

==[Decryption]==

To restore a file:

The encrypted vault file is selected
The correct password is entered
The application decrypts the file
The original file is restored
Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/SecureVault.git
cd SecureVault
2. Install dependencies
pip install pyside6 cryptography

If pip does not work:

python -m pip install pyside6 cryptography
3. Run the application
