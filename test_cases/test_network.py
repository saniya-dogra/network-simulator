from network_layer.ipv4 import IPv4Address
from network_layer.ipv6 import IPv6Address
from network_layer.classful_addressing import ClassfulAddressing

from network_layer.ip_packet import IPPacket
from network_layer.advanced_packet import AdvancedPacket

from network_layer.arp import ARPTable

from network_layer.router import Router
from network_layer.router_interface import RouterInterface

from network_layer.static_routing import StaticRouting

from network_layer.rip_protocol import RIPProtocol
from network_layer.ospf_protocol import OSPFProtocol
from network_layer.bgp_protocol import BGPProtocol
from network_layer.eigrp_protocol import EIGRPProtocol

from network_layer.subnetting import Subnetting
from network_layer.aggregation import AddressAggregation


def network_demo():

    print("\n========== NETWORK LAYER ==========")

    # ------------------------------------------------

    print("\nTEST 1 : IPv4 Addressing")

    ip1 = IPv4Address(
        "192.168.1.10",
        24
    )

    ip1.show()

    # ------------------------------------------------

    print("\nTEST 2 : Classful Addressing")

    classful = ClassfulAddressing()

    print(
        "10.0.0.1 ->",
        classful.identify_class("10.0.0.1")
    )

    print(
        "172.16.0.1 ->",
        classful.identify_class("172.16.0.1")
    )

    print(
        "192.168.1.1 ->",
        classful.identify_class("192.168.1.1")
    )

    # ------------------------------------------------

    print("\nTEST 3 : IPv6 Addressing")

    ipv6 = IPv6Address(
        "2001:0db8:85a3::8a2e:0370:7334"
    )

    ipv6.show()

    # ------------------------------------------------

    print("\nTEST 4 : ARP Protocol")

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

    # ------------------------------------------------

    print("\nTEST 5 : Basic IP Packet")

    packet = IPPacket(
        "192.168.1.10",
        "192.168.2.20",
        "Hello Network Layer"
    )

    packet.show_packet()

    # ------------------------------------------------

    print("\nTEST 6 : Advanced IPv4 Datagram")

    advanced_packet = AdvancedPacket(
        "192.168.1.10",
        "192.168.2.20",
        64,
        "TCP",
        "Advanced Datagram Payload"
    )

    advanced_packet.show()

    # ------------------------------------------------

    print("\nTEST 7 : Router Configuration")

    router = Router("Router1")

    interface1 = RouterInterface(
        "Gig0/0",
        "192.168.1.1/24"
    )

    interface2 = RouterInterface(
        "Gig0/1",
        "192.168.2.1/24"
    )

    router.add_interface(interface1)

    router.add_interface(interface2)

    router.show_interfaces()

    # ------------------------------------------------

    print("\nTEST 8 : Static Routing")

    router.add_route(
        "192.168.1.0",
        24,
        "Gig0/0"
    )

    router.add_route(
        "192.168.2.0",
        24,
        "Gig0/1"
    )

    router.routing_table.show_routes()

    router.route_packet(advanced_packet)

    static = StaticRouting()

    static.configure()

    # ------------------------------------------------

    print("\nTEST 9 : RIP Protocol")

    rip = RIPProtocol()

    rip.start()

    # ------------------------------------------------

    print("\nTEST 10 : OSPF Protocol")

    ospf = OSPFProtocol()

    ospf.start()

    # ------------------------------------------------

    print("\nTEST 11 : BGP Protocol")

    bgp = BGPProtocol()

    bgp.start()

    # ------------------------------------------------

    print("\nTEST 12 : EIGRP Protocol")

    eigrp = EIGRPProtocol()

    eigrp.start()

    # ------------------------------------------------

    print("\nTEST 13 : Subnetting")

    subnet = Subnetting()

    subnet.show_network(
        "192.168.10.0",
        24
    )

    # ------------------------------------------------

    print("\nTEST 14 : Address Aggregation")

    aggregation = AddressAggregation()

    aggregation.summarize()

    # ------------------------------------------------

    print("\nALL NETWORK LAYER FEATURES IMPLEMENTED")