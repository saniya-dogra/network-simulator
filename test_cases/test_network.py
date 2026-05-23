from network_layer.ipv4 import IPv4Address
from network_layer.ip_packet import IPPacket
from network_layer.arp import ARPTable
from network_layer.router import Router
from network_layer.static_routing import StaticRouting
from network_layer.rip_protocol import RIPProtocol
from network_layer.subnetting import Subnetting


def network_demo():

    print("\n========== NETWORK LAYER ==========")

    print("\nTEST 1 : IPv4 Addressing")

    ip1 = IPv4Address(
        "192.168.1.10",
        24
    )

    ip1.show()

    print("\n--------------------------------")

    print("\nTEST 2 : ARP Protocol")

    arp = ARPTable()

    arp.add_entry(
        "192.168.1.10",
        "AA:BB:CC:DD"
    )

    arp.add_entry(
        "192.168.1.20",
        "EE:FF:GG:HH"
    )

    arp.show_table()

    print(
        "\nMAC Address for 192.168.1.20 :",
        arp.get_mac("192.168.1.20")
    )

    print("\n--------------------------------")

    print("\nTEST 3 : IP Packet")

    packet = IPPacket(
        "192.168.1.10",
        "192.168.2.20",
        "Hello Network Layer"
    )

    packet.show_packet()

    print("\n--------------------------------")

    print("\nTEST 4 : Static Routing")

    router = Router("Router1")

    router.add_route(
        "192.168.1.",
        24,
        "Interface1"
    )

    router.add_route(
        "192.168.2.",
        24,
        "Interface2"
    )

    router.routing_table.show_routes()

    router.route_packet(packet)

    static = StaticRouting()

    static.configure()

    print("\n--------------------------------")

    print("\nTEST 5 : RIP Dynamic Routing")

    rip = RIPProtocol()

    rip.start()

    print("\n--------------------------------")

    print("\nTEST 6 : Subnetting")

    subnet = Subnetting()

    subnet.show_network(
        "192.168.10.0",
        24
    )