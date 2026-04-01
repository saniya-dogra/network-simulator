from core import SimulatorCore, Frame, Device, Hub, Switch
from layers.physical import PhysicalLayer
from layers.datalink import DataLinkLayer
from protocols.protocols.protocol import CSMACD, GoBackN, ChecksumProtocol


def parse_list(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def build_topology(sim, spec):
    """
    New CLI format:
    p2p:A-B
    star:Hub1>A,B,C
    switch:SW1>A,B,C,D
    hybrid:CoreSW|Hub1:H1_PC1,H1_PC2,H1_PC3,H1_PC4,H1_PC5|Hub2:H2_PC1,H2_PC2,H2_PC3,H2_PC4,H2_PC5
    """
    if ":" not in spec:
        raise ValueError("Invalid topology format. Missing ':'")

    topology, payload = spec.split(":", 1)
    topology = topology.strip().lower()
    payload = payload.strip()

    if topology == "p2p":
        if "-" not in payload:
            raise ValueError("p2p format must be p2p:DeviceA-DeviceB")
        left, right = payload.split("-", 1)
        name_a = left.strip()
        name_b = right.strip()
        if not name_a or not name_b:
            raise ValueError("Both device names are required for p2p")

        dev_a = Device(name_a)
        dev_b = Device(name_b)
        sim.add_device(dev_a)
        sim.add_device(dev_b)
        dev_a.connect(dev_b)
        return

    if topology in ("star", "switch"):
        if ">" not in payload:
            raise ValueError(f"{topology} format must be {topology}:Center>Dev1,Dev2")
        center_name, dev_csv = payload.split(">", 1)
        center_name = center_name.strip()
        device_names = parse_list(dev_csv)
        if not center_name or not device_names:
            raise ValueError("Center and at least one end device are required")

        center = Hub(center_name) if topology == "star" else Switch(center_name)
        sim.add_device(center)

        for name in device_names:
            dev = Device(name)
            sim.add_device(dev)
            dev.connect(center)
        return

    if topology == "hybrid":
        parts = [p.strip() for p in payload.split("|") if p.strip()]
        if len(parts) != 3:
            raise ValueError("hybrid format needs 3 sections: CoreSW|Hub1:list|Hub2:list")

        switch_name = parts[0]
        hub_defs = parts[1:]

        main_switch = Switch(switch_name)
        sim.add_device(main_switch)

        for hub_def in hub_defs:
            if ":" not in hub_def:
                raise ValueError("Each hub section must be HubName:Dev1,Dev2,...")
            hub_name, dev_csv = hub_def.split(":", 1)
            hub_name = hub_name.strip()
            dev_names = parse_list(dev_csv)
            if not hub_name or not dev_names:
                raise ValueError("Hub name and at least one connected device are required")

            hub = Hub(hub_name)
            sim.add_device(hub)
            main_switch.connect(hub)

            for dev_name in dev_names:
                dev = Device(dev_name)
                sim.add_device(dev)
                dev.connect(hub)
        return

    raise ValueError(f"Unsupported topology type: {topology}")


def parse_transmission(spec):
    """
    New message format:
    Sender->Receiver:Message text
    """
    if "->" not in spec or ":" not in spec:
        raise ValueError("Transmission format must be Sender->Receiver:Message")

    route, message = spec.split(":", 1)
    sender_name, receiver_name = route.split("->", 1)

    sender_name = sender_name.strip()
    receiver_name = receiver_name.strip()
    message = message.strip()

    if not sender_name or not receiver_name or not message:
        raise ValueError("Sender, receiver and message are all required")

    return sender_name, receiver_name, message

def main():
    sim = SimulatorCore()
    phy = PhysicalLayer()
    dll = DataLinkLayer(phy)
    csma = CSMACD()
    gbn = GoBackN(phy, dll)
    checksum = ChecksumProtocol()

    dll.set_access_protocol(csma)
    dll.set_flow_control_protocol(gbn)

    print("--- Network Simulator (Command CLI) ---")
    print("\nTopology input examples:")
    print("  p2p:A-B")
    print("  star:Hub1>A,B,C")
    print("  switch:SW1>A,B,C,D")
    print("  hybrid:CoreSW|Hub1:H1_PC1,H1_PC2,H1_PC3,H1_PC4,H1_PC5|Hub2:H2_PC1,H2_PC2,H2_PC3,H2_PC4,H2_PC5")

    topology_spec = input("\nEnter topology command: ")
    try:
        build_topology(sim, topology_spec)
    except ValueError as exc:
        print(f"Invalid topology input: {exc}")
        return

    print("\n--- Available Devices ---")
    for name in sim.all_devices:
        print(f"- {name}")

    print("\nTransmission input format:")
    print("  Sender->Receiver:Message")

    transfer_spec = input("Enter transmission command: ")
    try:
        sender_name, receiver_name, message = parse_transmission(transfer_spec)
    except ValueError as exc:
        print(f"Invalid transmission input: {exc}")
        return

    sender = sim.all_devices.get(sender_name)
    receiver = sim.all_devices.get(receiver_name)

    if sender and receiver:
        dll.send(sender, receiver, message)
        sim.get_stats()
    else:
        print("Device not available")

if __name__ == "__main__":
    main()