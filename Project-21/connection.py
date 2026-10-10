
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException


def connect_device(device):
    connection_params = {
        "device_type": device.device_type,
        "host": device.ip,
        "username": device.username,
        "password": device.password,
    }

    try:
        connection = ConnectHandler(**connection_params)
        print(f"Connected to {device.name}")
        return connection

    except NetmikoTimeoutException:
        print(f"Connection timed out: {device.ip}")

    except NetmikoAuthenticationException:
        print(f"Authentication failed: {device.name}")

    return None