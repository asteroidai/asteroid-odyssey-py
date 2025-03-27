import sys
from uuid import UUID
from asteroid_odyssey.api.generated.asteroid_agents_api_client.models.execution_status import ExecutionStatus
from asteroid_odyssey.client import AsteroidClient, ExecutionTerminalState
from asteroid_odyssey.api.generated.asteroid_agents_api_client.models.workflow_execution_request import WorkflowExecutionRequest

# Constants
API_KEY = "astKVDBl9BSNoMqdYVh34vbiqYOMANln7oolmu4MNn4N5r2swOVldET0uyGuX8Le"
WORKFLOW_NAME = "Commercial auto insurance application"
START_URL = "https://www.primeis.com/forms/commercial-auto-application/"

WORKFLOW_PROMPT = """
You are extremely advanced AI browser agent. 
Your task is to fill in the data to a form {{.DATA}}. 
Escalate to human before submitting the form
""".strip()

FORM_DATA = """
General Information:
Business Name: Acme Corporation
Applicant Name: John Doe
Mailing Address: 123 Main Street, Springfield, IL 62701
County: Sangamon
Email: john.doe@example.com
Business Telephone: 555-123-4567
Fax: 555-765-4321
Physical Location: 123 Main Street, Springfield, IL
Population within 50 miles: 500000
Other Business Names: Acme Inc., Acme Widgets
Contact Person: Jane Smith
Producer's Name: Alice Johnson

Business Activities Description:
Manufacturing and distribution of high-quality widgets at multiple locations.

Business Type: Corporation
Year Established: 1995

Owners Experience:
- John Doe: 20 years experience
- Mary Doe: 15 years experience

Managers Experience:
- Jane Smith: 10 years experience
- Bob Johnson: 8 years experience

Annual Payroll: $1,000,000
Total Employees: 50
- Full-time: 40
- Part-time: 10
""".strip()

def log_status(status: ExecutionStatus):
    """Callback function to log execution status updates."""
    print(f"Execution status updated: {status}")

def main():
    # Initialize client
    client = AsteroidClient(api_key=API_KEY)

    try:
        # List available agents
        agents = client.get_agents()
        print("Available agents:", [agent.name for agent in agents])

        # Create workflow
        workflow_id = client.create_workflow(
            workflow_name=WORKFLOW_NAME,
            start_url=START_URL,
            prompt=WORKFLOW_PROMPT
        )
        print(f"Created workflow with ID: {workflow_id}")

        # Execute workflow
        execution_params = {"DATA": FORM_DATA}
        result = client.execute_workflow_and_get_result(
            workflow_id=UUID(workflow_id),
            execution_params=execution_params,
            polling_interval=2.0,  # Check every 2 seconds
            timeout=600,  # Wait up to 10 minutes
            status_callback=log_status
        )
        
        # Print execution summary
        print(f"\nExecution Summary:")
        print(f"Completed at: {result.completed_at}")
        print(f"Final status: {result.status}")
        print(f"Result: {result.result}")

    except TimeoutError:
        print("Execution timed out")
    except Exception as e:
        print(f"Error during execution: {str(e)}")

if __name__ == "__main__":
    main()
