from core import Frame, Hub, Switch, Bridge

class DataLinkLayer:
    def __init__(self, physical_layer):
        self.physical_layer = physical_layer
        self.access_protocol = None
        self.flow_control_protocol = None
        self.sent_frames = 0
        self.received_frames = 0
        self.mac_table = {} 

    def set_access_protocol(self, protocol):
        self.access_protocol = protocol

    def set_flow_control_protocol(self, protocol):
        self.flow_control_protocol = protocol

    def send(self, sender, receiver, message):
        print(f"\n[L2/TX] start: {sender.name} -> {receiver.name} | text='{message}' | chars={len(message)}")
        frames = []
        for idx, char in enumerate(message):
            f = Frame(sender.mac_address, receiver.mac_address, char)
            f.is_ack = False
            # Skipping error_detection for ACKs
            
            self.add_error_detection(f)
            f.payload = f"{f.payload}|{f.error_code}"

            print(f"[L2/TX] frame-{idx}: data='{char}' checksum={f.error_code}")

            frames.append(f)

        connected_device = next((p for p in sender.ports if isinstance(p, (Hub, Switch, Bridge))), None)

        if self.flow_control_protocol and len(frames) > 1 and not frames[0].is_ack:
            target = connected_device if connected_device else receiver
            self.flow_control_protocol.send(sender, target, frames)
            self.sent_frames += len(frames)
            return

        for frame in frames:
            if self.access_protocol and connected_device:
                self.access_protocol.handle_access(sender, connected_device, frame, self.physical_layer)
            elif isinstance(connected_device, Switch):
                connected_device.forward(sender, frame, self)
            elif isinstance(connected_device, Hub):
                connected_device.broadcast(sender, frame, self)
            else:
                self.physical_layer.transmit(sender, receiver, frame,self)
            self.sent_frames += 1

    def receive(self, receiver, frame):
        print(f"\n[L2/RX] frame arrived at {receiver.name}")

        self.mac_table[frame.source_mac] = receiver

        if not frame.is_ack:
            if "|" not in frame.payload:
                print("[L2/RX] invalid frame format; drop")
                return

            data, recv_checksum = frame.payload.split("|")
            recv_checksum = int(recv_checksum)

            calculated = sum(ord(c) for c in data) % 256

            if calculated == recv_checksum:
                print("[L2/RX] checksum ok")
                frame.payload = data   # restore original
            else:
                print("[L2/RX] checksum mismatch; frame dropped")
                return

        # ADDRESS LEARNING TRIGGER
        if not frame.is_ack:
            print(f"[L2/RX] {receiver.name} -> ACK(seq={frame.seq_num})")
            # Sending back ACK frames for Switch to learn MAC address of receiver.
            self.send_ack(receiver, frame.source_mac, frame.seq_num)
        else:
            print(f"[L2/RX] ACK(seq={frame.seq_num}) accepted")

        self.received_frames += 1

    def add_error_detection(self, frame):
        frame.error_code = sum(ord(c) for c in frame.payload) % 256

    def check_error(self, frame):
        calculated = sum(ord(c) for c in frame.payload) % 256
        return calculated == frame.error_code

    def send_ack(self, sender, receiver_mac, seq_num):
    # sender: Device sending ACK
    # receiver_mac: Device who should recevive ACK (Original Sender)
        print(f"\n[L2/ACK] {sender.name} sending ACK(seq={seq_num})")
    
    # 1. Make ACK frames(Source = sender, Dest = original sender's MAC)
        ack_frame = Frame(sender.mac_address, receiver_mac, "ACK")
        ack_frame.is_ack = True
        ack_frame.seq_num = seq_num

    # 2. Intermediate device (Switch/Hub) connected to sender
        connected_device = next((p for p in sender.ports if isinstance(p, (Hub, Switch, Bridge))), None)

    # 3. Sending ACK through switch for learning address
        if isinstance(connected_device, Switch):
        # Switch will learn 'sender' address and forward the ACK
            connected_device.forward(sender, ack_frame, self)
        elif isinstance(connected_device, Hub):
            connected_device.broadcast(sender, ack_frame, self)
        else:
        # If no intermidiate device, send directly
            receiver_device = self.mac_table.get(receiver_mac)
            if receiver_device:
                self.physical_layer.transmit(sender, receiver_device, ack_frame, self)
            else:
                print("[L2/ACK] receiver for ACK not found")

    def stats(self):
        print("\n--- Data Link Layer Stats ---")
        print(f"Frames Sent: {self.sent_frames}")
        print(f"Frames Received: {self.received_frames}")
        