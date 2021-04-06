-- 1. max

select max(datetime) from animal_ins

-- 2. min

select min(datetime) from animal_ins

-- 3. count

select count(animal_id) from animal_ins

-- 4. distinct

select count(distinct(name)) from animal_ins