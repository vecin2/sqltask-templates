{#
[oneline_description]
Removes reason code or avilable status codes

[long_description]
It takes a range of reason codes IDs and it removes all the reason codes within that range including both ends.

[related_tasks]
add_reason_code.sql
#}
{% set message = "It deletes reason codes by range including both ends.\nFor example:  lower_id <= ID <= higher_id " %}
{% set _lower_id = lower_id %}
{% set _higher_id = higher_id | default(_lower_id) | print("leave default will only delete that one ID") %}

DELETE  
FROM LOCALISED_FIELD lf  
WHERE OBJECT_type ='ReasonCodeED' 
AND object_version >=9 
AND object_version<=99;

DELETE  
FROM GTCC_REASON_CODE 
WHERE ID >= {{lower_id}} AND ID <={{_higher_id}};
