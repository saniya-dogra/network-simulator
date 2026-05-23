from transport_layer.port_manager import PortManager
from transport_layer.tcp_segment import TCPSegment
from transport_layer.udp_segment import UDPSegment
from transport_layer.process_communication import ProcessCommunication
from transport_layer.go_back_n import GoBackN
from transport_layer.selective_repeat import SelectiveRepeat
from transport_layer.congestion_control import CongestionControl
from transport_layer.socket_simulator import SocketSimulator
from application_layer.ftp_service import FTPService
from application_layer.telnet_service import TelnetService
from application_layer.http_service import HTTPService
from application_layer.dns_service import DNSService
from application_layer.application_manager import ApplicationManager


def full_stack_demo():

    from physical_layer.end_device import EndDevice
    from physical_layer.topology import connect
    from datalink_layer.frame import Frame
    from network_layer.ip_packet import IPPacket
    from transport_layer.tcp_segment import TCPSegment
    from application_layer.http_service import HTTPService

    print("\n========== FULL PROTOCOL STACK DEMO ==========")
    print("Simulating: Browser on PC1 requesting a webpage from WebServer")

    # Step 1 - Application Layer
    print("\n[APPLICATION LAYER] Browser generates HTTP GET request")
    app_data = "GET /index.html HTTP/1.1"
    print(f"  Data : {app_data}")

    # Step 2 - Transport Layer
    print("\n[TRANSPORT LAYER] Wrapping in TCP Segment")
    tcp = TCPSegment(49152, 80, 1, app_data)
    tcp.show()

    # Step 3 - Network Layer
    print("\n[NETWORK LAYER] Wrapping in IP Packet")
    packet = IPPacket("192.168.1.10", "93.184.216.34", str(tcp.__dict__))
    packet.show_packet()

    # Step 4 - Data Link Layer
    print("\n[DATA LINK LAYER] Wrapping in Ethernet Frame")
    frame = Frame("AA:BB:CC:DD", "EE:FF:00:11", str(packet.__dict__))
    frame.show_frame()

    # Step 5 - Physical Layer
    print("\n[PHYSICAL LAYER] Transmitting bits over the wire")
    pc1 = EndDevice("PC1", "AA:BB:CC:DD")
    server = EndDevice("WebServer", "EE:FF:00:11")
    connect(pc1, server)
    pc1.send_data("Encoded bits of HTTP Frame")

    print("\n--- Frame arrives at WebServer ---")
    print("\n[PHYSICAL LAYER]    Bits received, reconstructing frame")
    print("[DATA LINK LAYER]   Frame extracted, checking MAC address")
    print("[NETWORK LAYER]     Packet extracted, checking IP address")
    print("[TRANSPORT LAYER]   Segment extracted, delivering to port 80 (HTTP)")
    print("[APPLICATION LAYER] HTTP Request received: GET /index.html HTTP/1.1")
    print("\n200 OK - Full stack encapsulation and decapsulation complete")


def transport_application_demo():

    print("\n========== TRANSPORT LAYER ==========")

    # ------------------------------------------------

    print("\nTEST 1 : Port Management")

    ports = PortManager()

    print(
        "HTTP Port :",
        ports.get_well_known_port("HTTP")
    )

    print(
        "FTP Port :",
        ports.get_well_known_port("FTP")
    )

    print(
        "Ephemeral Port :",
        ports.assign_ephemeral_port()
    )

    # ------------------------------------------------

    print("\nTEST 2 : TCP Segment")

    tcp = TCPSegment(
        5000,
        80,
        1,
        "TCP Payload"
    )

    tcp.show()

    # ------------------------------------------------

    print("\nTEST 3 : UDP Segment")

    udp = UDPSegment(
        6000,
        53,
        "UDP Payload"
    )

    udp.show()

    # ------------------------------------------------

    print("\nTEST 4 : Process Communication")

    process = ProcessCommunication()

    process.communicate(
        "Browser",
        "HTTP",
        "HTTP Request"
    )

    # ------------------------------------------------

    print("\nTEST 5 : Go Back N")

    gbn = GoBackN(window_size=4, total_frames=8)

    gbn.send_frames(lost_frame=2)

    # ------------------------------------------------

    print("\nTEST 6 : Selective Repeat")

    sr = SelectiveRepeat(window_size=4, total_frames=8)

    sr.send_frames(lost_frames=[3, 6])

    # ------------------------------------------------

    print("\nTEST 7 : Congestion Control")

    congestion = CongestionControl()

    congestion.simulate()

    # ------------------------------------------------

    print("\nTEST 8 : Socket Simulation")

    socket = SocketSimulator()

    socket.create_socket()

    socket.bind(8080)

    socket.listen()

    socket.accept("Client-PC1")

    socket.send("Hello from server")

    socket.close()

    # ------------------------------------------------

    print("\n========== APPLICATION LAYER ==========")

    app_manager = ApplicationManager()

    # ------------------------------------------------

    print("\nTEST 9 : FTP Service")

    app_manager.launch("FTP")

    ftp = FTPService()

    ftp.transfer_file()

    # ------------------------------------------------

    print("\nTEST 10 : Telnet Service")

    app_manager.launch("TELNET")

    telnet = TelnetService()

    telnet.connect()

    # ------------------------------------------------

    print("\nTEST 11 : HTTP Service")

    app_manager.launch("HTTP")

    http = HTTPService()

    http.request_page()

    # ------------------------------------------------

    print("\nTEST 12 : DNS Service")

    app_manager.launch("DNS")

    dns = DNSService()

    dns.resolve()

    # ------------------------------------------------

    full_stack_demo()

    # ------------------------------------------------

    print("\nFULL PROTOCOL STACK SUCCESSFULLY IMPLEMENTED")