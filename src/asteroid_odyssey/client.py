"""Client wrapper for the generated API client."""

import logging
import os
from typing import Optional
import uuid
from api.generated.asteroid_agents_api_client.client import Client, AuthenticatedClient
from api.generated.asteroid_agents_api_client.models.job import Job
from api.generated.asteroid_agents_api_client.models.job_data import JobData
from api.generated.asteroid_agents_api_client.types import Response
from api.generated.asteroid_agents_api_client.api.agent.run_agent import sync as run_agent_sync
from asteroid_odyssey.exceptions import ApiError

from asteroid_sdk.api.generated.asteroid_api_client.api.run.get_run import sync as get_run_sync
# Logger
logger = logging.getLogger(__name__)

class Odyssey:
    """Wrapper for the generated API client."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None
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
                
        if base_url is None:
            from_env = os.getenv("ASTEROID_AGENTS_API_URL")
            if not from_env:
                # Fall back to the production server
                # TODO replace with the URL
                from_env = "http://34.173.109.7/api/v1"
            base_url = from_env

    def _handle_response(self, response: Response):
        """Handle API response and errors."""
        logger.info(f"Response: {response}")

        return response.parsed

    def start(self, task: str, agent_name: str = "default_web"):
        """Example method using the API client."""
        logger.info(f"Running task: {task}")

        job_data = {
            "task": task
        }

        jd = JobData.from_dict(job_data)

        id = uuid.uuid4()

        try:
            response = run_agent_sync(
                agent_name=agent_name,
                client=self._client,
                body=Job(
                    data=jd
                )
            )
            logger.info(f"Response: {response}")
        except Exception as e:
            logger.error(f"Error running task: {e}")
            raise e

        if response is None:
            raise ApiError("No response from API")

        return self._handle_response(response)

    def get_run(self, run_id: str):
        """Get a run by its ID."""
        return self._handle_response(get_run_sync(client=self._client, run_id=run_id))
