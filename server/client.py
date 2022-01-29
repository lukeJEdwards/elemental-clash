import socket
from server.server import PORT

__all__ = ["networkClient"]


class networkClient:
    def __init__(self):
        self.client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host: str = "localhost"
        self.port: int = PORT
        self.id = self.connect()

    def get_address(self) -> tuple[str, int]:
        return (self.host, self.port)

    def connect(self):
        self.client.connect(self.get_address())
        return self.client.recv(2048).decode()

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)
