-- 1. select order by
select * from animal_ins order by animal_id

-- 2. select order by desc
select name,datetime,animal_id
from animal_ins order by animal_id desc

-- 3. select where 
select animal_id,name from animal_ins where intake_condition='Sick'

-- 4. select where order by
select animal_id,name from animal_ins where intake_condition!="Aged" 
order by animal_id

-- 5. 생략.

-- 6. select order by multiple conditions
select animal_id,name,datetime 
from animal_ins 
order by name,datetime desc

-- 7. select limit
select name from animal_ins order by datetime desc limit 1