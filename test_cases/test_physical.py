from physical_layer.end_device import EndDevice
from physical_layer.hub import Hub
from physical_layer.topology import connect
from physical_layer.signal import Signal
from physical_layer.line_coding import LineCoding


def physical_layer_demo():

    print("\nTEST 1 : Direct Connection")

    pc1 = EndDevice("PC1", "AA:11")
    pc2 = EndDevice("PC2", "BB:22")

    connect(pc1, pc2)

    pc1.send_data("Hello PC2")

    print("\n--------------------------------")

    print("\nTEST 2 : Star Topology using Hub")

    hub = Hub("Hub1")

    d1 = EndDevice("D1", "00:01")
    d2 = EndDevice("D2", "00:02")
    d3 = EndDevice("D3", "00:03")
    d4 = EndDevice("D4", "00:04")
    d5 = EndDevice("D5", "00:05")

    connect(d1, hub)
    connect(d2, hub)
    connect(d3, hub)
    connect(d4, hub)
    connect(d5, hub)

    d1.send_data("Message to all devices")

    print("\n--------------------------------")

    print("\nADD-ON FEATURES")

    bits = "101101"

    signal = Signal()
    signal.show_signal(bits)

    coding = LineCoding()

    print("\nNRZ Encoding:")
    print(coding.nrz(bits))

    print("\nManchester Encoding:")
    print(coding.manchester(bits))