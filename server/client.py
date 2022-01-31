import socket
from typing import Optional
from server.server import PORT, IP

__all__ = ["CLIENT"]


class networkClient:
    def __init__(self):
        self.client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_address(self, host: str) -> tuple[str, int]:
        return (host, PORT)

    def connect(self, host: Optional[str] = IP) -> str | None:
        try:
            self.client.connect(self.get_address(host))
            self.id = self.client.recv(2048).decode()
        except socket.error:
            return f"{host}:{PORT} failed"

    def disconnect(self):
        self.client.close()

    def send(self, data) -> str:
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            self.client.close()


CLIENT: networkClient = networkClient()
