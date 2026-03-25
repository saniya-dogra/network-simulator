def stop_and_wait(sender, packet):
    print("\n[Flow Control: Stop & Wait]")

    sender.send(packet)

    ack = True  # simulate ACK

    if ack:
        print("ACK received")
    else:
        print("Resending packet")
        sender.send(packet)


def go_back_n(sender, packets, window_size=3, fail_once_index=None):
    print(f"\n[Flow Control: Go-Back-N, window={window_size}]")

    base = 0
    next_seq = 0
    dropped_once = False

    while base < len(packets):
        while next_seq < len(packets) and next_seq < base + window_size:
            pkt = packets[next_seq]
            print(f"Sending frame seq={next_seq}")
            sender.send(pkt)
            next_seq += 1

        ack_end = next_seq - 1

        # Simulate one lost ACK to force retransmission behavior.
        if fail_once_index is not None and not dropped_once and base <= fail_once_index <= ack_end:
            print(f"ACK loss simulated at seq={fail_once_index}; retransmitting from seq={fail_once_index}")
            base = fail_once_index
            next_seq = fail_once_index
            dropped_once = True
        else:
            print(f"ACKs received up to seq={ack_end}")
            base = next_seq