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
