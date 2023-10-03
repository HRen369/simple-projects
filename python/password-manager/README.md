# Python Password Manager
This is a simple password manager made in python
The functionality involves these main features:
- View Accounts
- Add Accounts
- Delete Accounts

The master file that contains all of your accounts is encrypted with AES-256 Mode CBC and they are stored locally on your PC.

## .env
This program requires you to have a .env file with the following variables.
- `MASTER_PASSWORD`: Currently, not used but will be used in the future to validate.
- `KEY`: This is the Key you use to encrypt and decrypt the masterfile.
- `IV`: This used with AES's CBC mode.
- `MASTER_FILE_NAME`: The name of your encrypted master file.

If you want to get started immediately, you can use `python generateDotEnv.py` to create a default `.env` file. 
NOTE: DO NOT call the file twice when you have a encryptedMasterFile in your folder. This will override your encryptedMasterFile. There are currently no safeggaurds against this.

## Steps(for Windows 10)
1. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
2. Scripts\activate.ps1 or Scripts\activate.bat
3. pip -r requirements.txt
4. python generateDotEnv.py
4. python passwordManager.py