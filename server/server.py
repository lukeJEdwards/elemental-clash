import socket
from _thread import start_new_thread

__all__ = ["SERVER", "PORT"]


def get_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


PORT = 5555
IP = get_ip()


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = IP
        self.PORT = PORT
        self.running = True
        self.current_id = "0"

    def run_server(self):
        try:
            self.server.bind((self.SERVER, self.PORT))
        except socket.error as e:
            print(str(e))

        self.server.listen(2)
        print("waiting for a connection...")

        while self.running:
            conn, addr = self.server.accept()
            print("Connection accepted: ", addr)
            start_new_thread(self.threaded_client, (conn,))

    def threaded_client(self, conn: socket.socket):
        conn.send(str.encode(f"{self.current_id}, {self.SERVER}"))
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


SERVER: Server = Server()
