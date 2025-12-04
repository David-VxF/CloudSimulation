import os
base = "storage"
def upload_file(username):
    userPath = os.path.join(base, username)
    if not os.path.exists(userPath):
        os.makedirs(userPath)
    while True:
        file_name = input("enter the name of the file to upload: ")
        file_path = os.path.join(userPath, file_name)
        if os.path.exists(file_path):
            print("file already exists, please try again.")
            continue
        with open(file_path, 'w') as f:
            f.write("")
        print(f"file '{file_name}' successfully uploaded.")
        break

def view_files(username):
    userPath = os.path.join(base, username)
    if not os.path.exists(userPath):
        print("folder is empty.")
        return
    files = os.listdir(userPath)
    if not files:
        print("no files have been uploaded yet.")
    else:
        print("uploaded files:")
        for file in files:
            no = 1
            print(f"{no}. {file}")
            no += 1

def delete_file(username):
    userPath = os.path.join(base, username)
    if not os.path.exists(userPath):
        print("folder is empty.")
        return
    files = os.listdir(userPath)
    if not files:
        print("no files have been uploaded yet.")
        return
    print("uploaded files:")
    no = 1
    for file in files:
        print(f"{no}. {file}")
        no += 1
    file_number = input("enter the number of the file you want to delete: ")
    try:
        file_index = int(file_number) - 1
        if 0 <= file_index < len(files):
            file_name = files[file_index]
            file_path = os.path.join(userPath, file_name)
            if os.path.exists(file_path):
                auth = input(f"are you sure you want to delete the file '{file_name}'? (y/n): ")
                if auth.lower() != 'y':
                    print("deletion cancelled.")
                    return
                os.remove(file_path)
                print(f"file '{file_name}' successfully deleted.")
            else:
                print("file not found.")
    except ValueError:
        print("invalid input.")
