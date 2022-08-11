import socket
import codecs

def cript(str_, chave):
    str_retorno =  ""
    max = 126
    for a in str_:
        num_cript = ord(a) + chave
    
        if(num_cript > max):
            num_cript = 32 + (num_cript % max)
        
        char_crip = chr(num_cript)
    
        str_retorno = str_retorno + char_crip
        
    return str_retorno


def decript(str_, chave):
    str_retorno =  ""
    min = 32
    for a in str_:
        num_cript = ord(a) - chave
    
        if(num_cript < min):
            num_cript = 126 - (min % num_cript)
        
        char_crip = chr(num_cript)
    
        str_retorno = str_retorno + char_crip
        
    return str_retorno

HOST = '127.0.0.1'# The server's hostname or IP address
PORT = 65432        # The port used by the server
while True:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print ("Successful connection. ")


        print("Enter a message: ")
        str_ = input()
        chave = int(input("Qual a chave ? (valores entre 0 e 26)  "))
        out = cript(str_, chave)
        print(out)  
        msg = out

        msg_as_bytes = str.encode(msg)
        s.sendall(msg_as_bytes)
        print('Sent: ', msg)


        data = s.recv(1024)
        print('Received: ', codecs.decode(data))
        s.close()
        break

    while True:
        HOST1 = '192.168.15.55' # localhost 
        PORT1 = 65432        # Port to listen on 
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss.bind((HOST1, PORT1))
        ss.listen()
        print("Listem ip:" + HOST1 + " port: " + str(PORT))

        s, addr = ss.accept()

        info = socket.getnameinfo(addr, socket.NI_NUMERICSERV)

        print("Connected by ", info)

        while True:
            data = s.recv(1024)
            if not data:
                break
            print("Received: ", codecs.decode(data))
            s.sendall(data)
            chave = int(input("Qual a Chave ? (valores entre 0 e 26) " ))
            str_ = codecs.decode(data)
            out = decript(str_, chave)
            print(out)  
            break
        ss.close()
        break