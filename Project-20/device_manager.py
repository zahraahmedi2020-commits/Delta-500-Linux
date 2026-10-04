from device import Device, router1, switch1

class DeviceManager:

    def __init__(self):
        self.devices = []

    def add_device(self, ip, name, device_type, model, serial, status, new_status):
        device = Device(ip, name, device_type, model, serial, status, new_status)
        self.devices.append(device)

    def find_device(self, ip):
        for device in self.devices:
            if device.ip==ip:
                print(f'name device:{device.name}',f'IP device:{device.ip}',
                f' device_type:{device.device_type}', f'Serial device:{device.serial}',
                f'status device:{device.status}' )
                return device
        
        
        return None

    def remove_device(self,device):
        self.devices.remove(device)

    def update_device(self,device):
             if device.status == "offline":
                 device.new_status = "online"
                 device.status = "online"
                 print(device.new_status)
                 print("successfully Status")
            
    def show_devices(self, devices):
        if not devices:
                print("not exist devise for show")
        else:
            for device in devices:
                print(f'name device:{device.name}',f'IP device:{device.ip}',
                f' device_type:{device.device_type}', 
                f'Serial device:{device.serial}', f'status device:{device.status}',
                f'New status device:{device.new_status}' )
           

    def filter_devices(self, name):
        listdevices=[]
        for device in self.devices:
            if device.name == name:
                listdevices.append(device)
                
        return listdevices
      

manager = DeviceManager()
manager.devices.append(switch1)
manager.devices.append(router1)
