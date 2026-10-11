def generate_alert(health_status):
    if health_status == "Healthy":
        return "OK: Device is operating normally."

    elif health_status == "Warning":
        return "WARNING: Check device metrics."

    elif health_status == "Critical":
        return "CRITICAL: Immediate attention required."

    else:
        return "UNKNOWN: Unrecognized health status."