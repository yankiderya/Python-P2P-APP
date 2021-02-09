from socket import *
import json
filename="Usernames&Chunks.txt"

def create_file(file_name):
    with open(file_name, 'a') as text:
        text.write("-----------Users and Chunks-----------"+"\n")
create_file(filename)
while 1:
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('', 5000))
    m = s.recvfrom(1024)
    b = json.loads(m[0].decode('utf'))
    print("Username: "+ b["username"] +"  Files: " +str(b["files"]) + "  Chunks: "+ str(b["chunks"]) )
    string = "Username: " + b["username"] + "  Chunks: " + str(b["chunks"]) +" Files:" + str(b["files"])

    def save_users_and_chunks(filename, search_word):
        with open('Usernames&Chunks.txt', 'r+') as file:
            contents = file.read()
            if search_word in contents:
                    found="Word Found"
            else:
                file.write(search_word + "\n")



    save_users_and_chunks(filename,string )














