## Current Features

- **Device Management:** Stores and displays network device information.
- **Device Simulation:** Generates simulated CPU usage, memory usage, temperature, and interface status.
- **Health Evaluation:** Classifies device health as `Healthy`, `Warning`, or `Critical`.
- **Alert Management:** Generates an appropriate alert message based on the health status.
- **Main Workflow:** Integrates device management, simulated metrics, health evaluation, and alert generation.

- **SSH Connection Management:** Establishes device connections using Netmiko and handles connection timeouts, authentication failures, and unexpected errors.
- **Logging:** Records successful connections and connection errors in `logs/project21.log` with timestamps and severity levels.
- **Automated Connection Tests:** Uses `unittest` and mocks to test connection success, timeouts, and authentication failures without requiring physical network hardware.

## Current Limitations

- Device metrics are simulated and do not represent real hardware measurements.
- Real SSH connectivity has not yet been tested against a physical network device.
- The initial device configuration uses Cisco IOS as the target platform.

- Automated connection tests use mocks; real SSH connectivity and hardware behavior remain unverified.


## Run the Project

Activate the project's virtual environment, then run:

```bash
python main.py
```

The application displays the registered device, simulated health metrics, health status, and corresponding alert.

## Next Steps

- Improve health monitoring and alert handling.
- Add repeatable tests for different health conditions.
- Prepare for real-device SSH testing when compatible hardware is available.
- Update the documentation as new features are implemented.