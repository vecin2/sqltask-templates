{% set __process_descriptor_id = process_descriptor_id | suggest(_keynames.PD) %}
UPDATE EVA_PROCESS_DESCRIPTOR
SET (REPOSITORY_PATH) = ('{{new_process_path | codepath}}')
WHERE ID = @PD.{{__process_descriptor_id}};
