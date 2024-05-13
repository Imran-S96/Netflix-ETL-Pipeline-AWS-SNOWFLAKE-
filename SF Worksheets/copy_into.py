COPY INTO Shows (show_id, type, title, director, country, date_added, release_year, rating, duration, listed_in, description)
FROM '@NETFLIX.NETFLIX_SCHEMA.csv_folder'
FILE_FORMAT = (TYPE = 'CSV', SKIP_HEADER = 1)
ON_ERROR = 'SKIP_FILE_1';

COPY INTO Cast (show_id, cast)
FROM '@NETFLIX.NETFLIX_SCHEMA.csv_folder'
FILE_FORMAT = (TYPE = 'CSV', SKIP_HEADER = 1)
ON_ERROR = 'SKIP_FILE_1';
