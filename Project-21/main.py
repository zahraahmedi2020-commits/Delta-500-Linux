
from device import Device
from device_manager import DeviceManager
from connection import connect_device
from commands import get_device_info
from device_simulator import simulate_device_metrics
from health_evaluator import evaluate_device_health
from alert_manager import generate_alert
def main():
    manager = DeviceManager()
    
    router = Device(
        name="Router_1",
        ip="192.168.20.1",
        device_type="cisco_ios",
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD"
    )

    manager.add_device(router)
    manager.show_devices()
    print("\n=== Device Health Monitoring ===")

    metrics = simulate_device_metrics()
    health = evaluate_device_health(metrics)

    print("Simulated Metrics:", metrics)
    print("Health Status:", health)
    
    alert = generate_alert(health)
    print("Alert:", alert)
    # Real SSH testing is disabled until a device is available.
    test_real_ssh = False

    if test_real_ssh:
        connection = connect_device(router)

        if connection:
            try:
                output = get_device_info(
                    connection,
                    "show ip interface brief"
                )
                print(output)
            finally:
                connection.disconnect()


if __name__ == "__main__":
    main()
