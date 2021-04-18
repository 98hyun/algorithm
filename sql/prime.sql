set @num=1;
set @div=1;
select group_concat(n separator '&')
from (select @num:=@num+1 as n
     from information_schema.tables as t1,information_schema.tables as t2
     limit 1000) as n1
where not exists(select *
                from (select @div:=@div+1 as d
                     from information_schema.tables as t3,information_schema.tables as t4
                     limit 1000) as n2
                where mod(n,d)=0 and n!=d)