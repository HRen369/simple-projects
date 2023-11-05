# Python Keylogger

## About
This is a keylogger made with Python. It's a simple program that 
- creates a `keylogged.txt` file
- appends to the `keylogged.txt` file
Note that this `keylogged.txt` is in the gitignore
Use `[Esc]` key to stop the keylogger

## Set up without env
1. pip -r requirements.txt
2. python keylogger.py

## Window Virtual Env Steps(for Windows 10)
1. python -m venv .
2. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
3. Scripts\activate.ps1 or Scripts\activate.bat
4. pip -r requirements.txt
5. python keylogger.py