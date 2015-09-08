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

create table imdb.movie_data as
    select
        group_concat(role||'.'||person_id) features,
        rating
    from imdb.roles r
    inner join imdb.movies m
    on m.movie_id = r.movie_id
    group by m.movie_id, rating
;
