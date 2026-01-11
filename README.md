# YouTube Data Pipeline using AWS (End-to-End)
📌 **Project Overview**

This project demonstrates an end-to-end data engineering pipeline built on AWS, which extracts YouTube video data using the YouTube Data API, processes and transforms it using **AWS Lambda** and **AWS Glue**, stores it in **Amazon S3 (Parquet format)**, and enables analytics using **Amazon Athena**.
The goal of this project is to showcase real-world **ETL workflows**, serverless data processing, and analytics-ready data modeling.

**🏗️ Architecture Overview**

**High-level flow:**

1. Extract YouTube video metadata using YouTube Data API
2. Store raw JSON data in Amazon S3
3. Trigger transformation to structured format
4. Convert processed data into Parquet
5. Query data using Amazon Athena

Architecture is as below:

<img width="1618" height="982" alt="image" src="https://github.com/user-attachments/assets/425e6794-5fe1-4f24-985b-33937e0c6e9f" />



**🧰 Tech Stack Used**

**Programming Language**: Python

**Cloud Platform**: AWS

**Services**:
AWS Lambda,
 Amazon S3,
 AWS Glue (Spark ETL),
 Amazon Athena,
 AWS IAM

**Data Format**: JSON → Parquet

**API**: YouTube Data API v3



**🔄 Data Pipeline Explanation**

**1️.Data Extraction (AWS Lambda)**

* Fetches video data from YouTube Data API
* Extracts fields like:
video_id,
 title,
 published_at,
 view_count,
 like_count
* Stores raw data as JSON in Amazon S3

**2️. Data Transformation (AWS Glue)**

* Reads raw JSON data from S3
* Cleans and structures the data
* Converts data into Parquet format
* Writes optimized Parquet files back to S3

**3️. Analytics (Amazon Athena)**

* Glue Data Catalog used for schema discovery
* Athena queries run directly on Parquet files
* Example analytics:
 Top viewed videos,
 Most liked videos,
 Recent trending content



**🧪 Sample Athena Query**

SELECT title, view_count, like_count

FROM youtube_db.parquet_data

ORDER BY view_count DESC
LIMIT 10;


**📊 Output**

* Optimized Parquet files stored in S3
* Fast, cost-efficient analytics using Athena
* Query results visible in screenshots



**🔐 Security & Best Practices**

* IAM roles with least-privilege access
* No credentials hard-coded
* Environment variables used for secrets
* Columnar storage (Parquet) for performance



**🚀 Key Learnings**

* Building serverless ETL pipelines
* Handling semi-structured API data
* Data transformation using Spark (Glue)
* Analytics using Athena
* Real-world AWS data engineering workflow



**📌 Future Enhancements**

* Automate pipeline using EventBridge
* Add incremental data loads
* Create dashboards using Amazon QuickSight
* Add CI/CD using GitHub Actions

