class SocketSimulator:

    def __init__(self):
        self.bound_port = None
        self.is_connected = False

    def create_socket(self):
        print("\nSOCKET SIMULATION")
        print("Socket Created (TCP, STREAM type)")

    def bind(self, port):
        self.bound_port = port
        print(f"Socket Bound to Port {port}")

    def listen(self):
        if self.bound_port is None:
            print("Error: Socket not bound to any port")        #incoming connection request
            return
        print(f"Socket Listening on Port {self.bound_port} ...")

    def accept(self, client_name):
        print(f"Connection Accepted from {client_name}")         #Blocks until client connects,creates new socket
        self.is_connected = True

    def send(self, data):
        if not self.is_connected:
            print("Error: Not connected")
            return
        print(f"Socket Sending : {data}")

    def close(self):
        print(f"Socket on Port {self.bound_port} Closed")
        self.is_connected = False
        self.bound_port = None