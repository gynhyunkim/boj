SELECT * 
FROM places
WHERE host_id in
(SELECT host_id
FROM places
group by host_id having count(*) > 1)
order by id asc;

