import socket
from _thread import *

__all__ = ["Server", "PORT"]
PORT = 5555


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = get_ip()
        self.PORT = PORT
        self.running = True
        self.current_id = "0"
        try:
            self.server.bind((self.SERVER, self.PORT))
        except socket.error as e:
            print(str(e))

        self.server.listen(2)
        print("waiting for a connection...")

    def run_server(self):
        while self.running:
            conn, addr = self.server.accept()
            print("Connection accepted: ", addr)
            start_new_thread(self.threaded_client, (conn,))

    def threaded_client(self, conn: socket.socket):
        conn.send(str.encode(self.current_id))
        self.current_id = "1"
        reply = ""
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode("utf-8")
                if not data:
                    conn.send(str.encode("Goodbye"))
                    break
                else:
                    print("Recieved: " + reply)
            except:
                break

        print("Connection Closed")
        conn.close()
