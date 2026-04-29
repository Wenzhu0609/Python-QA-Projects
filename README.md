# Python QA Projects

This repository documents my progress building Python skills for Software Quality Assurance, API testing, backend automation, and test framework development.

The project currently includes foundational Python exercises plus a reorganized backend automation package that works with REST APIs, configuration files, environment variables, JSON data, file uploads, redirects, timeouts, and MySQL connectivity.

## What This Project Demonstrates

- Python fundamentals: loops, lists, dictionaries, functions, OOP, and logic practice
- API automation using `requests`
- JSON parsing and payload construction
- API authentication using environment variables
- Centralized test configuration with `.ini` files and `configparser`
- Safer secret handling with `.env` and `.env.example`
- File upload and multipart request examples
- Basic backend/database automation with MySQL connector
- Pytest-style test organization for API checks
- VS Code launch configuration for running the current Python file

## Project Structure

```text
.
├── Fundamentals/
│   └── Python practice exercises
├── Python_Back_End_Automation/
│   ├── api/
│   │   └── API request, payload, authentication, and validation examples
│   ├── data/
│   │   ├── JSON test data
│   │   └── files used for upload examples
│   ├── database/
│   │   └── MySQL connection and query examples
│   ├── tests/
│   │   └── API redirect and timeout checks
│   └── utilities/
│       └── Shared configuration and API resource helpers
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
pip install requests python-dotenv mysql-connector-python pytest
```

Create a local environment file from the example:

```bash
cp Python_Back_End_Automation/.env.example Python_Back_End_Automation/.env
```

Then add your local credentials to `Python_Back_End_Automation/.env`:

```text
GitHub_API_username=
GitHub_API_token=
mysql_username=
mysql_password=
```

The real `.env` file is ignored by Git so credentials are not committed.

## Running Files

In VS Code, open any runnable Python file and use the play button. The shared `.vscode/launch.json` runs the current file from the workspace root.

You can also run files from the terminal:

```bash
python Python_Back_End_Automation/api/API_Validations.py
```

For pytest-style tests:

```bash
pytest Python_Back_End_Automation/tests
```

Some examples call public training APIs or require local MySQL credentials, so results can depend on network access, API availability, and your local database setup.

## Current Focus

I am continuing to build this repository toward a more complete QA automation portfolio, including cleaner package structure, reusable test utilities, stronger API validation patterns, and future Playwright-based UI automation.
