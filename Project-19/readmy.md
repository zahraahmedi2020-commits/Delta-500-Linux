# Project 19 — Python API Client & Automation

## Overview

Project 19 is a Python-based API client and automation project developed as part of the Delta-500 roadmap.

The project connects to a Flask API, retrieves device information, monitors device status and health, automatically fixes offline devices, and provides interactive tools for filtering, sorting, and searching devices.

The main goal of this project was to practice Python programming together with REST API communication and basic network automation concepts.

## Technologies

* Python 3
* Requests
* REST API
* Flask API
* JSON
* Git & GitHub
* Linux / Ubuntu

## Project Features

### API Client

The client communicates with the Flask API using the `requests` library.

Supported operations include:

* GET — retrieve device data
* PUT — update device information

### Device Monitoring

The project can check device status and identify offline devices.

It also provides health monitoring based on:

* Temperature
* CPU usage
* Memory usage

Health status can be:

* NORMAL
* WARNING
* CRITICAL

### Automatic Fix

The automation checks for offline devices and automatically changes their status to `online`.

The workflow is:

```text
Health Check
     ↓
Detect Offline Devices
     ↓
Auto Fix
     ↓
Health Check Again
     ↓
Check Device Status
     ↓
Automation Report
```

This follows a simple automation principle:

**Check → Act → Recheck → Report**

### Automation Report

After the automation process, the program displays:

* Number of online devices
* Number of offline devices

### Interactive Menu

After the main automation workflow finishes, the user can access additional tools:

```text
1. Show Online Devices
2. Sort by Memory
3. Sort by Memory (Reverse)
4. Find Device by Name
5. Exit
```

These tools allow the user to:

* Filter online devices
* Sort devices by memory usage
* Sort devices in reverse order
* Search for a device by name

## Project Structure

```text
Project-19/
│
└── client.py
```

The main program is implemented in `client.py`.

The program uses a `main()` function as the entry point:

```python
def main():
    run_automation()
    menu()


if __name__ == "__main__":
    main()
```

This structure separates the main automation workflow from the interactive menu.

## What I Learned

During this project, I practiced:

* Python functions
* Lists and dictionaries
* Loops and conditions
* Function parameters and return values
* Working with JSON data
* REST API communication
* Using the `requests` library
* GET and PUT requests
* Filtering data
* Sorting data
* Searching data
* Building an interactive CLI menu
* Basic automation workflow design
* Health monitoring logic
* Git and GitHub workflow
* Running Python projects in Linux

## Automation Design

One of the main concepts learned in this project was separating different responsibilities into functions.

For example:

```text
get_items()
    ↓
Get data from API

check_device_health()
    ↓
Check device health

auto_fix_offline_items()
    ↓
Fix offline devices

automation_report()
    ↓
Report final status

menu()
    ↓
Provide optional tools
```

This makes the program easier to understand, test, and extend.

## Future Improvements

Possible future improvements include:

* Better API error handling
* Handling missing device data
* Adding POST and DELETE operations
