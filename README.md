.----------------------------------------------------------------------------.
|                              ZAPPY README                                 |
'----------------------------------------------------------------------------'

Zappy is a lightweight Python utility for tracking app versions and logs,
focusing on simplicity, minimal configuration, and clear console output. 
It increments a version count each time you run your script, prints useful 
debug information, and neatly captures errors.

--------------------------------------------------------------------------------
TABLE OF CONTENTS
--------------------------------------------------------------------------------
1. Overview
2. Installation
3. Usage
4. API Reference
   - run_with_debug
   - initialize_version
   - print_debug_info
   - print_page_break
5. Example
6. Configuration
7. FAQ
8. Contributing
9. License

--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------
• Increment Version Counts: Each time your app or script runs, zappy increases
  its version count, storing it in a JSON file.
• Debug-Friendly Output: Logs errors in red, prints version info in green,
  and adds a red line “page break” for readability.
• Simple JSON Storage: Uses a single debug_log.json file for version data,
  making it easy to edit or reset if needed.
• Minimal Dependencies: Works with Python’s standard libraries—no extra 
  installs needed (unless your main script does).

--------------------------------------------------------------------------------
2. INSTALLATION
--------------------------------------------------------------------------------
1) Download or clone the zappy repository into your project folder.
2) (Optional) Activate a Python virtual environment.
3) Copy zappy.py into your Python path or install it as a local package, 
   depending on your needs.
4) (Optional) Install additional libraries like pandas, xlwings, etc., 
   if your main script uses them.

--------------------------------------------------------------------------------
3. USAGE
--------------------------------------------------------------------------------
1) Import what you need:
   from zappy import run_with_debug, initialize_version, print_debug_info, print_page_break

2) Define a main function that contains your script’s primary logic:
   def main_logic():
       # Your code here
       pass

3) Wrap that logic with run_with_debug in your script’s entry point:
   if __name__ == "__main__":
       run_with_debug("MyZappyApp", main_logic)

4) Run your script from the command line or your IDE. 
   - zappy will create or update zappy/debug_log.json with version info.
   - Look for color-coded console messages and a page break at the end.

--------------------------------------------------------------------------------
4. API REFERENCE
--------------------------------------------------------------------------------
(A) run_with_debug(app_name, app_logic)
    • Initializes or increments the version count for app_name.
    • Prints version/app name in the console.
    • Executes app_logic(), catching errors and printing them in red.
    • Prints a final page break in red.

(B) initialize_version(app_name)
    • Loads or creates a debug log (JSON).
    • Increments the version for app_name or sets to 1 if not found.
    • Updates a global VERSION variable for reference.

(C) print_debug_info(app_name)
    • Prints the current version and app name in green for easy identification.

(D) print_page_break()
    • Prints a red dashed line in the console for readability.

--------------------------------------------------------------------------------
5. EXAMPLE
--------------------------------------------------------------------------------
from zappy import run_with_debug

def my_main_logic():
    print("Hello from my_main_logic!")

if __name__ == "__main__":
    run_with_debug("MyAwesomeApp", my_main_logic)

When executed:
• zappy checks/creates debug_log.json
• Increments the version for "MyAwesomeApp"
• Prints debug info
• Runs my_main_logic()
• Prints a red page break at the end

--------------------------------------------------------------------------------
6. CONFIGURATION
--------------------------------------------------------------------------------
• DEBUG_LOG_PATH (in zappy.py): The path where version logs are stored. 
  Defaults to "zappy/debug_log.json".
• VERSION: A global variable that holds the current version in memory 
  during runtime.

--------------------------------------------------------------------------------
7. FAQ
--------------------------------------------------------------------------------
Q: How do I reset the version number?
A: Remove or edit the entry for your app in zappy/debug_log.json.

Q: Can multiple scripts share the same debug log?
A: Yes. Each app_name gets its own version number entry. If you want them 
   separate, point them to different debug logs.

Q: What if I need concurrency?
A: zappy is designed for single-user, single-process usage. For concurrency,
   you might need additional locking logic to avoid collisions in the JSON file.

--------------------------------------------------------------------------------
8. CONTRIBUTING
--------------------------------------------------------------------------------
Pull requests, bug reports, and suggestions are welcome! Please open an issue
or PR in the GitHub repository to discuss changes or improvements.

--------------------------------------------------------------------------------
9. LICENSE
--------------------------------------------------------------------------------
zappy is provided for free use and modification. Check the repository for 
license details.

