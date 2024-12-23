import json
import os

# File to store debug version info in JSON format
DEBUG_LOG_PATH = "zappy/debug_log.json"

# Global variable for tracking the current version number
VERSION = None

def run_with_debug(app_name, app_logic):
    """
    Main wrapper to handle app initialization and debugging.
    
    1. Initializes or increments the version.
    2. Prints debug info (version and app name).
    3. Executes the core app logic.
    4. Catches and displays any errors.
    5. Prints a visual page break for clarity.
    """
    initialize_version(app_name)
    print_debug_info(app_name)

    try:
        app_logic()  # Run the main app logic
    except Exception as e:
        print(f"\033[91mError in {app_name}: {e}\033[0m")

    print_page_break()

def load_debug_log():
    """
    Loads the debug log (which stores version numbers per app) from disk.
    Returns an empty dict if the file doesn't exist.
    """
    if os.path.exists(DEBUG_LOG_PATH):
        with open(DEBUG_LOG_PATH, "r") as file:
            return json.load(file)
    return {}

def save_debug_log(log_data):
    """
    Saves the debug log dictionary to disk as JSON.
    Ensures the 'zappy' directory exists if needed.
    """
    os.makedirs(os.path.dirname(DEBUG_LOG_PATH), exist_ok=True)
    with open(DEBUG_LOG_PATH, "w") as file:
        json.dump(log_data, file, indent=4)

def initialize_version(app_name):
    """
    Reads the debug log and increments the version for the specified app,
    or sets it to 1 if it's not found. Then updates the global VERSION.
    """
    global VERSION
    log_data = load_debug_log()

    if app_name in log_data:
        log_data[app_name] += 1
    else:
        log_data[app_name] = 1

    VERSION = log_data[app_name]
    save_debug_log(log_data)

def print_debug_info(app_name):
    """
    Prints the current version and app name in a visible format
    to identify which script and version are running.
    """
    global VERSION
    print(f"\033[92m[{VERSION:03}] Script started for '{app_name}'.\033[0m")

def print_page_break():
    """
    Prints a visual divider in red (e.g., at the end of an app run).
    """
    print("\033[91m" + "-" * 80 + "\033[0m")

# Example usage when running this file directly
if __name__ == "__main__":
    APP_NAME = "ExampleApp"

    initialize_version(APP_NAME)
    print_debug_info(APP_NAME)

    # Placeholder for the app's main logic
    print(f"Running logic for {APP_NAME}...")

    # Print a page break to mark the end of the run
    print_page_break()
