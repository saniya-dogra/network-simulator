class AdvancedPacket:

    def __init__(
        self,
        source_ip,
        destination_ip,
        ttl,
        protocol,
        data
    ):

        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.ttl = ttl
        self.protocol = protocol
        self.data = data

    def show(self):

        print("\nADVANCED IPv4 DATAGRAM")

        print("Source IP :", self.source_ip)

        print("Destination IP :", self.destination_ip)

        print("TTL :", self.ttl)

        print("Protocol :", self.protocol)

        print("Payload :", self.data)