
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

        result = connect_device(self.device)

        self.assertIs(result, mock_connection)
        mock_connect.assert_called_once()

    @patch("connection.ConnectHandler")
    def test_connection_timeout(self, mock_connect):
        mock_connect.side_effect = NetmikoTimeoutException(
            "Connection timed out"
        )

        result = connect_device(self.device)

        self.assertIsNone(result)

    @patch("connection.ConnectHandler")
    def test_authentication_failure(self, mock_connect):
        mock_connect.side_effect = NetmikoAuthenticationException(
            "Authentication failed"
        )

        result = connect_device(self.device)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
