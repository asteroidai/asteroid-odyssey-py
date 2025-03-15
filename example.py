import sys
print(sys.path)

# Try importing and check its location
import asteroid_odyssey
print(asteroid_odyssey.__file__)

# from uuid import UUID
# from asteroid_odyssey.api.generated.agents.asteroid_agents_api_client.models.execution_status import ExecutionStatus
# from asteroid_odyssey.client import AsteroidClient, ExecutionTerminalState

# # Initialize client
# client = AsteroidClient(api_key="your-api-key")

# # Example status callback
# def log_status(status: ExecutionStatus):
#     print(f"Execution status updated: {status}")

# try:
#     # First, list available agents
#     agents = client.get_agents()
#     print("Available agents:", [agent["name"] for agent in agents])
    
#     # Create a new workflow for a specific agent
#     workflow_config = {
#         "name": "My Example Workflow",
#         "description": "A workflow created via the API",
#         "config": {
#             # Add any agent-specific configuration here
#             "parameter1": "value1",
#             "parameter2": "value2"
#         }
#     }
    
#     workflow_id = client.create_workflow(
#         agent_name="example-agent",  # Replace with actual agent name
#         workflow_config=workflow_config
#     )
#     print(f"Created workflow with ID: {workflow_id}")

#     # Execute workflow and wait for result
#     result = client.execute_workflow_and_get_result(
#         workflow_id=UUID(workflow_id),
#         execution_params={
#             # Add any execution-specific parameters here
#             "input": "example input",
#             "options": {
#                 "option1": "value1"
#             }
#         },
#         polling_interval=2.0,  # Check every 2 seconds
#         timeout=300,  # Wait up to 5 minutes
#         status_callback=log_status
#     )
    
#     # Handle the result
#     print(f"\nExecution Summary:")
#     print(f"Completed at: {result.completed_at}")
#     print(f"Final status: {result.status}")
    
#     if result.status.value.lower() == ExecutionTerminalState.COMPLETED.value:
#         print(f"Result: {result.result}")
#     elif result.error:
#         print(f"Error occurred: {result.error}")

# except TimeoutError:
#     print("Execution timed out")
# except Exception as e:
#     print(f"Error during execution: {str(e)}")
