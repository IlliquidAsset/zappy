# Zappy - Simple Version Tracking and Logging Utility

Zappy is a lightweight Python utility for tracking app versions and logs, focusing on simplicity, minimal configuration, and clear console output. It automatically increments version counts, tracks logs in a JSON file, and provides readable debug messages.

---

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
  - [run_with_debug](#run_with_debug)
  - [initialize_version](#initialize_version)
  - [print_debug_info](#print_debug_info)
  - [print_page_break](#print_page_break)
- [Example](#example)
- [Configuration](#configuration)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Zappy simplifies version tracking and debugging for Python applications by:
- **Incrementing Version Counts**: Tracks app runs by updating a version count in a JSON file.
- **Debug-Friendly Output**: Logs errors in red, displays version info in green, and adds visual page breaks for clarity.
- **Simple JSON Storage**: Stores logs in a `debug_log.json` file, which can be easily reset or edited.
- **Minimal Dependencies**: Uses only Python’s standard libraries.

---

## Installation

### Prerequisites
- Python 3.6 or higher.

### Steps
1. Clone or download the Zappy repository:
   ```bash
   git clone <repository-url>
   cd zappy
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. Copy `zappy.py` into your project folder or install it as a local package:
   ```bash
   cp zappy.py /path/to/your/project
   ```

4. Install dependencies if your script uses libraries like pandas or xlwings (Zappy itself has no external dependencies).

---

## Usage

### Quick Start
1. Import Zappy’s functions:
   ```python
   from zappy import run_with_debug, initialize_version, print_debug_info, print_page_break
   ```

2. Define your main application logic:
   ```python
   def main_logic():
       # Your app’s core logic
       print("Hello from Zappy!")
   ```

3. Use `run_with_debug` in the script’s entry point:
   ```python
   if __name__ == "__main__":
       run_with_debug("MyZappyApp", main_logic)
   ```

4. Run the script:
   ```bash
   python your_script.py
   ```

---

## API Reference

### run_with_debug(app_name, app_logic)
- **Purpose**: Initializes/increments the version count for `app_name`, prints debug info, runs `app_logic`, and logs errors if they occur.
- **Parameters**:
  - `app_name` (str): Name of your application.
  - `app_logic` (function): The main function containing your application logic.
- **Behavior**:
  - Increments the app’s version in the JSON log.
  - Executes `app_logic()`.
  - Prints errors in red and adds a red page break at the end.

### initialize_version(app_name)
- **Purpose**: Loads or initializes the debug log and increments the version count for `app_name`.
- **Returns**: The current version number for the app.

### print_debug_info(app_name)
- **Purpose**: Displays the current app name and version in green for easy identification.

### print_page_break()
- **Purpose**: Adds a red dashed line in the console output for better readability.

---

## Example

Here’s a minimal example:

```python
from zappy import run_with_debug

def my_main_logic():
    print("Zappy is running!")

if __name__ == "__main__":
    run_with_debug("MyAwesomeApp", my_main_logic)
```

When executed:
1. Zappy checks or creates `debug_log.json`.
2. Increments the version for "MyAwesomeApp".
3. Prints the version info and app name.
4. Runs `my_main_logic()`.
5. Prints a red page break at the end.

---

## Configuration

### DEBUG_LOG_PATH
- Default: `zappy/debug_log.json`
- Change this in `zappy.py` if you want logs stored elsewhere.

### VERSION
- A global variable that holds the current version in memory during runtime.

---

## FAQ

### How do I reset the version number?
- Edit or delete the corresponding entry in `debug_log.json`.

### Can multiple scripts share the same debug log?
- Yes. Each `app_name` gets its own version entry. To separate logs, modify the `DEBUG_LOG_PATH` for each script.

### What about concurrency?
- Zappy is designed for single-user, single-process usage. If multiple processes access the log simultaneously, consider adding file-locking logic.

---

## Contributing

Contributions are welcome! If you have ideas or find issues, open a pull request or an issue on GitHub.

---

## License

Zappy is free to use and modify. See the repository for license details.
