import socket
from rsa import RSA

def main():
    # Endereço e porta do servidor
    server_address = ('192.168.15.19', 1300)

    # Cria o socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect(server_address)

    # Inicializa o objeto RSA
    rsa = RSA()

    public_key_data = client_socket.recv(4096)
    public_key = eval(public_key_data.decode())

    # Recebe a mensagem do usuário
    #message = input("Mensagem:")
    message = 'The information security is of significant importance to ensure the privacy of communications'

    # Criptografa a mensagem com a chave pública do servidor
    encrypted_message = rsa.encrypt(message, public_key)

    # Envia a mensagem criptografada para o servidor
    client_socket.sendall(str(encrypted_message).encode())

    # Fecha a conexão com o servidor
    client_socket.close()

if __name__ == "__main__":
    main()
