// Create storage integration object

create or replace storage integration s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE 
  STORAGE_AWS_ROLE_ARN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  STORAGE_ALLOWED_LOCATIONS = ('s3://snowflake-s3-bucket-12/csv/')
   COMMENT = 'This an optional comment' ;
   
   
// See storage integration properties to fetch external_id so we can update it in S3
DESC integration s3_int;