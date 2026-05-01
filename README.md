# Python QA Projects

This repository showcases my hands-on Python QA automation practice, including REST API validation, backend test utilities, configuration handling, JSON data validation, file upload testing, authentication, and MySQL connectivity.

The project includes foundational Python exercises plus a cleaner backend QA automation framework that works with REST APIs, configuration files, environment variables, JSON data, file uploads, redirects, timeouts, authentication, and MySQL connectivity.

## What This Project Demonstrates

- Python fundamentals: loops, lists, dictionaries, functions, OOP, and logic practice
- API automation using `requests`
- JSON parsing and payload construction
- API authentication using environment variables
- Centralized test configuration with `.ini` files and `configparser`
- Safer secret handling with `.env` and `.env.example`
- File upload and multipart request examples
- Basic backend/database automation with MySQL connector
- Organized API learning scripts grouped by backend testing topic
- VS Code launch configuration for running the current Python file

## Project Structure

```text
.
├── Fundamentals/
│   └── Python practice exercises
├── Python_QA_Framework/
│   ├── config/
│   │   └── Shared API and SQL endpoints
│   ├── data/
│   │   ├── JSON test data
│   │   └── files used for upload examples
│   ├── database/
│   │   ├── schema.sql
│   │   └── MySQL example scripts
│   ├── payloads/
│   │   └── Reusable API request payload builders
│   ├── utilities/
│       ├── config.py
│       ├── db_utils.py
│       └── api_resources.py
│   └── tests/
│       ├── auth/
│       ├── file_upload/
│       ├── http_behaviour/
│       ├── json_data/
│       └── library/
└── .vscode/
    └── Shared launch configuration for running the current Python file
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the main packages used by the backend automation examples:

```bash
pip install -r requirements.txt
```

Create a local environment file from the example:

```bash
cp Python_QA_Framework/.env.example Python_QA_Framework/.env
```

Then add your local credentials to `Python_QA_Framework/.env`:

```text
GitHub_API_username=
GitHub_API_token=
mysql_username=
mysql_password=
```

The real `.env` file is ignored by Git so credentials are not committed.

## Running Files

In VS Code, open any runnable Python file and use the play button. The shared `.vscode/launch.json` runs the current file from the workspace root.

You can also run individual learning scripts from the terminal:

```bash
python Python_QA_Framework/tests/json_data/test_json_parsing.py
```

As the framework grows, pytest-style tests can be run from the same organized folders:

```bash
pytest Python_QA_Framework/tests
```

Some examples call public training APIs or require local MySQL credentials, so results can depend on network access, API availability, and your local database setup.

## Current Focus

I am continuing to build this repository toward a more complete QA automation portfolio, including reusable test utilities, stronger API validation patterns, cleaner pytest fixtures, reporting, CI, and future Playwright-based UI automation.
