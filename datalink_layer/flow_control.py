class StopAndWait:

    def send(self, frame):

        print("\nSending Frame")

        frame.show_frame()

        print("Waiting for ACK...")

        print("ACK Received")

        print("Next Frame Can Be Sent")