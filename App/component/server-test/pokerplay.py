import socket


class PokerClient:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_host, self.server_port))

    def play(self):
        # Implement player actions and communication with the server here
        pass


if __name__ == "__main__":
    client = PokerClient('localhost', 8888)
    client.play()
