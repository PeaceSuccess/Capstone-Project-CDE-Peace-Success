# CDE-CAPSTONE: Building a Data Platform for Travel Agency

## Project Overview
This project aims to construct a robust data platform to process and store data from a Country REST API, enabling predictive analytics for a travel agency. The platform leverages cloud infrastructure, data engineering tools, and machine learning techniques to deliver valuable insights.

## Data Architecture
The data architecture comprises the following layers:

1. **Raw Data Layer:**
   - **Source:** Country REST API
   - **Storage:** Cloud Object Storage (e.g., AWS S3, GCP Storage) in Parquet format

2. **Data Warehouse Layer:**
   - **Storage:** Cloud Data Warehouse (e.g., Snowflake, BigQuery)
   - **Modeling:** DBT for data modeling into fact and dimension tables

## Technology Stack
* **Cloud Infrastructure:** AWS, GCP, or Azure
* **Data Engineering:** Apache Airflow, Python (Pandas, PySpark)
* **Data Storage:** Cloud Object Storage, Cloud Data Warehouse
* **CI/CD:** GitHub Actions
* **Infrastructure as Code:** Terraform
* **Data Modeling:** DBT
* **Containerization:** Docker

## Workflow
1. **Data Extraction:**
   - Utilize Apache Airflow to schedule the extraction of data from the Country REST API.
   - Extract the entire raw data and store it in Parquet format on Cloud Object Storage.

2. **Data Transformation:**
   - Employ PySpark or Pandas to transform the raw data into the required format.
   - Extract the necessary attributes (country name, independence, UN membership, startOfWeek, official country name, common native name, currency code, currency name, currency symbol, country code, capital, region, subregion, languages, area, population, continents).

3. **Data Loading:**
   - Leverage Apache Airflow to orchestrate the loading of the transformed data into the Cloud Data Warehouse.
   - Utilize DBT to model the data into fact and dimension tables.

4. **CI/CD:**
   - Employ GitHub Actions to automate the building, testing, and deployment of the data pipeline.
   - Package the data extraction and loading code into a Docker image and push it to a container registry.

## Additional Considerations
* **Data Quality:** Implement data quality checks to ensure data accuracy and completeness.
* **Security:** Implement appropriate security measures to protect sensitive data.
* **Performance Optimization:** Optimize the data pipeline for performance and scalability.
* **Error Handling:** Implement robust error handling and logging mechanisms.
* **Monitoring:** Monitor the data pipeline to identify and resolve issues.

## Bonus
* **Data Insights:** Explore the dataset to uncover interesting insights, such as:
   - Identify countries with similar characteristics.
   - Analyze the distribution of languages across different regions.
   - Predict potential tourist destinations based on user preferences.

## Submission Requirements
* **Presentation:** Create a presentation to explain the project architecture, technology stack, and key insights.
* **README:** Write a clear and concise README file to document the project.
* **GitHub Repository:** Commit all project code, configuration files, and documentation to a GitHub repository.

By adhering to these guidelines, we can construct a robust and scalable data platform to support the travel agency's data-driven decision-making.