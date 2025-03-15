from typing import Optional, Dict, Any, List, Union, Callable, Tuple
from uuid import UUID
import logging
import time
from enum import Enum
import os

from .api.generated.agents.asteroid_agents_api_client.models import (
    CreateWorkflowRequest,
    WorkflowExecution,
    ExecutionStatus,
    Execution
)
from .api.generated.agents.asteroid_agents_api_client.api_client import ApiClient
from .api.generated.agents.asteroid_agents_api_client.configuration import Configuration
from .api.generated.agents.asteroid_agents_api_client.api.execution_api import ExecutionApi
from .api.generated.agents.asteroid_agents_api_client.api.agent_api import AgentApi
from .api.generated.agents.asteroid_agents_api_client.api.default_api import DefaultApi
from .api.generated.agents.asteroid_agents_api_client.api.workflow_api import WorkflowApi

logger = logging.getLogger(__name__)

class ExecutionTerminalState(Enum):
    """Terminal states for an execution"""
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    ERROR = "error"

agent_name = "iris"

class ExecutionResult:
    """Wrapper class for execution results"""
    def __init__(self, execution: Execution):
        self.execution_id = execution.id
        self.status = execution.status
        self.result = execution.result
        self.error = execution.error if hasattr(execution, 'error') else None
        self.created_at = execution.created_at
        self.completed_at = execution.completed_at if hasattr(execution, 'completed_at') else None

class AsteroidClient:
    """
    A high-level client for interacting with the Asteroid API.
    """
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        verify_ssl: bool = True
    ):
        """
        Initialize the Asteroid client.

        Args:
            api_key: API key for authentication. If not provided, will look for ASTEROID_API_KEY env var
            base_url: Base URL for the API. Defaults to production URL if not specified
            verify_ssl: Whether to verify SSL certificates. Defaults to True
        """
        self.api_key = api_key or os.getenv("ASTEROID_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key is required. Either pass it directly or set ASTEROID_API_KEY environment variable"
            )

        self.base_url = base_url or "https://api.asteroid.ai/v1"
        
        # Initialize configuration
        self.config = Configuration(
            host=self.base_url,
            api_key={"ApiKeyAuth": self.api_key},
            verify_ssl=verify_ssl
        )
        
        # Initialize API client
        self.client = ApiClient(configuration=self.config)

    def get_agents(self) -> List[Dict[str, Any]]:
        """
        Get list of available agents.
        
        Returns:
            List of agent details
        """
        try:
            return AgentApi(self.client).get_agents()
        except Exception as e:
            logger.error(f"Failed to get agents: {str(e)}")
            raise

    def create_workflow(
        self, 
        workflow_name: str,
        start_url: str,
        prompt: str
    ) -> str:
        """
        Create a new workflow for an agent.

        Args:
            agent_name: Name of the agent to create workflow for
            workflow_config: Configuration for the workflow

        Returns:
            Workflow ID
        """
        result_schema = {
            "properties": {
                "explanation": {
                    "description": "Detailed explanation of the result",
                    "type": "string"
                },
                "success": {
                    "description": "Whether the operation was successful",
                    "type": "boolean"
                }
            },
            "required": [
                "explanation",
                "success"
            ],
            "type": "object"
        }

        try:
            request = CreateWorkflowRequest(
                name=workflow_name,
                result_schema=result_schema,
                fields={"workflow_name": workflow_name, "start_url": start_url},
                prompts=[prompt],
                provider="openai"
            )

            return DefaultApi(self.client).create_workflow(
                agent_name=agent_name,
                create_workflow_request=request
            )
        except Exception as e:
            logger.error(f"Failed to create workflow: {str(e)}")
            raise

    def execute_workflow(
        self,
        workflow_id: UUID,
        execution_params: Dict[str, Any]
    ) -> str:
        """
        Execute an existing workflow.

        Args:
            workflow_id: ID of workflow to execute
            execution_params: Parameters for workflow execution

        Returns:
            Execution ID
        """
        try:
            return WorkflowApi(self.client).execute_workflow(
                workflow_id=workflow_id,
                request_body=execution_params
            )
        except Exception as e:
            logger.error(f"Failed to execute workflow: {str(e)}")
            raise

    def get_workflow_executions(self) -> List[WorkflowExecution]:
        """
        Get list of workflow executions.

        Returns:
            List of workflow executions
        """
        try:
            return WorkflowApi(self.client).get_agent_workflow_executions(
                agent_name=agent_name
            )
        except Exception as e:
            logger.error(f"Failed to get workflow executions: {str(e)}")
            raise

    def get_execution(self, execution_id: str) -> Execution:
        """
        Get the full execution details.

        Args:
            execution_id: ID of the execution to retrieve

        Returns:
            Execution object with full details
        """
        try:
            return ExecutionApi(self.client).get_execution(id=execution_id)
        except Exception as e:
            logger.error(f"Failed to get execution: {str(e)}")
            raise

    def get_execution_status(self, execution_id: str) -> ExecutionStatus:
        """
        Get the current status of an execution.

        Args:
            execution_id: ID of the execution to check

        Returns:
            Current execution status
        """
        execution = self.get_execution(execution_id)
        return execution.status

    def get_execution_result(self, execution_id: str) -> ExecutionResult:
        """
        Get the result of an execution.

        Args:
            execution_id: ID of the execution to get results for

        Returns:
            ExecutionResult object containing status, result, and other metadata

        Raises:
            ValueError: If execution doesn't exist or hasn't completed
        """
        execution = self.get_execution(execution_id)
        return ExecutionResult(execution)

    def wait_for_execution(
        self,
        execution_id: str,
        polling_interval: float = 1.0,
        timeout: Optional[float] = None,
        status_callback: Optional[Callable[[ExecutionStatus], None]] = None
    ) -> ExecutionStatus:
        """
        Wait for an execution to reach a terminal state.

        Args:
            execution_id: ID of the execution to wait for
            polling_interval: Time in seconds between status checks
            timeout: Maximum time in seconds to wait. None means wait indefinitely
            status_callback: Optional callback function that will be called with each status update

        Returns:
            Final execution status

        Raises:
            TimeoutError: If timeout is reached before execution reaches terminal state
            ValueError: If execution_id is invalid
        """
        start_time = time.time()
        last_status = None

        while True:
            # Check if we've exceeded timeout
            if timeout and (time.time() - start_time) > timeout:
                raise TimeoutError(f"Execution {execution_id} did not complete within {timeout} seconds")

            # Get current status
            current_status = self.get_execution_status(execution_id)

            # Call status callback if status has changed
            if status_callback and current_status != last_status:
                status_callback(current_status)
            last_status = current_status

            # Check if we've reached a terminal state
            if current_status.value.lower() in [state.value for state in ExecutionTerminalState]:
                return current_status

            # Wait before next check
            time.sleep(polling_interval)

    def wait_for_execution_result(
        self,
        execution_id: str,
        polling_interval: float = 1.0,
        timeout: Optional[float] = None,
        status_callback: Optional[Callable[[ExecutionStatus], None]] = None
    ) -> ExecutionResult:
        """
        Wait for an execution to complete and get its result.

        Args:
            execution_id: ID of the execution to wait for
            polling_interval: Time in seconds between status checks
            timeout: Maximum time in seconds to wait. None means wait indefinitely
            status_callback: Optional callback function that will be called with each status update

        Returns:
            ExecutionResult object containing final status, result, and other metadata

        Raises:
            TimeoutError: If timeout is reached before execution completes
            ValueError: If execution_id is invalid
        """
        # Wait for execution to reach terminal state
        final_status = self.wait_for_execution(
            execution_id=execution_id,
            polling_interval=polling_interval,
            timeout=timeout,
            status_callback=status_callback
        )

        # Get the final result
        result = self.get_execution_result(execution_id)

        # If execution failed, include error information in logs
        if final_status.value.lower() in [ExecutionTerminalState.FAILED.value, ExecutionTerminalState.ERROR.value]:
            logger.error(f"Execution {execution_id} failed with error: {result.error}")

        return result

    def execute_workflow_and_get_result(
        self,
        workflow_id: UUID,
        execution_params: Dict[str, Any],
        polling_interval: float = 1.0,
        timeout: Optional[float] = None,
        status_callback: Optional[Callable[[ExecutionStatus], None]] = None
    ) -> ExecutionResult:
        """
        Execute a workflow and wait for its result.

        Args:
            workflow_id: ID of workflow to execute
            execution_params: Parameters for workflow execution
            polling_interval: Time in seconds between status checks
            timeout: Maximum time in seconds to wait. None means wait indefinitely
            status_callback: Optional callback function that will be called with each status update

        Returns:
            ExecutionResult object containing final status, result, and other metadata
        """
        # Start execution
        execution_id = self.execute_workflow(workflow_id, execution_params)

        # Wait for result
        return self.wait_for_execution_result(
            execution_id=execution_id,
            polling_interval=polling_interval,
            timeout=timeout,
            status_callback=status_callback
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
