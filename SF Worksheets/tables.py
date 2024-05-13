CREATE TABLE Netflix_Movies (
    show_id INT PRIMARY KEY,
    type VARCHAR(50),
    title VARCHAR(255),
    director VARCHAR(255),
    country VARCHAR(255),
    date_added DATE,
    release_year INT,
    rating VARCHAR(50),
    duration VARCHAR(50),
    listed_in VARCHAR(255),
    description VARCHAR(5000)
);

CREATE TABLE Netflix_Cast (
    cast_id INT PRIMARY KEY AUTOINCREMENT,
    show_id INT,
    cast VARCHAR(255),
    FOREIGN KEY (show_id) REFERENCES NETFLIX_MOVIES(show_id)
);

