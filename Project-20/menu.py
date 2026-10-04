from device_manager import DeviceManager, manager

def menu():
    while True:
        print("""
=== Delta-500 Menu ===

===== Network Device Manager =====

1. Add Device
2. Find Device
3. Remove Device
4. Update Device
5. Show Devices
6. Filter Devices
7. Exit
""")

        choice = input("Enter your choice: ")
        if choice == "1":
            
            ip = input("Enter IP: ")
            device = manager.find_device(ip)
            if device is None:
               name = input("Enter name: ")
               device_type = input("Enter device_type:")
               model = input("Enter Model: ")
               serial = input("Enter Serial: ")
               status = input("Enter status:")
               new_status = " "
               manager.add_device(ip, name, device_type, model, serial, status, new_status)
            else:
                 print("this device by this ip exist.")
            
        elif choice == "2":
            ip = input("Enter IP: ")
            device = manager.find_device(ip)
            if device is None:
                print("not exist devise for remove")

        elif choice == "3":
            ip = input("Enter IP: ")
            device = manager.find_device(ip)
            if device is None:
                print("not exist devise for remove")
            else:
                manager.remove_device(device)

        elif choice == "4":
            ip = input("Enter IP: ")
            device = manager.find_device(ip)
            if device is None:
                print("not exist devise for update")
            else:
                manager.update_device(device)

        elif choice == "5":
            manager.show_devices(manager.devices)

        elif choice == "6":
            name = input("enter name for filter Devices:")
            devices = manager.filter_devices(name)
            if not devices:
                print("not exist devise for filter")
            else:
               manager.show_devices(devices)

        elif choice == "7":
            print("Exiting Menu...")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
