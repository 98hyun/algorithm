-- 1. group by

select animal_type,count(distinct(animal_id)) from animal_ins
group by animal_type

-- 2. group by, having

select NAME,count(NAME) as 'COUNT'
from ANIMAL_INS 
group by NAME
having count(NAME)>=2
order by NAME

-- 3. where, having

select hour(DATETIME) as 'HOUR',count(hour(DATETIME)) as 'COUNT'
from ANIMAL_OUTS 
where hour(DATETIME)>=9 and hour(DATETIME)<=19
group by hour(DATETIME)
order by hour(DATETIME)

-- 4. left join, with, set, 

set @rownum:=-1; 

WITH H as (SELECT @rownum:=@rownum+1 as HOUR 
           FROM ANIMAL_OUTS
           limit 24),

A as (SELECT HOUR(DATETIME) as HOUR, count(*) as COUNT
      FROM ANIMAL_OUTS
      GROUP BY HOUR)

SELECT H.HOUR, IFNULL(A.COUNT, 0) as COUNT
FROM H
LEFT JOIN A on H.HOUR = A.HOUR