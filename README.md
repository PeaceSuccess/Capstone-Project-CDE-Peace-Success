# CDE-CAPSTONE: Data Platform for Travel Agency

## Project Overview
This project aims to develop a robust data platform to process and store data from a Country REST API, enabling predictive analytics for a travel agency. The platform will leverage cloud infrastructure, data engineering tools, and machine learning techniques to deliver valuable insights.

## Data Architecture
**Data Flow:**
1. **Data Extraction:**
   - **Source:** Country REST API
   - **Target:** Cloud Object Storage (e.g., AWS S3) in Parquet format
2. **Data Transformation:**
   - **Source:** Cloud Object Storage
   - **Target:** Cloud Data Warehouse (e.g., Snowflake)
3. **Data Modeling:**
   - **Source:** Cloud Data Warehouse
   - **Target:** DBT-modeled fact and dimension tables

**Technology Stack:**
* **Cloud Infrastructure:** AWS
* **Data Engineering:** Apache Airflow, Python (Pandas)
* **Data Storage:** Cloud Object Storage, Cloud Data Warehouse
* **CI/CD:** GitHub Actions
* **Infrastructure as Code:** Terraform
* **Data Modeling:** DBT
* **Containerization:** Docker

## Workflow
1. **Data Extraction:**
   - Schedule API calls using Apache Airflow.
   - Extract the entire raw data and store it in Parquet format on Cloud Object Storage.
2. **Data Transformation:**
   - Use PySpark or Pandas to transform the raw data into a suitable format for the data warehouse.
   - Extract relevant attributes (country name, independence, UN membership, etc.).
3. **Data Loading:**
   - Orchestrate the loading process using Apache Airflow.
   - Load the transformed data into the Cloud Data Warehouse.
4. **Data Modeling:**
   - Utilize DBT to create a dimensional data model, defining fact and dimension tables.
5. **CI/CD Pipeline:**
   - Use GitHub Actions to automate the build, test, and deployment process.
   - Package the data pipeline code into a Docker image and push it to a container registry.

