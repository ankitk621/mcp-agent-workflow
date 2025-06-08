import sys
from dotenv import load_dotenv
from agents import planner_agent, code_agent, iac_agent, deploy_agent
from agents.common import print_agent_step

def main():
    """The main entry point for the AI Agent system."""
    load_dotenv() # Load variables from .env file

    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your natural language command>\"")
        sys.exit(1)
    
    user_command = sys.argv[1]
    
    # 1. Start with the PlannerAgent to create a plan
    plan = planner_agent.execute(user_command)
    product_name = plan['productName']
    new_price = plan['newPrice']
    
    print_agent_step("Orchestrator", "Plan received. Dispatching tasks to agents...")
    
    # 2. Dispatch tasks to Code and IaC agents
    code_success = code_agent.execute(product_name, new_price)
    iac_success = iac_agent.execute(product_name, new_price)
    
    # 3. If code and IaC agents succeed, dispatch to Deploy agent
    if code_success and iac_success:
        print_agent_step("Orchestrator", "Code and IaC agents succeeded. Dispatching to DeployAgent...")
        deploy_agent.execute()
        print("\n🎉 AI agent workflow finished successfully!")
    else:
        print("\n❌ AI agent workflow failed. Please check agent logs.")

if __name__ == "__main__":
    main()

