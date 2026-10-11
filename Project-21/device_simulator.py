import random


def simulate_device_metrics():
    metrics = {
        "cpu_usage": random.randint(10, 95),
        "memory_usage": random.randint(20, 90),
        "temperature": random.randint(35, 85),
        "interface_status": "up"
    }

    return metrics