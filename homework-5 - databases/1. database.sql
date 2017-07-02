CREATE TABLE critics (
    id                  serial PRIMARY KEY,
    full_name           varchar(120) NOT NULL,
    nationality_code    char(2),
    company             varchar(120)
);

CREATE TABLE films (
    id                  serial PRIMARY KEY,
    title               varchar(120) NOT NULL,
    release_year        char(4),
    rating              decimal,
    duration            int
);

CREATE TABLE directors (
    id                  serial PRIMARY KEY,
    full_name           varchar(120),
    year_of_birth       decimal,
    nationality_code    char(2)
);

CREATE TABLE reviews (
    id                  serial PRIMARY KEY,
    critic_id           int,
    film_id             int,
    rank                char(2)
);

CREATE TABLE directions (
    id                  serial PRIMARY KEY,
    director_id         int,
    film_id             int
);

CREATE TABLE genres (
    id                  serial PRIMARY KEY,
    film_id             int,
    genre               varchar(60)
);

CREATE TABLE countries (
    id                  serial PRIMARY KEY,
    name                varchar(120) NOT NULL,
    code                char(2),
    continent_code      char(2)
);

CREATE TABLE continents (
    id                  serial PRIMARY KEY,
    code                char(2),
    name                varchar(120) NOT NULL
);
