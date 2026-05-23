from physical_layer.end_device import EndDevice
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

    print("\nBroadcast Domains = 1")

    print("Collision Domains = 5")