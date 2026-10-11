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