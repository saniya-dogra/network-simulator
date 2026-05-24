class PortManager:

    def __init__(self):

        self.well_known_ports = {
            "HTTP": 80,
            "FTP": 21,
            "TELNET": 23,
            "DNS": 53
        }

        self.ephemeral_port = 49152    # dynamic port range(49152-65535)

    def get_well_known_port(self, service):     #takes dest port value

        return self.well_known_ports.get(service)

    def assign_ephemeral_port(self):          #Every time a client process wants to start a new connection, the OS picks
                                              #the next available ephemeral port

        port = self.ephemeral_port

        self.ephemeral_port += 1

        return port