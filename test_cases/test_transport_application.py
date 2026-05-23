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
        "Web Server",
        "HTTP Request"
    )

    # ------------------------------------------------

    print("\nTEST 5 : Go Back N")

    gbn = GoBackN()

    gbn.send_frames()

    # ------------------------------------------------

    print("\nTEST 6 : Selective Repeat")

    sr = SelectiveRepeat()

    sr.send_frames()

    # ------------------------------------------------

    print("\nTEST 7 : Congestion Control")

    congestion = CongestionControl()

    congestion.simulate()

    # ------------------------------------------------

    print("\nTEST 8 : Socket Simulation")

    socket = SocketSimulator()

    socket.create_socket()

    socket.bind(8080)

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

    print("\nFULL PROTOCOL STACK SUCCESSFULLY IMPLEMENTED")