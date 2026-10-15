
import unittest

from health_evaluator import evaluate_device_health
from alert_manager import generate_alert


class TestHealthMonitor(unittest.TestCase):

    def test_healthy_device(self):
        metrics = {
            "cpu_usage": 30,
            "memory_usage": 40,
            "temperature": 45,
            "interface_status": "up"
        }

        self.assertEqual(
            evaluate_device_health(metrics),
            "Healthy"
        )

    def test_warning_device(self):
        metrics = {
            "cpu_usage": 80,
            "memory_usage": 50,
            "temperature": 40,
            "interface_status": "up"
        }

        self.assertEqual(
            evaluate_device_health(metrics),
            "Warning"
        )

    def test_critical_device(self):
        metrics = {
            "cpu_usage": 95,
            "memory_usage": 50,
            "temperature": 40,
            "interface_status": "up"
        }

        self.assertEqual(
            evaluate_device_health(metrics),
            "Critical"
        )

    def test_critical_alert(self):
        alert = generate_alert("Critical")

        self.assertIn("CRITICAL", alert)
    
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
    
    def test_memory_boundary(self):
        metrics = {
            "cpu_usage": 30,
            "memory_usage": 84,
            "temperature": 40,
            "interface_status": "up"
        }

        self.assertEqual(
            evaluate_device_health(metrics),
            "Healthy"
        )

        metrics["memory_usage"] = 85

        self.assertEqual(
            evaluate_device_health(metrics),
            "Warning"
        )

        metrics["memory_usage"] = 94

        self.assertEqual(
            evaluate_device_health(metrics),
            "Warning"
        )

        metrics["memory_usage"] = 95

        self.assertEqual(
            evaluate_device_health(metrics),
            "Critical"
        )
    
    def test_temperature_boundary(self):
        metrics = {
            "cpu_usage": 30,
            "memory_usage": 40,
            "temperature": 69,
            "interface_status": "up"
        }

        self.assertEqual(
            evaluate_device_health(metrics),
            "Healthy"
        )

        metrics["temperature"] = 70

        self.assertEqual(
            evaluate_device_health(metrics),
            "Warning"
        )

        metrics["temperature"] = 79

        self.assertEqual(
            evaluate_device_health(metrics),
            "Warning"
        )

        metrics["temperature"] = 80

        self.assertEqual(
            evaluate_device_health(metrics),
            "Critical"
        )
    
    def test_interface_down(self):
        metrics = {
            "cpu_usage": 30,
            "memory_usage": 40,
            "temperature": 45,
            "interface_status": "down"
        }

        self.assertEqual(
            evaluate_device_health(metrics),
            "Critical"
        )

    
if __name__ == "__main__":
    unittest.main()
