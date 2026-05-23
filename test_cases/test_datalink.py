from physical_layer.end_device import EndDevice
from physical_layer.hub import Hub
from physical_layer.topology import connect

from datalink_layer.switch import Switch
from datalink_layer.bridge import Bridge
from datalink_layer.frame import Frame
from datalink_layer.error_control import ParityCheck
from datalink_layer.mac_protocol import CSMACD
from datalink_layer.flow_control import StopAndWait


def datalink_demo():

    print("\nTEST 1 : Switch Communication")

    switch = Switch("Switch1")

    d1 = EndDevice("PC1", "AA")
    d2 = EndDevice("PC2", "BB")
    d3 = EndDevice("PC3", "CC")
    d4 = EndDevice("PC4", "DD")
    d5 = EndDevice("PC5", "EE")

    switch.connect_device(d1)
    switch.connect_device(d2)
    switch.connect_device(d3)
    switch.connect_device(d4)
    switch.connect_device(d5)

    switch.send_frame(d1, "BB", "Hello PC2")

    switch.show_mac_table()

    print("\n--------------------------------")

    print("\nTEST 2 : Bridge")

    bridge = Bridge("Bridge1")

    bridge.forward("Bridge Data")

    print("\n--------------------------------")

    print("\nTEST 3 : Error Control")

    parity = ParityCheck()

    bits = "1010101"

    parity_bit = parity.generate_parity(bits)

    print("Data Bits:", bits)

    print("Parity Bit:", parity_bit)

    print(parity.check_error(bits, parity_bit))

    print("\n--------------------------------")

    print("\nTEST 4 : Access Control Protocol")

    protocol = CSMACD()

    protocol.transmit()

    print("\n--------------------------------")

    print("\nTEST 5 : Flow Control")

    frame = Frame("AA", "BB", "Hello")

    flow = StopAndWait()

    flow.send(frame)

    print("\n--------------------------------")

    print("\nTEST 6 : Single Switch Statistics")

    print("Broadcast Domains = 1")

    print("Collision Domains = 5")

    print("\n--------------------------------")

    print("\nTEST 7 : Two Star Topologies Connected Using Switch")

    # CREATE MAIN SWITCH

    core_switch = Switch("CoreSwitch")

    # CREATE HUBS

    hub1 = Hub("Hub1")
    hub2 = Hub("Hub2")

    # CREATE DEVICE LISTS

    devices_hub1 = []
    devices_hub2 = []

    # CREATE 5 DEVICES FOR HUB1

    for i in range(1, 6):

        device = EndDevice(
            f"H1_PC{i}",
            f"H1_MAC{i}"
        )

        devices_hub1.append(device)

        connect(device, hub1)

    # CREATE 5 DEVICES FOR HUB2

    for i in range(1, 6):

        device = EndDevice(
            f"H2_PC{i}",
            f"H2_MAC{i}"
        )

        devices_hub2.append(device)

        connect(device, hub2)

    # HUB CONNECTOR CLASS

    class HubConnector:

        def __init__(self, name, mac):

            self.name = name
            self.mac = mac

        def receive_data(self, data):

            print(f"{self.name} received data: {data}")

    # CREATE CONNECTORS

    hub1_connector = HubConnector(
        "Hub1_Connector",
        "HUB1"
    )

    hub2_connector = HubConnector(
        "Hub2_Connector",
        "HUB2"
    )

    # CONNECT HUBS TO SWITCH

    core_switch.connect_device(hub1_connector)
    core_switch.connect_device(hub2_connector)

    print("\nNetwork Topology")

    print(r"""
            H1_PC1  H1_PC2  H1_PC3  H1_PC4  H1_PC5
                 \      |      |      |      /
                          Hub1
                            |
                      CoreSwitch
                            |
                          Hub2
                 /      |      |      |      \\
            H2_PC1  H2_PC2  H2_PC3  H2_PC4  H2_PC5
    """)

    print("\nCommunication Inside Hub1")

    devices_hub1[0].send_data(
        "Hello from Hub1"
    )

    print("\nCommunication Inside Hub2")

    devices_hub2[0].send_data(
        "Hello from Hub2"
    )

    print("\nCommunication Across Switch")

    core_switch.send_frame(
        hub1_connector,
        "HUB2",
        "Message from Hub1 Network to Hub2 Network"
    )

    print("\nFinal Network Statistics")

    print("Broadcast Domains = 1")

    print("Collision Domains = 3")

    print("\nAll 10 Devices Successfully Connected")