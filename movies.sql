drop table movies;
create table movies as
select cast(info as number) rating, movie_id
from movie_info_idx
where info_type_id = 101
and movie_id in (
select movie_id
from movie_info_idx
where info_type_id = 100
and cast(info as integer) >= 11000)
;
