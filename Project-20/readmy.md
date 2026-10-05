# Project 20 - Python Network Device Manager

## Overview

Project 20 is a Python-based Network Device Manager designed to practice
Object-Oriented Programming (OOP) and device management concepts for
Network Automation.

The project manages a collection of network device objects and provides
operations such as adding, finding, updating, removing, displaying, and
filtering devices.

This project is a bridge between the Python/API automation concepts learned
in previous projects and the real network automation tasks that will be
introduced in the next projects.

---

## Project Goals

- Practice Object-Oriented Programming in Python
- Create and manage network device objects
- Separate data models from management logic
- Manage multiple devices using a central manager
- Practice validation and error handling
- Practice filtering and searching devices
- Prepare for real network automation and SSH-based management

---

## Device Information

Each device contains the following information:

- IP Address
- Name
- Device Type
- Model
- Serial Number
- Status
- New Status

Example device types:

- Router
- Switch

---

## Project Structure

```text
Project-20/
│
├── device.py
├── device_manager.py
├── menu.py
└── README.md