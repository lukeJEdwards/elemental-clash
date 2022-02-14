import socket
import pickle

from dataclasses import dataclass

from server.player import Player
from utils.constants import IP, PORT, BUFFER


@dataclass
class Client:
    client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip: str = IP) -> list[Player]:
        try:
            self.client.connect((ip, PORT))
            return pickle.loads(self.client.recv(2048))
        except socket.error:
            pass

    def disconnect(self) -> None:
        self.client.close()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, player: Player) -> Player:
        try:
            self.client.send(pickle.dumps(player))
            data: bytes = self.client.recv(BUFFER)

            if data:
                return pickle.loads(data)

        except socket.error as e:
            print(str(e))
            self.client.close()


CLIENT: Client = Client()
