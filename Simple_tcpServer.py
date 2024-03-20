import socket
from rsa import RSA

def main():
    # Porta do servidor
    serverPort = 1300

    # Cria o socket TCP
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liga o socket ao endereço e à porta
    serverSocket.bind(("", serverPort))

    # Escuta por conexões de clientes
    serverSocket.listen(5)

    print("TCP Server\n")
    
        # Inicializa o objeto RSA
    rsa = RSA()
    
    public_key, private_key = rsa.generateKey()
    
    print(str(public_key))
    print(str(private_key))
    
    while True:

	    # Aceita a conexão do cliente
	    connectionSocket, addr = serverSocket.accept()
	    
	    connectionSocket.sendall(str(public_key).encode())

	    # Recebe a mensagem criptografada do cliente
	    encrypted_message_data = connectionSocket.recv(4096)
	    encrypted_message = eval(encrypted_message_data.decode())

	    # Decifra a mensagem com a chave privada do servidor
	    decrypted_message = rsa.decrypt(encrypted_message,private_key)

	    print("Received From Client:", decrypted_message)

	    # Fecha a conexão com o cliente
	    connectionSocket.close()

if __name__ == "__main__":
    main()
