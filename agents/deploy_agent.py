from .common import print_agent_step, run_command

def execute():
    """The main execution function for the DeployAgent."""
    print_agent_step("DeployAgent", "Received task: Deploy all pending changes.", is_task=True)
    
    print_agent_step("DeployAgent", "Pulling latest changes from GitHub...")
    run_command("git pull origin main")
    
    print_agent_step("DeployAgent", "Pushing all committed changes to GitHub...")
    run_command("git push origin main")
    
    print_agent_step("DeployAgent", "Executing Terraform to apply infrastructure changes...")
    run_command("terraform -chdir=iac init -quiet")
    run_command(f"terraform -chdir=iac apply -var-file=../iac/terraform.tfvars -auto-approve")
    
    print_agent_step("DeployAgent", "Deployment to Catchpoint complete. Reporting SUCCESS.")
    return True
