drop table train;
create table train as
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
from train_data
group by movie_id, rating
;
drop table test;
create table test as
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
from test_data
group by movie_id, rating
;
