-- 1. where in 

select ANIMAL_ID,NAME,SEX_UPON_INTAKE
from ANIMAL_INS 
where NAME in ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')

-- 2. where like

select ANIMAL_ID,NAME
from ANIMAL_INS 
where NAME like '%el%' and ANIMAL_TYPE='Dog'
order by NAME

-- 3. case when, like

select ANIMAL_ID,NAME,case when SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%' then 'O' else 'X' end as '중성화'
from ANIMAL_INS 

-- 4. subtract datetime

select ANIMAL_OUTS.ANIMAL_ID,ANIMAL_OUTS.NAME
from ANIMAL_OUTS
left join ANIMAL_INS on ANIMAL_OUTS.ANIMAL_ID=ANIMAL_INS.ANIMAL_ID
where ANIMAL_INS.DATETIME is not null
order by ANIMAL_INS.DATETIME- ANIMAL_OUTS.DATETIME
limit 2

-- 5. date

select ANIMAL_ID,NAME,date_format(DATETIME,'%Y-%m-%d') as 날짜
from ANIMAL_INS
order by ANIMAL_ID
