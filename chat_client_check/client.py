import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5378
HOST_PORT = (SERVER_HOST, SERVER_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Attempting to connect to server at {}:{}".format(SERVER_HOST, SERVER_PORT))
sock.connect(HOST_PORT)

print('Welcome to Chat Client. Enter you login:')
# Please put your code in this file
# going to implement each requirement modularly 
# RA1: The client must ask the user for a username and attempt to log them in.
def main():

