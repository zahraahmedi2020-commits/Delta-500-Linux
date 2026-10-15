def evaluate_device_health(metrics):
    cpu = metrics["cpu_usage"]
    memory = metrics["memory_usage"]
    temperature = metrics["temperature"]
    interface_status = metrics["interface_status"]

    if (
        cpu >= 90
        or memory >= 95
        or temperature >= 80
        or interface_status != "up"
    ):
        return "Critical"

    if (
        cpu >= 75
        or memory >= 85
        or temperature >= 70
    ):
        return "Warning"

    return "Healthy"
def test_cpu_boundary(self):
    metrics = {
        "cpu_usage": 74,
        "memory_usage": 40,
        "temperature": 40,
        "interface_status": "up"
    }

    self.assertEqual(
        evaluate_device_health(metrics),
        "Healthy"
    )

    metrics["cpu_usage"] = 75

    self.assertEqual(
        evaluate_device_health(metrics),
        "Warning"
    )
def test_cpu_critical_boundary(self):
    metrics = {
        "cpu_usage": 89,
        "memory_usage": 40,
        "temperature": 40,
        "interface_status": "up"
    }

    self.assertEqual(
        evaluate_device_health(metrics),
        "Warning"
    )

    metrics["cpu_usage"] = 90

    self.assertEqual(
        evaluate_device_health(metrics),
        "Critical"
    )
