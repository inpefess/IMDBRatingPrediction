delete from train_movie;
insert into train_movie (movie_id, rating)
select
    m.movie_id movie_id,
    rating
from movies m
where movie_id in (
    select movie_id
    from train_ids
)
;

delete from train_role;
insert into train_role (person_id, role, rating)
select person_id, role, sum(rating) rating
from roles r
inner join train_movie m
on r.movie_id = m.movie_id
group by person_id, role
;

delete from avg_role;
insert into avg_role (rating, role)
select avg(rating) rating, role
from train_role
group by role
;

delete from train_data_unpivot;
insert into train_data_unpivot (movie_id, role, rating_part, rating)
select
    m.movie_id movie_id,
    r.role role,
    sum(coalesce(tr.rating, ar.rating)) rating_part,
    m.rating rating
from train_movie m
left join roles r
on m.movie_id = r.movie_id
left join train_role tr
on r.person_id = tr.person_id
and r.role = tr.role
left join avg_role ar
on ar.role = r.role
group by m.movie_id, r.role
;

delete from train_data;
insert into train_data (movie_id, rating, actor, producer, writer, cinematographer, composer,
    costume_director, director, editor, misc, production_designer)
select movie_id, rating,
coalesce(sum(case when role = 1 then rating_part else 0 end), 0) actor,
coalesce(sum(case when role = 3 then rating_part else 0 end), 0) producer,
coalesce(sum(case when role = 4 then rating_part else 0 end), 0) writer,
coalesce(sum(case when role = 5 then rating_part else 0 end), 0) cinematographer,
coalesce(sum(case when role = 6 then rating_part else 0 end), 0) composer,
coalesce(sum(case when role = 7 then rating_part else 0 end), 0) costume_director,
coalesce(sum(case when role = 8 then rating_part else 0 end), 0) director,
coalesce(sum(case when role = 9 then rating_part else 0 end), 0) editor,
coalesce(sum(case when role = 10 then rating_part else 0 end), 0) misc,
coalesce(sum(case when role = 11 then rating_part else 0 end), 0) production_designer
from train_data_unpivot
group by movie_id, rating
;
