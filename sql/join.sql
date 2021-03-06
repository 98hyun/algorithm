-- 1. left join

select ANIMAL_OUTS.ANIMAL_ID,ANIMAL_OUTS.NAME
from ANIMAL_OUTS 
left join ANIMAL_INS
on ANIMAL_INS.ANIMAL_ID=ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_INS.ANIMAL_ID is null

-- 2. left join

select ANIMAL_OUTS.ANIMAL_ID,ANIMAL_OUTS.NAME
from ANIMAL_OUTS 
left join ANIMAL_INS
on ANIMAL_INS.ANIMAL_ID=ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_INS.DATETIME>ANIMAL_OUTS.DATETIME
order by ANIMAL_INS.DATETIME

-- 3. left join 

select ANIMAL_INS.NAME, ANIMAL_INS.DATETIME
from ANIMAL_INS
left join ANIMAL_OUTS on ANIMAL_INS.ANIMAL_ID=ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_OUTS.ANIMAL_ID is null
order by ANIMAL_INS.DATETIME
limit 3

-- 4. left join 

select ANIMAL_INS.ANIMAL_ID,ANIMAL_INS.ANIMAL_TYPE,ANIMAL_INS.NAME
from ANIMAL_INS
left join ANIMAL_OUTS on ANIMAL_INS.ANIMAL_ID=ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_INS.SEX_UPON_INTAKE!=ANIMAL_OUTS.SEX_UPON_OUTCOME

-- 4번 다른 답

select ANIMAL_OUTS.ANIMAL_ID,ANIMAL_OUTS.ANIMAL_TYPE,ANIMAL_OUTS.NAME 
from ANIMAL_OUTS 
left join ANIMAL_INS on ANIMAL_OUTS.ANIMAL_ID=ANIMAL_INS.ANIMAL_ID 
where ANIMAL_INS.SEX_UPON_INTAKE like 'Intact%' and (ANIMAL_OUTS.SEX_UPON_OUTCOME like 'Spayed%' or ANIMAL_OUTS.SEX_UPON_OUTCOME like 'Neutered%')