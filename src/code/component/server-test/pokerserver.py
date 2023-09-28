import socket
import threading


class PokerServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.players = []

    def start(self):
        self.server_socket.listen()
        print("Server listening on", (self.host, self.port))

        while True:
            client_socket, client_address = self.server_socket.accept()
            print("New connection from", client_address)
            player_thread = threading.Thread(
                target=self.handle_player, args=(client_socket,))
            player_thread.start()

    def handle_player(self, client_socket):
        # Handle communication with a single player here
        pass


if __name__ == "__main__":
    server = PokerServer('localhost', 8888)
    server.start()
