-- 1. null

select ANIMAL_ID
from ANIMAL_INS 
where NAME is null

--2. not null

select ANIMAL_ID
from ANIMAL_INS 
where NAME is not null

--3. ifnull

select ANIMAL_TYPE,ifnull(NAME,'No name') as NAME,SEX_UPON_INTAKE
from ANIMAL_INS