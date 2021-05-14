select
(ry-0.5*ny*(ny+1))/(ny*nx) as auc,
pctr/tctr as copc
select
count(*) as cnt,
sum(if(y=1,rank,0)) as ry,
sum(y) as ny ,
sum(1-y) as nx,
sum(pctr)/count (*) as pctr,
sum(y)/count (*)  as tctr
from (
    select click as y,
    row_number() over( order  by pctr ASC) as rank,
    pctr
    from a.impr_click_table
    where pt = '2021-05-14'
) t
