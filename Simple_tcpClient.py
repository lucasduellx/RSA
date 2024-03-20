import socket
from rsa import RSA

def main():

    server_address = ('192.168.15.19', 1300)
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(server_address)

    rsa = RSA()

    public_key_data = client_socket.recv(4096)
    public_key = eval(public_key_data.decode())

    #message = input("Mensagem:")
    message = 'The information security is of significant importance to ensure the privacy of communications'

    encrypted_message = rsa.encrypt(message, public_key)

    client_socket.sendall(str(encrypted_message).encode())

    client_socket.close()

if __name__ == "__main__":
    main()
