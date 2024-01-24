import unittest
from unittest.mock import patch
from urllib.robotparser import RobotFileParser

from TP1.robot import *




class TestRobotsEntre(unittest.TestCase):

    @patch.object(RobotFileParser, 'read')
    @patch.object(RobotFileParser, 'set_url')
    def test_robots_entre_allow(self, mock_set_url, mock_read):
        # Arrange
        url_base = "http://www.ensai.fr"
        mock_set_url.return_value = None
        mock_read.return_value = None

        # Act
        result = robots_entre(url_base)

        # Assert
        self.assertTrue(result)

    @patch.object(RobotFileParser, 'read')
    @patch.object(RobotFileParser, 'set_url')
    def test_robots_entre_disallow(self, mock_set_url, mock_read):
        # Arrange
        url_base = "http://www.example.com"
        mock_set_url.return_value = None
        mock_read.return_value = None

        # Mocking can_fetch to return False
        with patch.object(RobotFileParser, 'can_fetch', return_value=False):
            # Act
            result = robots_entre(url_base)

        # Assert
        self.assertFalse(result)

    @patch.object(RobotFileParser, 'read')
    @patch.object(RobotFileParser, 'set_url')
    def test_robots_entre_invalid_url(self, mock_set_url, mock_read):
        # Arrange
        url_base = "invalid_url"
        mock_set_url.return_value = None
        mock_read.return_value = None

        # Act
        result = robots_entre(url_base)

        # Assert
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
