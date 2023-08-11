--{"lower_id":"9","higher_id":"99"}
DELETE  
FROM LOCALISED_FIELD lf  
WHERE OBJECT_type ='ReasonCodeED' 
AND object_version >=9 
AND object_version<=99;

DELETE 
FROM
GTCC_REASON_CODE WHERE ID >= 9 AND ID <=99;
