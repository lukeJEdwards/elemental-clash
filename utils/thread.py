import threading


class Thread(threading.Thread):
    def __init__(self, target, *args):
        super().__init__(target=target, args=args)
        self.start()
