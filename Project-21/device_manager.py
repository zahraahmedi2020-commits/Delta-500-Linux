
class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def show_devices(self):
        for device in self.devices:
            print(
                f"Name: {device.name}, "
                f"IP: {device.ip}, "
                f"Type: {device.device_type}"
            )