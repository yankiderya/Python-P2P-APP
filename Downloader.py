import socket
import os
from datetime import datetime

while 1:
    def create_Socket():
        global conn,conn1,addr,size,s,host,port
        s = socket.socket()
        host = input(str("Please enter an ip adress of the server : "))
        port = 5001
        s.connect((host, port))


        size = socket.socket()
        host1 = host
        port1 = 9999
        size.connect((host1, port1))
        print("Connected...")


    sourcedir = os.getcwd() + '/chunks'
    outputdira = os.getcwd() + '/Received Files'
    outputdirb = os.getcwd() + '/Content Dictionary'
    chunk = input("Please enter a filename for incoming file without index number : ")
    file_type=chunk.split(".",1)[1]





    def get_chunks(file, outputdir):

        create_Socket()
        c = size.recv(1223)
        p = int.from_bytes(c, byteorder='big')
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
        for i in range(1,6):
            with open(outputdir + '/' + file.split('.')[0] + "_" + str(i) + "."+file_type, "wb+") as infile:
                try:
                    error= False
                    data_file = s.recv(p)
                    infile.write(data_file)
                except:
                    error = True
                    errorlog = open("ClientErrorLog.txt", "a")
                    efile = file.split('.')[0] + "_" + str(i) + "."+file_type
                    now = datetime.now()
                    timeStamp = now.strftime("%m/%d/%Y, %H:%M:%S")
                    errorlog.write("Error: " + timeStamp + " , " + efile + " couldn't recieve from " + host + "\n")
                    errorlog.close()
                    continue
        if error:
            err= "ERROR: You couldn't recieve the whole file. <ClientErrorLog.txt> saved."
            print(err)
        else:
            print("The file received successfully!")






    def combine_chunks(inp, sourcedir, outputdir):
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        with open(outputdir + '/' + inp, 'wb') as outfile:
            for i in range(1, 6):
                with open(sourcedir + '/' + inp.split('.')[0] + "_" + str(i) + "."+file_type, "rb") as infile:
                    outfile.write(infile.read())
                    flag = 1









    def get_log():
        dosya = open("DownloadLog.txt", "a")
        now = datetime.now()
        chunks = os.listdir(os.getcwd() + '/Content Dictionary')
        timeStamp = now.strftime("%m/%d/%Y, %H:%M:%S")
        dosya.write("Time: " + timeStamp + "  Chunks: " + str(chunks) + "  From: " + host + "\n")
        dosya.close()



    get_chunks(chunk, outputdirb)
    get_log()
    combine_chunks(chunk, outputdirb, outputdira)

