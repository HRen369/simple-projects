# MD5 File Verifer
## Description
This program auto generates a veri.json file that contains your md5 hashes files

## Commands

### Local Commands
These commands are done by looking at the current and subdirectories.

`python write`: Grabs alls files in current and sub directories. Then gets MD5 hashes and stores them in `veri.json`

`python verify`: Verfies all files in current and subdirectories with local `veri.json`

`python write-verify`: Does both `write` and `verify` commands to current and sub directories

`python delete`: Deletes local `veri.json`
