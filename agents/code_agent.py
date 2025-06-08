import json
from .common import print_agent_step, run_command

def execute(product_name, new_price):
    """The main execution function for the CodeAgent."""
    print_agent_step("CodeAgent", f"Received task: Update application code for '{product_name}'.", is_task=True)
    
    # Read, modify, and write the application data file
    with open('website/products.json', 'r+') as f:
        products = json.load(f)
        product_found = False
        for p in products:
            if p['name'].lower() == product_name.lower():
                p['price'] = new_price
                product_found = True
                break
        
        if not product_found:
             print(f"❌ CodeAgent Error: Product '{product_name}' not found.")
             return False

        f.seek(0)
        json.dump(products, f, indent=2)
        f.truncate()

    print_agent_step("CodeAgent", "products.json updated. Committing change to GitHub...")
    commit_message = f"feat(app): update price for {product_name} to {new_price}"
    run_command("git add website/products.json")
    run_command(f"git commit -m \"{commit_message}\"")
    print_agent_step("CodeAgent", "Task complete. Reporting SUCCESS.")
    return True

