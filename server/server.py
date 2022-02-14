import threading
import socket
import pickle
from _thread import start_new_thread

from server.player import Player
from systems.stateMachine import GAME_STATE
from utils.constants import IP, PORT, BUFFER


class Server:
    def __init__(self):
        self.server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.players: list[Player] = [Player(index=0), Player(index=1)]

    def run(self) -> None:

        try:
            self.server.bind((IP, PORT))
        except socket.error as e:
            print(str(e))

        self.server.listen(2)
        print("waiting for players...")

        while GAME_STATE.server_running:
            conn, address = self.server.accept()
            print(f"Player connected, IP:{address[0]}:{address[1]}")
            start_new_thread(self.client_handler, (conn,))

        print("---Server closed---")
        self.server.close()

    def client_handler(self, conn: socket.socket) -> None:
        conn.send(pickle.dumps(self.players))
        while True:
            try:
                player: Player = pickle.loads(conn.recv(BUFFER))

                if not player:
                    conn.send(str.encode("Goodbye"))
                    break

                self.players[player.index] = player
                conn.send(pickle.dumps(self.players[1 if player.index == 0 else 0]))

            except Exception as e:
                print(e)
                break

        print("Connection Closed")
        conn.close()


SERVER: Server = Server()
