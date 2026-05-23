from physical_layer.connection import Connection


def connect(device1, device2):

    connection = Connection(device1, device2)

    device1.add_connection(connection)
    device2.add_connection(connection)

    return connection