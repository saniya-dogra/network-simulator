from devices.end_device import EndDevice
from devices.hub import Hub
from devices.switch import Switch
from devices.bridge import Bridge
from layers.physical import Connection
from utils.packet import Packet

from protocols.error_control import add_parity, check_parity
from protocols.flow_control import stop_and_wait
from protocols.access_control import csma_cd


# ================================
# TEST 1: DIRECT CONNECTION
# ================================
print("\n========== TEST 1: DIRECT CONNECTION ==========")

A = EndDevice("A")
B = EndDevice("B")

conn = Connection()
A.connect(conn)
B.connect(conn)

data = add_parity("Hello B")
packet = Packet("A", "B", data)

A.send(packet)

if check_parity(data):
    print("No error in transmission")


# ================================
# ERROR CONTROL DEMO
# ================================
print("\n--- ERROR CONTROL TEST ---")

data = add_parity("Hello")
print("Original:", data)

# simulate error
corrupted = data[:-1] + ('1' if data[-1] == '0' else '0')
print("Corrupted:", corrupted)

if check_parity(corrupted):
    print("No error")
else:
    print("Error detected!")


# ================================
# TEST 2: HUB
# ================================
print("\n========== TEST 2: HUB ==========")

hub = Hub("Hub1")
devices = [EndDevice(f"D{i}") for i in range(5)]           #creates D0, D1, D2, D3, D4

for d in devices:
    hub.connect(d)                                         #all devices connected to hub

packet = Packet("D0", "D3", "Hello via Hub")               #D0 sends message to D3
devices[0].send(packet)


# ================================
# TEST 3: SWITCH
# ================================
print("\n========== TEST 3: SWITCH ==========")

switch = Switch("Switch1")
devices = [EndDevice(f"S{i}") for i in range(5)]

for d in devices:
    switch.connect(d)

packet = Packet("S0", "S4", "Hello via Switch")

# FIX: Ensure flow control always runs
if csma_cd():
    stop_and_wait(devices[0], packet)
else:
    print("Retrying transmission...")
    stop_and_wait(devices[0], packet)


# ================================
# TEST 4: COMPLEX NETWORK
# ================================
print("\n========== TEST 4: COMPLEX NETWORK ==========")

hub1 = Hub("Hub1")
hub2 = Hub("Hub2")
switch = Switch("Switch2")

devices1 = [EndDevice(f"A{i}") for i in range(5)]
devices2 = [EndDevice(f"B{i}") for i in range(5)]

for d in devices1:
    hub1.connect(d)
    switch.connect(d)

for d in devices2:
    hub2.connect(d)
    switch.connect(d)

packet = Packet("A0", "B3", "Cross Network Message")

switch.receive(packet, devices1[0])


# ================================
# TEST 5: BRIDGE
# ================================
print("\n========== TEST 5: BRIDGE ==========")

bridge = Bridge("Bridge1")

d1 = EndDevice("X1")
d2 = EndDevice("X2")

bridge.connect(d1)
bridge.connect(d2)

packet = Packet("X1", "X2", "Hello via Bridge")
bridge.forward(packet)


# ================================
# DOMAIN CALCULATION
# ================================
print("\n========== DOMAIN CALCULATION ==========")

print("Broadcast Domains: 1")
print("Collision Domains:", len(devices1) + len(devices2))

print("\nExplanation:")
print("Each switch port = 1 collision domain")
print("Hub = single collision domain")
print("Entire network = 1 broadcast domain")