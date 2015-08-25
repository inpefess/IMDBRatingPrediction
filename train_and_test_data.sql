drop table train_movie;
create table train_movie as
select movie_id, rating
from movies
limit 100;

drop table train_role;
create table train_role as
select person_id, role, sum(rating) rating
from roles r
inner join train_movie m
on r.movie_id = m.movie_id
group by person_id, role
;

drop table avg_role;
create table avg_role as
select avg(rating) rating, role
from train_role
group by role
;

drop table train_data;
create table train_data as
select m.movie_id, r.role, sum(coalesce(tr.rating, ar.rating)) rating_part, m.rating
from train_movie m
inner join roles r
on m.movie_id = r.movie_id
left join train_role tr
on r.person_id = tr.person_id
and r.role = tr.role
left join avg_role ar
on ar.role = r.role
group by m.movie_id, r.role
;

drop table test_movie;
create table test_movie as
select movie_id, rating
from movies
where movie_id not in
(select movie_id from train_movie)
;

drop table test_data;
create table test_data as
select m.movie_id, r.role, sum(coalesce(tr.rating, ar.rating)) rating_part, m.rating
from test_movie m
inner join roles r
on m.movie_id = r.movie_id
left join train_role tr
on r.person_id = tr.person_id
and r.role = tr.role
left join avg_role ar
on ar.role = r.role
group by m.movie_id, r.role
;
