# Python Password Manager
This is a simple password manager made in python
The functionality involves these main features:
- View Accounts
- Add Accounts
- Delete Accounts

The program uses password validation at each option. The master file that contains all of your accounts is encrypted with AES-256 Mode CBC and they are stored locally on your PC.

## .env
This program requires you to have a .env file with the following variables.
- `MASTER_PASSWORD`: Currently, not used but will be used in the future to validate.
- `KEY`: This is the Key you use to encrypt and decrypt the masterfile.
- `IV`: This used with AES's CBC mode.
- `MASTER_FILE_NAME`: The name of your encrypted master file.

If you want to get started immediately, you can use `python generateDotEnv.py` to create a default `.env` file. 
NOTE: the  `generateDotEnv.py` uses a hardcoded master password, changing is recommended. Also, `generateDotEnv.py` checks to see if a `.env` file exsists. Be careful of overriding previous `.env` files. 

## Set up without env
1. pip -r requirements.txt
2. python `generateDotEnv.py`
3. python `passwordManager.py`

## Window Virtual Env Steps(for Windows 10)
1. python -m venv .
2. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
3. Scripts\activate.ps1 or Scripts\activate.bat
4. pip -r requirements.txt
5. python `generateDotEnv.py`
6. python `passwordManager.py`