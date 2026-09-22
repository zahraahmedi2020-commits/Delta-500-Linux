# Project 18 — Flask REST API

## Overview

Project 18 is a Flask-based REST API project developed as part of the Delta-500 roadmap.

The project provides an API for storing and managing device information. It was created to practice backend development, REST API concepts, JSON data exchange, and Linux-based Python development.

The API can receive, return, update, and delete device data.

## Technologies

* Python 3
* Flask
* REST API
* JSON
* curl
* Linux / Ubuntu
* Git & GitHub
* Python Virtual Environment (`venv`)

## Project Features

### Device Data

The API stores device information using a simple structure:

```text
id
name
status
```

Example:

```json
{
    "id": 1,
    "name": "Server",
    "status": "online"
}
```

### API Endpoints

The project supports the following operations:

| Method | Endpoint     | Purpose                   |
| ------ | ------------ | ------------------------- |
| GET    | `/data`      | Retrieve device data      |
| POST   | `/data`      | Add a new device          |
| PUT    | `/data/<id>` | Update an existing device |
| DELETE | `/data/<id>` | Delete a device           |

### GET

Returns the current device data from the API.

### POST

Receives JSON data and adds a new device to the device list.

### PUT

Searches for a device by its ID and updates its information.

If the requested ID does not exist, the API returns a message indicating that the device was not found.

### DELETE

Searches for a device by its ID and removes it from the list.

If the requested ID does not exist, the API returns a device-not-found message.

## Example API Data

The project uses devices such as:

```text
Server
Router
Switch
```

with their corresponding status values such as:

```text
online
offline
```

## Running the Project

Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Flask:

```bash
pip install flask
```

Run the Flask application:

```bash
python app.py
```

The API runs locally at:

```text
http://127.0.0.1:5000
```

## Testing with curl

### GET

```bash
curl http://127.0.0.1:5000/data
```

### POST

```bash
curl -X POST http://127.0.0.1:5000/data \
-H "Content-Type: application/json" \
-d '{"id":3,"name":"Switch","status":"online"}'
```

### PUT

```bash
curl -X PUT http://127.0.0.1:5000/data/2 \
-H "Content-Type: application/json" \
-d '{"name":"Main Switch","status":"offline"}'
```

### DELETE

```bash
curl -X DELETE http://127.0.0.1:5000/data/2
```

## What I Learned

During this project, I practiced:

* Flask basics
* REST API concepts
* API endpoints
* HTTP methods
* GET, POST, PUT, and DELETE
* JSON data
* `request.json`
* URL parameters
* Searching for an item by ID
* Updating and deleting data
* Testing APIs with curl
* Python virtual environments
* Flask development in Linux
* Debugging API errors
* Git and GitHub workflow

## CRUD Concept

This project helped me understand the basic CRUD model:

```text
Create → POST
Read   → GET
Update → PUT
Delete → DELETE
```

These operations form the foundation of many API-based applications.

## Project Structure

```text
Project-18/
│
├── app.py
├── api-test.js
├── index.html
├── venv/
└── __pycache__/
```

The virtual environment and Python cache files are excluded from Git using `.gitignore`.

## Future Improvements

Possible future improvements include:

* Persistent database storage
* Better API error handling
* Input validation
* Authentication
* Logging
* More REST endpoints
* Connecting the API to a frontend application
* Connecting the API to a Python automation client

## Connection to Project 19

Project 18 provides the API that was later used by **Project 19 — Python API Client & Automation**.

The relationship between the two projects is:

```text
Project 18
Flask REST API
      ↓
     HTTP
      ↓
Project 19
Python API Client
      ↓
Automation
```

This created a practical foundation for moving from backend/API development toward Python-based automation.

## Project Status

**Status: Completed ✅**
