"""
Test suite for the AsteroidClient high-level client interface.

This module contains comprehensive tests for the AsteroidClient class,
including unit tests for all public methods, error handling, and edge cases.
"""

import unittest
import time
import os
import tempfile
from unittest.mock import Mock, patch, MagicMock, mock_open
from typing import Dict, Any

from asteroid_odyssey.client import (
    AsteroidClient, 
    create_client,
    execute_agent,
    get_execution_status,
    get_execution_result,
    wait_for_execution_result,
    upload_execution_files,
    get_browser_session_recording
)
from openapi_client import (
    Configuration,
    ApiClient,
    SDKApi,
    ExecutionApi,
    ExecutionStatusResponse,
    ExecutionResultResponse,
    BrowserSessionRecordingResponse,
    UploadExecutionFiles200Response,
    Status
)
from openapi_client.exceptions import ApiException


class TestAsteroidClient(unittest.TestCase):
    """Test suite for the AsteroidClient class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.api_key = "test-api-key"
        self.base_url = "https://test.asteroid.ai/api/v1"
        self.agent_id = "test-agent-id"
        self.execution_id = "test-execution-id"
        
    def test_client_initialization_with_defaults(self):
        """Test client initialization with default base URL."""
        client = AsteroidClient(self.api_key)
        
        self.assertIsNotNone(client.api_client)
        self.assertIsNotNone(client.sdk_api)
        self.assertIsNotNone(client.execution_api)
        
    def test_client_initialization_with_custom_base_url(self):
        """Test client initialization with custom base URL."""
        client = AsteroidClient(self.api_key, self.base_url)
        
        self.assertIsNotNone(client.api_client)
        self.assertIsNotNone(client.sdk_api)
        self.assertIsNotNone(client.execution_api)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_execute_agent_success(self, mock_sdk_api):
        """Test successful agent execution."""
        # Setup mock
        mock_response = Mock()
        mock_response.execution_id = self.execution_id
        mock_sdk_api.return_value.execute_agent.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        execution_data = {"input": "test input"}
        
        # Execute
        result = client.execute_agent(self.agent_id, execution_data)
        
        # Verify
        self.assertEqual(result, self.execution_id)
        mock_sdk_api.return_value.execute_agent.assert_called_once_with(self.agent_id, execution_data)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_execute_agent_api_exception(self, mock_sdk_api):
        """Test agent execution with API exception."""
        # Setup mock
        mock_sdk_api.return_value.execute_agent.side_effect = ApiException("API Error")
        
        client = AsteroidClient(self.api_key)
        execution_data = {"input": "test input"}
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.execute_agent(self.agent_id, execution_data)
        
        self.assertIn("Failed to execute agent", str(context.exception))
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_get_execution_status_success(self, mock_sdk_api):
        """Test successful execution status retrieval."""
        # Setup mock
        mock_response = ExecutionStatusResponse(
            execution_id=self.execution_id,
            status=Status.RUNNING,
            reason=None
        )
        mock_sdk_api.return_value.get_execution_status.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = client.get_execution_status(self.execution_id)
        
        # Verify
        self.assertEqual(result, mock_response)
        self.assertEqual(result.execution_id, self.execution_id)
        self.assertEqual(result.status, Status.RUNNING)
        mock_sdk_api.return_value.get_execution_status.assert_called_once_with(self.execution_id)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_get_execution_status_api_exception(self, mock_sdk_api):
        """Test execution status retrieval with API exception."""
        # Setup mock
        mock_sdk_api.return_value.get_execution_status.side_effect = ApiException("API Error")
        
        client = AsteroidClient(self.api_key)
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.get_execution_status(self.execution_id)
        
        self.assertIn("Failed to get execution status", str(context.exception))
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_get_execution_result_success(self, mock_sdk_api):
        """Test successful execution result retrieval."""
        # Setup mock
        test_result = {"output": "test output", "success": True}
        mock_response = ExecutionResultResponse(
            execution_id=self.execution_id,
            result=test_result,
            error=None,
            status=Status.COMPLETED
        )
        mock_sdk_api.return_value.get_execution_result.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = client.get_execution_result(self.execution_id)
        
        # Verify
        self.assertEqual(result, test_result)
        mock_sdk_api.return_value.get_execution_result.assert_called_once_with(self.execution_id)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_get_execution_result_with_error(self, mock_sdk_api):
        """Test execution result retrieval when execution failed."""
        # Setup mock
        error_message = "Execution failed"
        mock_response = ExecutionResultResponse(
            execution_id=self.execution_id,
            result=None,
            error=error_message,
            status=Status.FAILED
        )
        mock_sdk_api.return_value.get_execution_result.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.get_execution_result(self.execution_id)
        
        self.assertIn(error_message, str(context.exception))
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_get_execution_result_none_result(self, mock_sdk_api):
        """Test execution result retrieval with None result."""
        # Setup mock
        mock_response = ExecutionResultResponse(
            execution_id=self.execution_id,
            result=None,
            error=None,
            status=Status.COMPLETED
        )
        mock_sdk_api.return_value.get_execution_result.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = client.get_execution_result(self.execution_id)
        
        # Verify
        self.assertEqual(result, {})
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_get_execution_result_api_exception(self, mock_sdk_api):
        """Test execution result retrieval with API exception."""
        # Setup mock
        mock_sdk_api.return_value.get_execution_result.side_effect = ApiException("API Error")
        
        client = AsteroidClient(self.api_key)
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.get_execution_result(self.execution_id)
        
        self.assertIn("Failed to get execution result", str(context.exception))
        
    @patch('asteroid_odyssey.client.SDKApi')
    @patch('time.sleep')
    def test_wait_for_execution_result_success(self, mock_sleep, mock_sdk_api):
        """Test successful wait for execution result."""
        # Setup mock responses
        test_result = {"output": "test output", "success": True}
        
        # First call returns RUNNING, second returns COMPLETED
        status_responses = [
            ExecutionStatusResponse(execution_id=self.execution_id, status=Status.RUNNING),
            ExecutionStatusResponse(execution_id=self.execution_id, status=Status.COMPLETED)
        ]
        
        result_response = ExecutionResultResponse(
            execution_id=self.execution_id,
            result=test_result,
            error=None,
            status=Status.COMPLETED
        )
        
        mock_sdk_api.return_value.get_execution_status.side_effect = status_responses
        mock_sdk_api.return_value.get_execution_result.return_value = result_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = client.wait_for_execution_result(self.execution_id, interval=0.1)
        
        # Verify
        self.assertEqual(result, test_result)
        self.assertEqual(mock_sdk_api.return_value.get_execution_status.call_count, 2)
        mock_sdk_api.return_value.get_execution_result.assert_called_once_with(self.execution_id)
        mock_sleep.assert_called_once_with(0.1)
        
    @patch('asteroid_odyssey.client.SDKApi')
    @patch('time.sleep')
    def test_wait_for_execution_result_failed(self, mock_sleep, mock_sdk_api):
        """Test wait for execution result when execution fails."""
        # Setup mock
        status_response = ExecutionStatusResponse(
            execution_id=self.execution_id,
            status=Status.FAILED,
            reason="Execution failed"
        )
        mock_sdk_api.return_value.get_execution_status.return_value = status_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.wait_for_execution_result(self.execution_id)
        
        self.assertIn("ended with status: failed", str(context.exception))
        self.assertIn("Execution failed", str(context.exception))
        
    @patch('asteroid_odyssey.client.SDKApi')
    @patch('time.sleep')
    def test_wait_for_execution_result_cancelled(self, mock_sleep, mock_sdk_api):
        """Test wait for execution result when execution is cancelled."""
        # Setup mock
        status_response = ExecutionStatusResponse(
            execution_id=self.execution_id,
            status=Status.CANCELLED,
            reason="User cancelled"
        )
        mock_sdk_api.return_value.get_execution_status.return_value = status_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.wait_for_execution_result(self.execution_id)
        
        self.assertIn("ended with status: cancelled", str(context.exception))
        self.assertIn("User cancelled", str(context.exception))
        
    @patch('asteroid_odyssey.client.SDKApi')
    @patch('time.sleep')
    @patch('time.time')
    def test_wait_for_execution_result_timeout(self, mock_time, mock_sleep, mock_sdk_api):
        """Test wait for execution result with timeout."""
        # Setup mock - simulate timeout
        mock_time.side_effect = [0, 10]  # start_time=0, elapsed_time=10
        
        status_response = ExecutionStatusResponse(
            execution_id=self.execution_id,
            status=Status.RUNNING
        )
        mock_sdk_api.return_value.get_execution_status.return_value = status_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.wait_for_execution_result(self.execution_id, timeout=5.0)
        
        self.assertIn("timed out after 5.0s", str(context.exception))
        
    @patch('asteroid_odyssey.client.ExecutionApi')
    def test_upload_execution_files_bytes(self, mock_execution_api):
        """Test file upload with bytes content."""
        # Setup mock
        mock_response = UploadExecutionFiles200Response(
            message="Files uploaded successfully",
            file_ids=["file-id-1"]
        )
        mock_execution_api.return_value.upload_execution_files.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        file_content = b"Hello World!"
        
        # Execute
        result = client.upload_execution_files(self.execution_id, [file_content])
        
        # Verify
        self.assertEqual(result, mock_response)
        mock_execution_api.return_value.upload_execution_files.assert_called_once_with(
            self.execution_id,
            files=[("file.txt", file_content)]
        )
        
    @patch('asteroid_odyssey.client.ExecutionApi')
    def test_upload_execution_files_tuples(self, mock_execution_api):
        """Test file upload with filename and content tuples."""
        # Setup mock
        mock_response = UploadExecutionFiles200Response(
            message="Files uploaded successfully",
            file_ids=["file-id-1"]
        )
        mock_execution_api.return_value.upload_execution_files.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        files = [("hello.txt", b"Hello World!"), ("test.txt", "Test content")]
        
        # Execute
        result = client.upload_execution_files(self.execution_id, files)
        
        # Verify
        self.assertEqual(result, mock_response)
        expected_files = [("hello.txt", b"Hello World!"), ("test.txt", b"Test content")]
        mock_execution_api.return_value.upload_execution_files.assert_called_once_with(
            self.execution_id,
            files=expected_files
        )
        
    @patch('asteroid_odyssey.client.ExecutionApi')
    @patch('os.path.isfile', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data=b"File content")
    def test_upload_execution_files_file_path(self, mock_file, mock_isfile, mock_execution_api):
        """Test file upload with file path."""
        # Setup mock
        mock_response = UploadExecutionFiles200Response(
            message="Files uploaded successfully",
            file_ids=["file-id-1"]
        )
        mock_execution_api.return_value.upload_execution_files.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        file_path = "/path/to/test.txt"
        
        # Execute
        result = client.upload_execution_files(self.execution_id, [file_path])
        
        # Verify
        self.assertEqual(result, mock_response)
        mock_file.assert_called_once_with(file_path, 'rb')
        mock_execution_api.return_value.upload_execution_files.assert_called_once_with(
            self.execution_id,
            files=[("test.txt", b"File content")]
        )
        
    @patch('asteroid_odyssey.client.ExecutionApi')
    def test_upload_execution_files_string_content(self, mock_execution_api):
        """Test file upload with string content."""
        # Setup mock
        mock_response = UploadExecutionFiles200Response(
            message="Files uploaded successfully",
            file_ids=["file-id-1"]
        )
        mock_execution_api.return_value.upload_execution_files.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        file_content = "Hello World!"
        
        # Execute
        result = client.upload_execution_files(self.execution_id, [file_content])
        
        # Verify
        self.assertEqual(result, mock_response)
        mock_execution_api.return_value.upload_execution_files.assert_called_once_with(
            self.execution_id,
            files=[("file.txt", b"Hello World!")]
        )
        
    @patch('asteroid_odyssey.client.ExecutionApi')
    def test_upload_execution_files_custom_default_filename(self, mock_execution_api):
        """Test file upload with custom default filename."""
        # Setup mock
        mock_response = UploadExecutionFiles200Response(
            message="Files uploaded successfully",
            file_ids=["file-id-1"]
        )
        mock_execution_api.return_value.upload_execution_files.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        file_content = b"Hello World!"
        
        # Execute
        result = client.upload_execution_files(
            self.execution_id, 
            [file_content], 
            default_filename="custom.txt"
        )
        
        # Verify
        self.assertEqual(result, mock_response)
        mock_execution_api.return_value.upload_execution_files.assert_called_once_with(
            self.execution_id,
            files=[("custom.txt", file_content)]
        )
        
    @patch('asteroid_odyssey.client.ExecutionApi')
    def test_upload_execution_files_api_exception(self, mock_execution_api):
        """Test file upload with API exception."""
        # Setup mock
        mock_execution_api.return_value.upload_execution_files.side_effect = ApiException("API Error")
        
        client = AsteroidClient(self.api_key)
        file_content = b"Hello World!"
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.upload_execution_files(self.execution_id, [file_content])
        
        self.assertIn("Failed to upload execution files", str(context.exception))
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_get_browser_session_recording_success(self, mock_sdk_api):
        """Test successful browser session recording retrieval."""
        # Setup mock
        recording_url = "https://example.com/recording.mp4"
        mock_response = BrowserSessionRecordingResponse(recording_url=recording_url)
        mock_sdk_api.return_value.get_browser_session_recording.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = client.get_browser_session_recording(self.execution_id)
        
        # Verify
        self.assertEqual(result, recording_url)
        mock_sdk_api.return_value.get_browser_session_recording.assert_called_once_with(self.execution_id)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_get_browser_session_recording_api_exception(self, mock_sdk_api):
        """Test browser session recording retrieval with API exception."""
        # Setup mock
        mock_sdk_api.return_value.get_browser_session_recording.side_effect = ApiException("API Error")
        
        client = AsteroidClient(self.api_key)
        
        # Execute and verify exception
        with self.assertRaises(Exception) as context:
            client.get_browser_session_recording(self.execution_id)
        
        self.assertIn("Failed to get browser session recording", str(context.exception))
        
    def test_context_manager(self):
        """Test client as context manager."""
        with AsteroidClient(self.api_key) as client:
            self.assertIsNotNone(client)
            self.assertIsInstance(client, AsteroidClient)


class TestConvenienceFunctions(unittest.TestCase):
    """Test suite for convenience functions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.api_key = "test-api-key"
        self.base_url = "https://test.asteroid.ai/api/v1"
        self.agent_id = "test-agent-id"
        self.execution_id = "test-execution-id"
        
    def test_create_client_with_defaults(self):
        """Test create_client function with default parameters."""
        client = create_client(self.api_key)
        self.assertIsInstance(client, AsteroidClient)
        
    def test_create_client_with_base_url(self):
        """Test create_client function with custom base URL."""
        client = create_client(self.api_key, self.base_url)
        self.assertIsInstance(client, AsteroidClient)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_convenience_execute_agent(self, mock_sdk_api):
        """Test convenience function for execute_agent."""
        # Setup mock
        mock_response = Mock()
        mock_response.execution_id = self.execution_id
        mock_sdk_api.return_value.execute_agent.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        execution_data = {"input": "test"}
        
        # Execute
        result = execute_agent(client, self.agent_id, execution_data)
        
        # Verify
        self.assertEqual(result, self.execution_id)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_convenience_get_execution_status(self, mock_sdk_api):
        """Test convenience function for get_execution_status."""
        # Setup mock
        mock_response = ExecutionStatusResponse(
            execution_id=self.execution_id,
            status=Status.RUNNING
        )
        mock_sdk_api.return_value.get_execution_status.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = get_execution_status(client, self.execution_id)
        
        # Verify
        self.assertEqual(result, mock_response)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_convenience_get_execution_result(self, mock_sdk_api):
        """Test convenience function for get_execution_result."""
        # Setup mock
        test_result = {"output": "test"}
        mock_response = ExecutionResultResponse(
            execution_id=self.execution_id,
            result=test_result,
            error=None,
            status=Status.COMPLETED
        )
        mock_sdk_api.return_value.get_execution_result.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = get_execution_result(client, self.execution_id)
        
        # Verify
        self.assertEqual(result, test_result)
        
    @patch('asteroid_odyssey.client.SDKApi')
    @patch('time.sleep')
    def test_convenience_wait_for_execution_result(self, mock_sleep, mock_sdk_api):
        """Test convenience function for wait_for_execution_result."""
        # Setup mock
        test_result = {"output": "test"}
        
        status_response = ExecutionStatusResponse(
            execution_id=self.execution_id,
            status=Status.COMPLETED
        )
        result_response = ExecutionResultResponse(
            execution_id=self.execution_id,
            result=test_result,
            error=None,
            status=Status.COMPLETED
        )
        
        mock_sdk_api.return_value.get_execution_status.return_value = status_response
        mock_sdk_api.return_value.get_execution_result.return_value = result_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = wait_for_execution_result(client, self.execution_id)
        
        # Verify
        self.assertEqual(result, test_result)
        
    @patch('asteroid_odyssey.client.ExecutionApi')
    def test_convenience_upload_execution_files(self, mock_execution_api):
        """Test convenience function for upload_execution_files."""
        # Setup mock
        mock_response = UploadExecutionFiles200Response(
            message="Files uploaded successfully",
            file_ids=["file-id-1"]
        )
        mock_execution_api.return_value.upload_execution_files.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        files: list = [b"Hello World!"]
        
        # Execute
        result = upload_execution_files(client, self.execution_id, files)
        
        # Verify
        self.assertEqual(result, mock_response)
        
    @patch('asteroid_odyssey.client.SDKApi')
    def test_convenience_get_browser_session_recording(self, mock_sdk_api):
        """Test convenience function for get_browser_session_recording."""
        # Setup mock
        recording_url = "https://example.com/recording.mp4"
        mock_response = BrowserSessionRecordingResponse(recording_url=recording_url)
        mock_sdk_api.return_value.get_browser_session_recording.return_value = mock_response
        
        client = AsteroidClient(self.api_key)
        
        # Execute
        result = get_browser_session_recording(client, self.execution_id)
        
        # Verify
        self.assertEqual(result, recording_url)


class TestEdgeCases(unittest.TestCase):
    """Test suite for edge cases and error conditions."""
    
    def test_empty_api_key(self):
        """Test client initialization with empty API key."""
        # This should still work as the SDK doesn't validate the API key format
        client = AsteroidClient("")
        self.assertIsNotNone(client)
        
    def test_none_api_key(self):
        """Test client initialization with None API key."""
        with self.assertRaises(TypeError):
            AsteroidClient(None)  # type: ignore
            
    @patch('asteroid_odyssey.client.ExecutionApi')
    def test_upload_execution_files_empty_list(self, mock_execution_api):
        """Test file upload with empty file list."""
        # Setup mock
        mock_response = UploadExecutionFiles200Response(
            message="No files uploaded",
            file_ids=[]
        )
        mock_execution_api.return_value.upload_execution_files.return_value = mock_response
        
        client = AsteroidClient("test-key")
        
        # Execute
        result = client.upload_execution_files("test-execution-id", [])
        
        # Verify
        self.assertEqual(result, mock_response)
        mock_execution_api.return_value.upload_execution_files.assert_called_once_with(
            "test-execution-id",
            files=[]
        )
        
    @patch('asteroid_odyssey.client.ExecutionApi')
    def test_upload_execution_files_mixed_types(self, mock_execution_api):
        """Test file upload with mixed file types."""
        # Setup mock
        mock_response = UploadExecutionFiles200Response(
            message="Files uploaded successfully",
            file_ids=["file-id-1", "file-id-2", "file-id-3"]
        )
        mock_execution_api.return_value.upload_execution_files.return_value = mock_response
        
        client = AsteroidClient("test-key")
        
        # Mixed file types
        files = [
            b"Raw bytes content",
            ("named_file.txt", b"Named file content"),
            "String content"
        ]
        
        # Execute
        result = client.upload_execution_files("test-execution-id", files)
        
        # Verify
        self.assertEqual(result, mock_response)
        expected_files = [
            ("file.txt", b"Raw bytes content"),
            ("named_file.txt", b"Named file content"),
            ("file.txt", b"String content")
        ]
        mock_execution_api.return_value.upload_execution_files.assert_called_once_with(
            "test-execution-id",
            files=expected_files
        )


if __name__ == '__main__':
    unittest.main() 