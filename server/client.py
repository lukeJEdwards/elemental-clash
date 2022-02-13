from dataclasses import dataclass
from socket import socket, AF_INET, SOCK_STREAM, error

from server.server import IP, PORT
from systems.stateMachine import GAME_STATE


@dataclass
class Client:
    client: socket = socket(AF_INET, SOCK_STREAM)

    def connect(self, ip: str = IP) -> bool:
        try:
            self.client.connect((ip, PORT))
            GAME_STATE.player.load(self.client.recv(2048))
            return True
        except error:
            return False

    def disconnect(self) -> None:
        self.client.close()
        self.client = socket(AF_INET, SOCK_STREAM)

    def send(self) -> None:
        try:
            self.client.send(GAME_STATE.player.pickle())
            GAME_STATE.opponent.load(self.client.recv(2048))
        except error as e:
            print(str(e))
            self.client.close()


CLIENT: Client = Client()
