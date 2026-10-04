class Device:
    def __init__(self, ip, name, device_type, model, serial, status, new_status):
        self.ip = ip
        self.name = name
        self.device_type = device_type
        self.model = model
        self.serial = serial
        self.status = status
        self.new_status = new_status

router1 = Device("192.168.20.1","Router_1","router", "sisco", "E982T370HH1", "offline","offline")
switch1 = Device("192.168.20.2", "Switch_1","switch", "sisco", "ER82T370HU0", "online", "online ")

