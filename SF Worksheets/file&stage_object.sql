// Create file format object
CREATE OR REPLACE file format NETFLIX.NETFLIX_SCHEMA.csv_fileformat
    type = csv
    field_delimiter = ','
    skip_header = 1
    null_if = ('NULL','null')
    empty_field_as_null = TRUE;
    
    
 // Create stage object with integration object & file format object
CREATE OR REPLACE stage NETFLIX.NETFLIX_SCHEMA.csv_folder
    URL = 's3://snowflake-s3-bucket-12/csv/'
    STORAGE_INTEGRATION = s3_int
    FILE_FORMAT = NETFLIX.NETFLIX_SCHEMA.csv_fileformat
