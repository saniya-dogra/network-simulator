class GoBackN:

    def __init__(self, window_size=4, total_frames=8):
        self.window_size = window_size
        self.total_frames = total_frames

    def send_frames(self, lost_frame=None):

        print("\nGO BACK N PROTOCOL")
        print(f"Window Size : {self.window_size}")
        print(f"Total Frames : {self.total_frames}")

        sent = 0
        acknowledged = 0

        while acknowledged < self.total_frames:

            # Send all frames within the current window
            window_end = min(sent + self.window_size, self.total_frames)

            for seq in range(sent, window_end):
                if seq == lost_frame:
                    print(f"  [SENT]  Frame {seq}  <-- LOST IN TRANSMISSION")
                else:
                    print(f"  [SENT]  Frame {seq}")

            # Simulate ACKs coming back
            # If a frame was lost, only ACKs up to that frame arrive
            if lost_frame is not None and sent <= lost_frame < window_end:
                print(f"  [TIMEOUT] No ACK for Frame {lost_frame}. Retransmitting from Frame {lost_frame}.")
                sent = lost_frame
                lost_frame = None  # Only lose it once
            else:
                # All frames in window acknowledged
                for seq in range(sent, window_end):
                    print(f"  [ACK]   ACK received for Frame {seq}")
                acknowledged = window_end
                sent = window_end
                if sent < self.total_frames:
                    print(f"  [WINDOW SLIDES] Window now covers Frames {sent} to {min(sent + self.window_size - 1, self.total_frames - 1)}")

        print("All Frames Successfully Delivered via Go-Back-N")