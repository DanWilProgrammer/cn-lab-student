import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5378
HOST_PORT = (SERVER_HOST, SERVER_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Attempting to connect to server at {}:{}".format(SERVER_HOST, SERVER_PORT))
sock.bind(HOST_PORT)

print('Welcome to Chat Client. Enter you login:')
# Please put your code in this file
# going to implement each requirement modularly 

# RA1: The client must ask the user for a username and attempt to log them in.
def username_login():
    try:
        username = input()
        sock.connect(HOST_PORT)
        string_bytes = "Sockets are great!".encode("utf-8")
        bytes_len = len(string_bytes)
        num_bytes_to_send = bytes_len
        while num_bytes_to_send > 0:
            # Sometimes, the operating system cannot send everything immediately.
            # For example, the sending buffer may be full.
            # send returns the number of bytes that were sent.
            num_bytes_to_send -= sock.send(string_bytes[bytes_len-num_bytes_to_send:])
        data = sock.recv(4096)
        if not data:
            print("Socket is closed.")
        else:
            print(f"Read data from socket: {data}")
        if data == "IN-USE\n":
            #RA2: The client must ask the user for a new username if the provided one is already in use, with an informative message.
            print("Username is already in use. Please try again with a unique username.")
            username_login()
        elif data == "BUSY\n":
            #RA3: The client must inform the user if the server is full and exit gracefully.
            print("Server is busy (max number of clients on server). Please try again later.")
            username_login()
        elif data == "SUCCESS\n":
            pass
    except Exception as e:
        pass
    finally:
        sock.close()
