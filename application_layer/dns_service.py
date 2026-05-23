from transport_layer.port_manager import PortManager
from transport_layer.udp_segment import UDPSegment

class DNSService:

    def __init__(self):
        self.dns_table = {
            "www.example.com": "93.184.216.34",
            "www.google.com": "142.250.190.4",
            "www.github.com": "140.82.121.4"
        }

    def resolve(self, hostname="www.example.com"):

        print("\nDNS SERVICE")

        port_manager = PortManager()
        src_port = port_manager.assign_ephemeral_port()
        dest_port = port_manager.get_well_known_port("DNS")  # 53

        print(f"DNS Query for   : {hostname}")
        print(f"Source Port     : {src_port}")
        print(f"Destination Port: {dest_port} (DNS)")

        # DNS uses UDP — encapsulate query in UDP segment
        query_segment = UDPSegment(src_port, dest_port, f"DNS Query: {hostname}")
        query_segment.show()

        # Look up the hostname
        resolved_ip = self.dns_table.get(hostname, "NOT FOUND")
        print(f"\nDNS Response : {hostname} -> {resolved_ip}")

        # DNS response also in UDP segment
        response_segment = UDPSegment(dest_port, src_port, f"DNS Response: {resolved_ip}")
        response_segment.show()