class SelectiveRepeat:

    def __init__(self, window_size=4, total_frames=8):
        self.window_size = window_size
        self.total_frames = total_frames

    def send_frames(self, lost_frames=None):

        if lost_frames is None:
            lost_frames = []

        print("\nSELECTIVE REPEAT PROTOCOL")
        print(f"Window Size : {self.window_size}")
        print(f"Total Frames : {self.total_frames}")

        # Track which frames have been acknowledged
        acked = [False] * self.total_frames
        sent_lost = set()

        for seq in range(self.total_frames):
            if seq in lost_frames:
                print(f"  [SENT]  Frame {seq}  <-- LOST IN TRANSMISSION")
                sent_lost.add(seq)
            else:
                print(f"  [SENT]  Frame {seq}")
                acked[seq] = True
                print(f"  [ACK]   ACK received for Frame {seq}")

        # Retransmit only the lost frames (not the whole window)
        if sent_lost:
            print(f"\n  [SELECTIVE RETRANSMIT] Retransmitting only lost frames: {sorted(sent_lost)}")
            for seq in sorted(sent_lost):
                print(f"  [RESENT] Frame {seq}")
                acked[seq] = True
                print(f"  [ACK]    ACK received for Frame {seq}")

        print("All Frames Successfully Delivered via Selective Repeat")