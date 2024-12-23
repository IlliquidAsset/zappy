import json
import os

# Debug log path
DEBUG_LOG_PATH = "zappy/debug_log.json"
VERSION = None  # Placeholder for the current version

def run_with_debug(app_name, app_logic):
    """
    Wrapper to handle app initialization and debugging.
    
    Parameters:
    - app_name (str): The name of the app.
    - app_logic (function): The main logic of the app as a callable function.
    """
    initialize_version(app_name)
    print_debug_info(app_name)
    
    try:
        app_logic()  # Run the main app logic
    except Exception as e:
        print(f"\033[91mError in {app_name}: {e}\033[0m")
    
    print_page_break()

def load_debug_log():
    """Loads the debug log from a file or initializes a new log."""
    if os.path.exists(DEBUG_LOG_PATH):
        with open(DEBUG_LOG_PATH, "r") as file:
            return json.load(file)
    return {}

def save_debug_log(log_data):
    """Saves the debug log to a file."""
    os.makedirs(os.path.dirname(DEBUG_LOG_PATH), exist_ok=True)
    with open(DEBUG_LOG_PATH, "w") as file:
        json.dump(log_data, file, indent=4)

def initialize_version(app_name):
    """Initializes or increments the version number for a specific app."""
    global VERSION
    log_data = load_debug_log()
    if app_name in log_data:
        log_data[app_name] += 1
    else:
        log_data[app_name] = 1
    VERSION = log_data[app_name]
    save_debug_log(log_data)

def print_debug_info(app_name):
    """Prints the debugging information for the app."""
    global VERSION
    print(f"\033[92m[{VERSION:03}] Script started for '{app_name}'.\033[0m")

def print_page_break():
    """Prints a red page break at the end."""
    print("\033[91m" + "-" * 80 + "\033[0m")

# Example usage:
if __name__ == "__main__":
    APP_NAME = "ExampleApp"  # Replace with your app name
    initialize_version(APP_NAME)
    print_debug_info(APP_NAME)

    # Simulated app logic here
    print(f"Running logic for {APP_NAME}...")

    # End script with a page break
    print_page_break()
