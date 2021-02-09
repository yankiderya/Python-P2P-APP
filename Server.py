import socket
import os
import math
from datetime import datetime

while 1:
    sharing_file = input("Please enter the file name you want to share:")
    file_type = sharing_file.split(".", 1)[1]
    directory = os.getcwd() + '/chunks'


    def create_socket():
        global addr, conn, conn1,s,host,port

        s = socket.socket()
        host = socket.gethostbyname(socket.gethostname())
        port = 5001
        s.bind((host, port))
        s.listen(5)
        print("Server Ip: "+host)
        print("Waiting for any incoming connections ... ")
        conn, addr = s.accept()
        print(addr, "Has connected to the server")

        size = socket.socket()
        host1 = host
        port1 = 9999
        size.bind((host1, port1))
        size.listen(5)
        conn1, addr1 = size.accept()


    def divide_into_chunks(file, fileName, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        c = os.path.getsize(file)
        CHUNK_SIZE = math.ceil(math.ceil(c) / 5)
        cnt = 1
        with open(file, 'rb') as infile:
            divided_file = infile.read(int(CHUNK_SIZE))
            while divided_file:
                name = directory + "/" + fileName.split('.')[0] + "_" + str(cnt) + "."+file_type
                with open(name, 'wb+') as div:
                    div.write(divided_file)
                cnt += 1
                divided_file = infile.read(int(CHUNK_SIZE))


    divide_into_chunks(sharing_file, sharing_file, directory)


    def send_chunks(file, sourcedir):
        create_socket()
        if not os.path.exists(sourcedir):
            os.makedirs(sourcedir)
        c = os.path.getsize(file)
        print(c)
        CHUNK_SIZE = math.ceil(math.ceil(c) / 5)
        bytechunksize = CHUNK_SIZE.to_bytes(4, 'big')
        conn1.send(bytechunksize)
        for i in range(1, 6):
            with open(sourcedir + '/' + file.split('.')[0] + "_" + str(i) + "."+file_type, "rb") as infile:
                try:
                    error= False
                    data_file = infile.read(int(c))
                    conn.send(data_file)
                except:
                    error = True
                    errorlog= open("ServerErrorLog.txt","a")
                    efile= file.split('.')[0] + "_" + str(i) + "."+file_type
                    newAdress = ''.join(str(addr))
                    now = datetime.now()
                    timeStamp = now.strftime("%m/%d/%Y, %H:%M:%S")
                    errorlog.write("Error: " +timeStamp+" , "+ efile + " couldn't send to "+newAdress +"\n" )
                    errorlog.close()
                    continue
        if error:
            err= "ERROR: You couldn't send the whole file. <ServerErrorLog.txt> saved."
            print(err)
        else:
            print("The file sent succesfully!")









    def log():
        log = open("ServerLog.txt", "a")
        file = os.listdir(os.getcwd() + '/chunks')
        now = datetime.now()
        timeStamp = now.strftime("%m/%d/%Y, %H:%M:%S")
        newFileName = file
        newAdress = ''.join(str(addr))
        log.write("Time: " + timeStamp + "  Chunks:" + str(
            newFileName) + "  Sent to: " + newAdress + " Downloaded From: "+host+"\n")
        log.close()


    send_chunks(sharing_file, directory)
    log()














