select n,case
when p is null then 'Root'
when (select count(*) from bst where p=a.n) then 'Inner'
else 'Leaf'
end
from bst a
order by n