class PortManager:

    def __init__(self):

        self.well_known_ports = {
            "HTTP": 80,
            "FTP": 21,
            "TELNET": 23,
            "DNS": 53
        }

        self.ephemeral_port = 49152

    def get_well_known_port(self, service):

        return self.well_known_ports.get(service)

    def assign_ephemeral_port(self):

        port = self.ephemeral_port

        self.ephemeral_port += 1

        return port