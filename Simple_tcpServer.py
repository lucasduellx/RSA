import socket
from rsa import RSA

def main():

    serverPort = 1300

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSocket.bind(("", serverPort))

    serverSocket.listen(5)

    print("TCP Server\n")
    
    rsa = RSA()
    
    public_key, private_key = rsa.generateKey()
    
    print(str(public_key))
    print(str(private_key))
    
    while True:

	    connectionSocket, addr = serverSocket.accept()
	    
	    connectionSocket.sendall(str(public_key).encode())

	    encrypted_message_data = connectionSocket.recv(4096)
	    encrypted_message = eval(encrypted_message_data.decode())

	    decrypted_message = rsa.decrypt(encrypted_message,private_key)

	    print("Received From Client:", decrypted_message)

	    connectionSocket.close()

if __name__ == "__main__":
    main()
