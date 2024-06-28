import os,sys,hashlib,json

def calculate_md5(data):
    with open(data, 'rb') as file_to_check:
        data = file_to_check.read()    
        return hashlib.md5(data).hexdigest()

def write_md5_file():
    with open('veri.json', 'w', encoding='utf-8') as f:
        json.dump(create_verifications(), f, ensure_ascii=False, indent=4)


def create_verifications():
    root_dir = os.getcwd()

    # Iterates through all files in all subdirectories
    verifications = {}
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file not in ["veri.json", "file_checker.py"]:
                curr_dir = subdir[len(root_dir)+1:len(subdir)]
                try:
                    name = os.path.join(curr_dir, file)
                    verifications[name] = calculate_md5(os.path.join(subdir,file))
                                            
                except UnicodeDecodeError:
                    print("--------------------------------")
                    print("-- Verification Aborted --")
                    print(f'ERROR: {os.path.join(subdir,file)}')
                    exit(0)
    return {
    "root": root_dir,
    "verifications":verifications
    }



def add_new_md5(file_dir):
    with open("veri","a") as veri:
        veri.write(f'{file_dir}++++{calculate_md5(file_dir)}\n')


def verify_md5s(comp_dir):
    f = open('veri.json')
    data = json.load(f)
    
    for subdir, dirs, files in os.walk(comp_dir):
        for file in files:
            if file not in ["veri.json", "file_checker.py"]:
                try:
                    name = os.path.join(subdir[len(comp_dir)+1:len(subdir)], file)
                    ori_md5 = data['verifications'][name]                
                    new_md5 = calculate_md5(os.path.join(comp_dir,name))
                    if ori_md5 != new_md5:
                        print(f"NOT SAME MD5 HASH: {name}")
                        exit(1)
                except UnicodeDecodeError:
                    print("--------------------------------")
                    print("-- Verification Aborted --")
                    print(f'ERROR: {name}')
                    print("--------------------------------")
                    exit(1)
                except KeyError:
                    print("--------------------------------")
                    print("-- Verification Aborted --")
                    print(f'NO FILE: {name}')
                    print("--------------------------------")
                    exit(1)

    f.close()    

    print("--- All Files Verified ---")


def self_verify_md5s():
    f = open('veri.json')
    data = json.load(f)
    
    verify_md5s(data['root'])

    f.close()

def main():
    if len(sys.argv) == 1:
        print("No Commands")
    elif len(sys.argv) == 2:
        command = sys.argv[1]
        if command == "write":
            write_md5_file()
        elif command == "write-verify":
            write_md5_file()
            self_verify_md5s() 
        elif command == "verify":
            verify_md5s("kp")
        elif command == "delete":
            os.remove("veri.json")
        else:
            print("Not Valid Command")
    elif sys.argv[1] == "verify" and len(sys.argv) == 3:
        verify_md5s(sys.argv[2])
    else:
        print("Too many commands")

if __name__ == '__main__':
    main()
    # verify_md5s("C:\\.personal\\personal-projects\\txt-rpg\\other_dir\\hi")