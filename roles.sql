drop table roles;
create table roles as
select
    case
        when role_id in (1,2) then 1
        else role_id
    end role,
    person_id,
    movie_id
from cast_info
where movie_id in (select movie_id from movies)
;
