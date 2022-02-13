import threading
import socket
import pickle

from server.player import Player, playerAuth
from systems.stateMachine import GAME_STATE
from utils.thread import Thread


def get_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


LOCK = threading.Lock()
PORT = 5555
IP = get_ip()


class Server:
    def __init__(self):
        self.server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sockets: dict[playerAuth, socket.socket] = {}

        self.owner: Player = Player(playerAuth.OWNER)
        self.opponent: Player = Player(playerAuth.OPPONENT)

        self.is_owner = True

    def run(self) -> None:

        try:
            self.server.bind((IP, PORT))
        except socket.error as e:
            print(str(e))

        self.server.listen()
        print("waiting for players...")

        while GAME_STATE.server_running:
            conn, address = self.server.accept()
            print(f"Player connected, IP:{address[0]}")
            connetion = Thread(self.client_handler, conn)
            connetion.join()

        print("---Server closed---")
        self.server.close()

    def send_player_info(self, player_auth: playerAuth, player: Player) -> None:
        try:
            self.sockets[player_auth].send(player.pickle())
        except (socket.error, KeyError) as e:
            print(e)
            pass

    def client_handler(self, conn: socket.socket) -> None:
        conn.send(self.owner.pickle() if self.is_owner else self.opponent.pickle())
        self.sockets[playerAuth.OWNER if self.is_owner else playerAuth.OPPONENT] = conn
        self.is_owner = False

        while True:
            try:
                player: dict = pickle.loads(conn.recv(2048))

                if not player:
                    conn.send(str.encode("Goodbye"))
                    break

                if player["auth"] == playerAuth.OWNER:
                    self.owner = player
                else:
                    self.opponent = player

                print("sending player info")
                self.send_player_info(playerAuth.OWNER, self.opponent)
                self.send_player_info(playerAuth.OPPONENT, self.owner)

            except socket.error as e:
                break

        print("Connection Closed")
        conn.close()


SERVER: Server = Server()
