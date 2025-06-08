import subprocess
import time

def print_agent_step(agent_name, message, is_task=False):
    """Prints a formatted step message for an agent."""
    icon = "🤖" if not is_task else "▶️"
    print(f"\n{icon} [{agent_name}]: {message}")
    time.sleep(1)

def run_command(command):
    """Executes a shell command."""
    print(f"   └── Running command: '{command}'")
    time.sleep(0.5)
    # Using capture_output=False to show command output directly in terminal
    subprocess.run(command, shell=True, check=True)

