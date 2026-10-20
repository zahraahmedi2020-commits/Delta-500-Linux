
import unittest
from unittest.mock import patch, MagicMock

from connection import connect_device
from netmiko.exceptions import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


class TestConnection(unittest.TestCase):

    def setUp(self):
        self.device = MagicMock()
        self.device.name = "Router_1"
        self.device.ip = "192.168.20.1"
        self.device.username = "test_user"
        self.device.password = "test_password"

    @patch("connection.ConnectHandler")
    def test_successful_connection(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        with self.assertLogs("connection", level="INFO") as logs:
            result = connect_device(self.device)

        self.assertIs(result, mock_connection)
        mock_connect.assert_called_once()

        self.assertTrue(
             any(
                  "Connected to device: Router_1" in message
                  for message in logs.output
                 )
        )

    @patch("connection.ConnectHandler")
    
    def test_connection_timeout(self, mock_connect):
        mock_connect.side_effect = NetmikoTimeoutException(
            "Connection timed out"
        )

        with self.assertLogs("connection", level="WARNING") as logs:
            result = connect_device(self.device)

        self.assertIsNone(result)

        self.assertTrue(
            any(
               "Connection timed out for device Router_1"
               in message
               for message in logs.output
             )
        )


    
    @patch("connection.ConnectHandler")
    def test_authentication_failure(self, mock_connect):
        mock_connect.side_effect = NetmikoAuthenticationException(
            "Authentication failed"
        )

        with self.assertLogs("connection", level="ERROR") as logs:
             result = connect_device(self.device)

        self.assertIsNone(result)

        self.assertTrue(
            any(
               "Authentication failed for device Router_1"
               in message
               for message in logs.output
               )
         )



if __name__ == "__main__":
    unittest.main()
