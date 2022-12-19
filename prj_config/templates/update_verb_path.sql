{% set _process_descriptor_id = process_descriptor_id | suggest(_keynames.PD) %}
{% set process_descriptor = _db.find.pd_by_keyname(_process_descriptor_id)%}
UPDATE EVA_PROCESS_DESCRIPTOR
SET (REPOSITORY_PATH) = ('{{new_process_path | print(process_descriptor) | codepath}}')
WHERE ID = @PD.{{_process_descriptor_id}};
