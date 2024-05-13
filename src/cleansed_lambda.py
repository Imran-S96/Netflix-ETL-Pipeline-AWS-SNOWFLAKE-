import json
import boto3
import pandas as pd
import io
import csv

s3 = boto3.client('s3')

def transform_cleanse_data(file_obj):
    try:
        # Read CSV file into DataFrame
        print("Reading CSV file...")
        df = pd.read_csv(file_obj['Body'])
        print("CSV file read successfully.")

        # Filter for only Movies from the United States 
        print("Filtering data...")
        df = df[(df['country'] == 'United States') & (df['type'] == 'Movie')]
        print("Data filtered successfully.")
        
        # Convert date column to datetime and format it as 'yyyy-mm-dd'
        print("Converting date format...")
        df['date_added'] = pd.to_datetime(df['date_added']).dt.strftime('%Y-%m-%d')
        print("Date format converted successfully.")
        
        # Remove 'min' from duration and convert to integer
        print("Cleaning duration data...")
        df['duration'] = df['duration'].str.replace('min', '').astype(int)
        print("Duration data cleaned successfully.")
        
        # Split and explode listed_in and cast columns
        print("Splitting and exploding data...")
        df = df.assign(listed_in=df['listed_in'].str.split(','), cast=df['cast'].str.split(',')).explode(['listed_in', 'cast'])
        print("Data split and exploded successfully.")
        
        # Rename Columns
        print("Renaming columns...")
        df.rename(columns={'duration': 'duration(m)', 'listed_in': 'genre'}, inplace=True)
        print("Columns renamed successfully.")

        # Convert DataFrame into list of dictionaries
        print("Converting DataFrame to list of dictionaries...")
        list_of_dicts = df.to_dict(orient='records')
        print("Conversion successful.")

        return list_of_dicts
    except Exception as e:
        print("Error in transform_cleanse_data:", e)
        raise

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            # Extract bucket name and file name from S3 event
            source_bucket_name = 'fifa-raw-bucket'
            file_key = 'netflix_titles.csv'
            
            # Read the CSV file from S3
            print("Fetching file from S3...")
            response = s3.get_object(Bucket=source_bucket_name, Key=file_key)
            print("File fetched successfully.")
            
            # Process the CSV file
            print("Processing CSV file...")
            list_of_dicts = transform_cleanse_data(response)
            print("CSV file processed successfully.")
            
            # Convert list of dictionaries back to CSV format
            print("Converting data to CSV format...")
            csv_buffer = io.StringIO()
            writer = csv.DictWriter(csv_buffer, fieldnames=list_of_dicts[0].keys())
            writer.writeheader()
            writer.writerows(list_of_dicts)
            csv_buffer.seek(0)
            print("Conversion to CSV format successful.")
            
            # Upload the modified CSV as a new file to another S3 bucket
            target_bucket_name = 'snowflake-s3-bucket-12'
            new_file_name = 'cleaned_' + file_key  # Prefix 'cleaned_' to original file name
            print("Uploading file to S3...")
            s3.put_object(Bucket=target_bucket_name, Key=new_file_name, Body=csv_buffer.getvalue(), ContentType='text/csv')
            print("File uploaded successfully.")

        return {
            'statusCode': 200,
            'body': 'Processed uploaded CSV files successfully'
        }
    except Exception as e:
        print("Error in lambda_handler:", e)
        return {
            'statusCode': 500,
            'body': 'Error processing uploaded CSV files'
        }
