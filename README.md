# Expense Data Warehouse ETL Pipeline with FastAPI and Docker

## Project Overview

The project supports full loading, incremental loading, and Slowly Changing Dimension Type 2 (SCD Type 2) for employee history. FastAPI provides an endpoint to trigger the ETL pipeline, and Docker packages the application for containerized execution.

## Project Objectives  

- Automate expense data ingestion from CSV files.
- Clean and validate raw expense data using Python and Pandas.
- Load data into a structured MySQL data warehouse.
- Implement full and incremental data loading.
- Track employee changes using SCD Type 2.
- Maintain fact and dimension tables with primary and foreign keys.
- Expose an API endpoint to trigger ETL execution.
- Run the application inside a Docker container.

## Technologies Used

- Python
- Pandas and NumPy
- MySQL
- SQLAlchemy and PyMySQL
- FastAPI
- Uvicorn
- Docker
- Git and GitHub

## Architecture
```
Raw Expense CSV Files
         |
         v
Python ETL Pipeline
         |
         v
Data Cleaning and Validation
         |
         v
Full Load / Incremental Load
         |
         v
Dimension Processing
Employee SCD Type 2
         |
         v
Fact and Dimension Tables
         |
         v
MySQL Data Warehouse
```

## FastAPI and Docker Integration

```
Client / Swagger UI
         |
         v
FastAPI Application
         |
         v
POST /etl/run
         |
         v
Existing Python ETL Pipeline
         |
         v
MySQL Data Warehouse
```

Docker packages the FastAPI application, ETL code, and Python dependencies into a container image.

## FastAPI Integration

FastAPI exposes an endpoint to execute the existing ETL pipeline.

| HTTP Method | Endpoint | Description |
|:---|:---|:---|
| `GET` | `/` | Check API status |
| `POST` | `/etl/run` | Trigger the ETL pipeline |

## API Documentation

When the application is running, open:

http://localhost:8000/docs

Use the interactive Swagger UI to test the API endpoints.

The ETL endpoint should report success only when the pipeline finishes successfully. Exceptions in the ETL functions must be propagated to the API layer for accurate error reporting.

## Docker Setup

- Prerequisites

- Python 3.12 or compatible environment
- Docker Desktop
- MySQL server
- Git

## Project Structure

```
Expense-Data-Warehouse/
│
├── Data/
│   ├── Raw/
│   └── Archive/
│
├── main.py
├── expense_date_warehouse_etl.py
├── config.py
├── database.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env.example
├── etl.log
├── LICENSE
└── README.md
```
## Build the Docker Image

Open a terminal in the project directory and run:
```
docker build -t expense-warehouse .
```

## Run the Container
```
docker run --rm -p 8000:8000 --env-file .env expense-warehouse
```

The container starts Uvicorn and serves the FastAPI application on port 8000.

Open the Swagger UI:

http://localhost:8000/docs

## Database Configuration

Configure the following environment variables in your local .env file:
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=host.docker.internal
DB_NAME=your_database_name

## Installation and Local Execution

1. Clone the Repository
```
git clone <your-repository-url>
cd <your-project-folder>
```

2. Install Dependencies
```
python -m pip install -r requirements.txt
```

3. Configure the Environment

Create a local .env file containing the MySQL connection settings.

4. Prepare Input Data

Place the required CSV files inside:
Data/Raw/

5. Run the ETL Directly
```
python expense_date_warehouse_etl.py

```
6. Run FastAPI Locally

Open http://localhost:8000/docs and use POST /etl/run to trigger the ETL pipeline.

## Security Considerations

- Store credentials in environment variables.
- Exclude .env from Git and Docker build contexts.
- Protect the ETL trigger endpoint from unauthorized use before deployment.
- Avoid simultaneous ETL runs against the same input files.
- Back up the warehouse before destructive full loads.


## Future Improvements

- Add automated tests for ETL transformations and API endpoints.
- Deploy the application to a cloud environment.
- Add a reporting dashboard for warehouse analysis.

## Author

**Akshay Gawand**