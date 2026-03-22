"""
DATA LINK LAYER MODULE

This file represents the Data Link Layer in the network simulator.

Instead of implementing everything here, the functionalities are
modularized into separate components:

- Switch (MAC Learning) → devices/switch.py
- Bridge → devices/bridge.py
- Error Control (Parity) → protocols/error_control.py
- Flow Control (Stop & Wait) → protocols/flow_control.py
- Access Control (CSMA/CD) → protocols/access_control.py

This modular design improves readability and maintainability.
"""


