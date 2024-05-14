# Netflix-ETL-Pipeline-AWS-SNOWFLAKE

## Overview
Netflix provided me with a raw, disorganized CSV file containing a comprehensive list of programming available on their platform. My task is to develop an ETL (Extract, Transform, Load) pipeline to clean, transform, and load the CSV file onto both the AWS and Snowflake platforms.

## Aims
This project serves as a platform for me to demonstrate my proficiency in leveraging tools such as Pandas and Python, along with my burgeoning familiarity with AWS and Snowflake platforms. It marks my initial foray into utilizing some of these features, offering an opportunity for growth and exploration as I navigate the intricacies of data manipulation, cloud computing, and database management. Through this endeavor, I aim to not only accomplish the task at hand but also to broaden my skill set and deepen my understanding of these powerful technologies.

## Technologies 
1. Python (Pandas)
2. AWS (S3 Buckets, Lambda Functions, Cloudwatch, IAM Roles) 
3. SNOWFLAKE (SQL Worksheets, Databases)
## Set Up
### AWS 
1. Create S3 Buckets
2. Create IAM Policy
3. Create Lambdas

### SNOWFLAKE
1. Create Database.
2. Create Schema.
3. Create Tables.
4. Create Fileformat.
5. Create Stage. 
6. Create Intergration Object.
7. Create Copy Into.

## Future Implementation 
Automate process by creating a Lambda Function to load data into SNOWFLAKE directly rather than a SQL Worksheet to copy data into tables.  

## Architecture 
![alt text](<NETFLIX ETL PIPELINE.jpg>)

## Snowflake Schema 
![alt text](<NETFLIX SNOWFLAKE SCHEMA.png>)