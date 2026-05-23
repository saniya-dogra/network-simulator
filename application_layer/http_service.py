from transport_layer.port_manager import PortManager
from transport_layer.tcp_segment import TCPSegment

class HTTPService:

    def request_page(self, url="/index.html", server_ip="93.184.216.34"):

        print("\nHTTP SERVICE")

        port_manager = PortManager()
        src_port = port_manager.assign_ephemeral_port()
        dest_port = port_manager.get_well_known_port("HTTP")  # 80

        print(f"Client Source Port      : {src_port}")
        print(f"Server Destination Port : {dest_port} (HTTP)")
        print(f"Sending HTTP Request    : GET {url} HTTP/1.1")

        # Encapsulate HTTP request into a TCP segment
        segment = TCPSegment(src_port, dest_port, 1, f"GET {url} HTTP/1.1")
        segment.show()

        print(f"\nServer at {server_ip} processing request...")
        print(f"HTTP Response : 200 OK")
        print(f"Response Body : <html><body>Welcome to {url}</body></html>")

        # Encapsulate response into a TCP segment going back
        response_segment = TCPSegment(dest_port, src_port, 2, "200 OK - HTML Content")
        response_segment.show()