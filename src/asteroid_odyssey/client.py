"""Client wrapper for the generated API client."""

import logging
import os
from typing import Optional
from api.generated.asteroid_agents_api_client.client import Client, AuthenticatedClient
from api.generated.asteroid_agents_api_client.models.job import Job
from api.generated.asteroid_agents_api_client.models.job_data import JobData
from api.generated.asteroid_agents_api_client.types import Response
from api.generated.asteroid_agents_api_client.api.agent.run_agent import sync as run_agent_sync
from asteroid_odyssey.exceptions import ApiError

# Logger

logger = logging.getLogger(__name__)

class AsteroidClient:
    """Wrapper for the generated API client."""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "http://34.173.109.7/api/v1"
    ):
        """Initialize the client.
        
        Args:
            api_key: Optional API key for authentication
            base_url: Base URL for the API
        """
        if api_key:
            self._client = Client(
                base_url=base_url,
                verify_ssl=False,
                headers={"X-Asteroid-Agents-Api-Key": f"{api_key}"}
            )
        else:
            # Try to get the API key from the environment
            api_key = os.getenv("ASTEROID_API_KEY")
            if not api_key:
                raise ApiError("Asteroid API key is required, please set the ASTEROID_API_KEY environment variable. You can get one from https://platform.asteroid.com/")

    def _handle_response(self, response: Response):
        """Handle API response and errors."""
        if not response.is_success:
            raise ApiError(
                f"API request failed: {response.status_code}",
                status_code=response.status_code,
                response=response.content
            )
        return response.parsed

    def run(self, task: str):
        """Example method using the API client."""
        logger.info(f"Running task: {task}")

        job_data = {
            "task": task
        }

        jd = JobData.from_dict(job_data)

        try:
            response = run_agent_sync(
                agent_name="default_web",
                client=self._client,
                body=Job(
                    id="test",
                    data=jd
                )
            )
        except Exception as e:
            logger.error(f"Error running task: {e}")
            raise e

        if response is None:
            raise ApiError("No response from API")

        return self._handle_response(response)
