from .common import print_agent_step, run_command

# --- CATCHPOINT CONFIG (Replace with your actual IDs) ---
CATCHPOINT_PRODUCT_ID = 15330
CATCHPOINT_DIVISION_ID = 1000

def execute(product_name, new_price):
    """The main execution function for the IaCAgent."""
    print_agent_step("IaCAgent", f"Received task: Update infrastructure code for '{product_name}'.", is_task=True)
    
    product_slug = product_name.lower().replace(' ', '-')
    test_url = f"https://www.mysuperstore.com/products/{product_slug}"
    price_string = f"${new_price:.2f}"
    test_script_content = f'go("{test_url}");\\nverifyText("{price_string}");'

    tf_vars_content = f'''
test_name    = "Price Check for {product_name}"
product_id   = {CATCHPOINT_PRODUCT_ID}
division_id  = {CATCHPOINT_DIVISION_ID}
test_script  = "{test_script_content}"
'''
    with open('iac/terraform.tfvars', 'w') as f:
        f.write(tf_vars_content)

    print_agent_step("IaCAgent", "terraform.tfvars generated. Committing change to GitHub...")
    commit_message = f"feat(iac): update monitor for {product_name} to ${new_price}"
    run_command("git add iac/terraform.tfvars")
    run_command(f"git commit -m \"{commit_message}\"")
    print_agent_step("IaCAgent", "Task complete. Reporting SUCCESS.")
    return True

