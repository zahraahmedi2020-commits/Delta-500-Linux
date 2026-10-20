from config import DEVICE_TYPE, CONNECTION_TIMEOUT, FAST_CLI
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
from logger_config import get_logger


logger = get_logger(__name__)


def connect_device(device):
    connection_params = {
        "device_type": DEVICE_TYPE,
        "host": device.ip,
        "username": device.username,
        "password": device.password,
        "timeout": CONNECTION_TIMEOUT,
        "fast_cli": FAST_CLI,
    }

    try:
        connection = ConnectHandler(**connection_params)
        logger.info("Connected to device: %s", device.name)
        print(f"Connected to {device.name}")
        return connection

    except NetmikoTimeoutException:
        logger.warning(
            "Connection timed out for device %s at %s",
            device.name,
            device.ip,
        )
        print(f"Connection timed out: {device.ip}")

    except NetmikoAuthenticationException:
        logger.error(
            "Authentication failed for device %s at %s",
            device.name,
            device.ip,
        )
        print(f"Authentication failed: {device.name}")

    except Exception:
        logger.exception(
            "Unexpected error while connecting to device %s at %s",
            device.name,
            device.ip,
        )
        print(f"Unexpected connection error: {device.name}")

    return None
