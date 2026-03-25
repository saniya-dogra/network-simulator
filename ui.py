import tkinter as tk
import time
from devices.end_device import EndDevice
from devices.hub import Hub
from devices.switch import Switch
from utils.packet import Packet


class NetworkUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Simulator")

        self.canvas = tk.Canvas(root, width=800, height=500, bg="white")
        self.canvas.pack()

        self.output = tk.Text(root, height=12)
        self.output.pack()

        self.create_buttons()

    # =========================
    # LOG FUNCTION
    # =========================
    def log(self, msg):
        self.output.insert(tk.END, msg + "\n")
        self.output.see(tk.END)

    # =========================
    # DRAWING FUNCTIONS
    # =========================
    def draw_node(self, x, y, name, color="lightblue"):
        self.canvas.create_oval(x, y, x+40, y+40, fill=color)
        self.canvas.create_text(x+20, y+20, text=name)

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)

    # =========================
    # PACKET ANIMATION
    # =========================
    def animate_packet(self, x1, y1, x2, y2):
        packet = self.canvas.create_oval(x1, y1, x1+10, y1+10, fill="red")

        steps = 20
        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps

        for _ in range(steps):
            self.canvas.move(packet, dx, dy)
            self.root.update()
            time.sleep(0.05)

        self.canvas.delete(packet)

    # =========================
    # BUTTONS
    # =========================
    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Test Hub", command=self.test_hub).pack(side="left")
        tk.Button(frame, text="Test Switch", command=self.test_switch).pack(side="left")

    # =========================
    # HUB TEST (UPDATED)
    # =========================
    def test_hub(self):
        from protocols.noise import add_noise

        self.canvas.delete("all")
        self.output.delete(1.0, tk.END)

        hub = Hub("Hub1")
        devices = [EndDevice(f"D{i}") for i in range(5)]

        self.draw_node(350, 200, "Hub", "orange")

        positions = [(100, 100), (600, 100), (100, 350), (600, 350), (350, 400)]

        for i, d in enumerate(devices):
            hub.connect(d)
            x, y = positions[i]
            self.draw_node(x, y, d.name)
            self.draw_line(370, 220, x+20, y+20)

        packet = Packet("D0", "D3", "Hello")

        # 🔥 ADD-ONS
        binary = packet.to_binary()
        noisy_data = add_noise(packet.data)

        self.log("=== HUB TRANSMISSION ===")
        self.log(f"Original Data: {packet.data}")
        self.log(f"Binary: {binary}")
        self.log(f"After Noise: {noisy_data}")
        self.log("Hub behavior: frame is repeated on every other port")

        # animation: sender -> hub
        sx, sy = positions[0]
        self.animate_packet(sx+20, sy+20, 370, 220)

        # animation: hub -> every receiver except sender (true hub broadcast)
        for i, (x, y) in enumerate(positions):
            if i == 0:
                continue
            self.animate_packet(370, 220, x+20, y+20)

            receiver = devices[i].name
            if receiver == packet.dest:
                self.log(f"{receiver}: accepted frame")
            else:
                self.log(f"{receiver}: discarded frame (not destination)")

        devices[0].send(packet)

        self.log("D3 receives data after hub broadcast\n")

    # =========================
    # SWITCH TEST (UPDATED)
    # =========================
    def test_switch(self):
        from protocols.noise import add_noise
        from layers.line_coding import nrz_encode

        self.canvas.delete("all")
        self.output.delete(1.0, tk.END)

        switch = Switch("Switch1")
        devices = [EndDevice(f"S{i}") for i in range(5)]

        self.draw_node(350, 200, "Switch", "green")

        positions = [(100, 100), (600, 100), (100, 350), (600, 350), (350, 400)]

        for i, d in enumerate(devices):
            switch.connect(d)
            x, y = positions[i]
            self.draw_node(x, y, d.name)
            self.draw_line(370, 220, x+20, y+20)

        packet = Packet("S0", "S4", "Hello")

        # 🔥 ADD-ONS
        binary = packet.to_binary()
        signal = nrz_encode(binary)
        noisy_data = add_noise(packet.data)

        self.log("=== SWITCH TRANSMISSION ===")
        self.log(f"Original Data: {packet.data}")
        self.log(f"Binary: {binary}")
        self.log(f"NRZ Signal: {signal[:20]} ...")
        self.log(f"After Noise: {noisy_data}")

        # animation
        sx, sy = positions[0]
        dx, dy = positions[4]

        self.animate_packet(sx+20, sy+20, 370, 220)
        self.animate_packet(370, 220, dx+20, dy+20)

        switch.receive(packet, devices[0])

        self.log("Delivered to S4\n")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkUI(root)
    root.mainloop()