from transport_layer.port_manager import PortManager
from transport_layer.tcp_segment import TCPSegment

class ProcessCommunication:

    def __init__(self):
        self.port_manager = PortManager()

    def communicate(self, source_process, destination_process, data):

        print("\nPROCESS TO PROCESS COMMUNICATION")

        # Assign a source ephemeral port to the sending process
        src_port = self.port_manager.assign_ephemeral_port()

        # Look up well-known destination port, or assign ephemeral
        dest_port = self.port_manager.get_well_known_port(destination_process.upper())
        if dest_port is None:
            dest_port = self.port_manager.assign_ephemeral_port()

        print(f"Source Process      : {source_process}  (Port {src_port})")
        print(f"Destination Process : {destination_process}  (Port {dest_port})")

        # Wrap data in a TCP segment
        segment = TCPSegment(src_port, dest_port, 1, data)
        segment.show()

        print(f"Data '{data}' delivered from {source_process}:{src_port} -> {destination_process}:{dest_port}")