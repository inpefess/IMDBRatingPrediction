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

drop table genres;
create table genres as
select movie_id, info genre
from movie_info
where movie_id in (select movie_id from movies)
;

drop table roles;
create table roles as
select case when role_id in (1,2) then 'a'
when role_id = 4 then 'w'
else 'd' end role, person_id, movie_id
from cast_info
where movie_id in (select movie_id from movies)
;