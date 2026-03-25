from devices.end_device import EndDevice
from devices.hub import Hub
from devices.switch import Switch
from devices.bridge import Bridge
from layers.physical import Connection
from utils.packet import Packet

from protocols.error_control import add_parity, check_parity
from protocols.flow_control import stop_and_wait, go_back_n
from protocols.access_control import csma_cd


def print_header(title):
    print(f"\n========== {title} ==========")


def test_physical_direct_connection():
    print_header("TEST 1: DIRECT CONNECTION")

    a = EndDevice("A")
    b = EndDevice("B")

    conn = Connection()
    a.connect(conn)
    b.connect(conn)

    data = add_parity("Hello B")
    packet = Packet("A", "B", data)
    a.send(packet)

    print("Parity check:", "PASS" if check_parity(data) else "FAIL")


def test_physical_hub_star():
    print_header("TEST 2: HUB STAR TOPOLOGY")

    hub = Hub("Hub1")
    devices = [EndDevice(f"D{i}") for i in range(5)]

    for d in devices:
        hub.connect(d)

    packet = Packet("D0", "D3", "Hello via Hub")
    devices[0].send(packet)


def test_datalink_switch_with_protocols():
    print_header("TEST 3: SWITCH + ACCESS + FLOW CONTROL")

    switch = Switch("Switch1")
    devices = [EndDevice(f"S{i}") for i in range(5)]

    for d in devices:
        switch.connect(d)

    # Access control retry loop.
    retries = 0
    while not csma_cd() and retries < 5:
        retries += 1
        print(f"Retry attempt {retries}")

    # Stop-and-wait demonstration.
    packet = Packet("S0", "S4", "Hello via Switch")
    stop_and_wait(devices[0], packet)

    # Sliding-window demonstration (Go-Back-N).
    frames = [Packet("S1", "S3", f"Frame-{i}") for i in range(1, 6)]
    go_back_n(devices[1], frames, window_size=3, fail_once_index=2)

    print("\nDomain Report (Switch + 5 end devices)")
    print("Broadcast Domains: 1")
    print("Collision Domains: 5")


def test_datalink_two_hubs_connected_by_switch():
    print_header("TEST 4: TWO STAR TOPOLOGIES CONNECTED VIA SWITCH")

    hub1 = Hub("Hub1")
    hub2 = Hub("Hub2")
    core_switch = Switch("Switch2")

    hub1.connect_uplink(core_switch)
    hub2.connect_uplink(core_switch)

    devices1 = [EndDevice(f"A{i}") for i in range(5)]
    devices2 = [EndDevice(f"B{i}") for i in range(5)]

    for d in devices1:
        hub1.connect(d)

    for d in devices2:
        hub2.connect(d)

    packet = Packet("A0", "B3", "Cross Network Message")
    devices1[0].send(packet)

    print("\nDomain Report (2 hubs + 1 switch)")
    print("Broadcast Domains: 1")
    print("Collision Domains: 3")
    print("Reason: each hub contributes 1 collision domain, plus 1 switch link between hubs")


def test_bridge_minimum_deliverable():
    print_header("TEST 5: BRIDGE")

    bridge = Bridge("Bridge1")
    d1 = EndDevice("X1")
    d2 = EndDevice("X2")

    bridge.connect(d1)
    bridge.connect(d2)

    packet = Packet("X1", "X2", "Hello via Bridge")
    bridge.forward(packet)


def test_error_control_demo():
    print_header("ERROR CONTROL DEMO")

    data = add_parity("Hello")
    print("Original:", data)

    corrupted = data[:-1] + ("1" if data[-1] == "0" else "0")
    print("Corrupted:", corrupted)
    print("Result:", "No error" if check_parity(corrupted) else "Error detected")


if __name__ == "__main__":
    test_physical_direct_connection()
    test_error_control_demo()
    test_physical_hub_star()
    test_datalink_switch_with_protocols()
    test_datalink_two_hubs_connected_by_switch()
    test_bridge_minimum_deliverable()