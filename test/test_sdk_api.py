# coding: utf-8

"""
    Asteroid Agents API

    Version 1 of the Asteroid Agents API

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.sdk_api import SDKApi


class TestSDKApi(unittest.TestCase):
    """SDKApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SDKApi()

    def tearDown(self) -> None:
        pass

    def test_execute_agent(self) -> None:
        """Test case for execute_agent

        Execute an agent
        """
        pass

    def test_get_browser_session_recording(self) -> None:
        """Test case for get_browser_session_recording

        Get browser session recording
        """
        pass

    def test_get_execution_result(self) -> None:
        """Test case for get_execution_result

        Get execution result
        """
        pass

    def test_get_execution_status(self) -> None:
        """Test case for get_execution_status

        Get execution status
        """
        pass


if __name__ == '__main__':
    unittest.main()
