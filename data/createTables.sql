attach "imdb_raw.sqlite" as raw;
attach "imdb.sqlite" as imdb;

create table imdb.movies as
select
    cast(info as number) rating,
    movie_id
from raw.movie_info_idx
where info_type_id = 101
and movie_id in (
    select movie_id
    from raw.movie_info_idx
    where info_type_id = 100
    and cast(info as integer) >= 1000
)
and movie_id in (
    select movie_id
    from raw.cast_info
)
;

create table imdb.roles as
select
    case
        when role_id in (1,2) then 1
        else role_id
    end role,
    person_id,
    movie_id
from raw.cast_info
where movie_id in (select movie_id from imdb.movies)
;

detach raw;

create table imdb.train_ids (
    movie_id INTEGER
);

create table imdb.train_movie (
    movie_id INTEGER,
    rating REAL
);

create table imdb.train_role (
    person_id INTEGER,
    role INTEGER,
    rating REAL
);

create table imdb.avg_role (
    rating REAL,
    role INTEGER
);

create table imdb.train_data_unpivot (
    movie_id INTEGER,
    role INTEGER,
    rating_part REAL,
    rating REAL
);

create table imdb.train_data (
    movie_id INTEGER,
    rating REAL,
    actor REAL,
    producer REAL,
    writer REAL,
    cinematographer REAL,
    composer REAL,
    costume_designer REAL,
    director REAL,
    editor REAL,
    misc REAL,
    production_designer REAL
);

detach imdb;
