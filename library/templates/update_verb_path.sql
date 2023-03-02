{% set _process_descriptor_id = process_descriptor_id | suggest(_keynames.PD) %}
{% set process_descriptor = _db.find.pd_by_keyname(_process_descriptor_id)%}
UPDATE EVA_PROCESS_DESCRIPTOR
SET (REPOSITORY_PATH) = ('{{new_process_path | print(process_descriptor) | codepath}}')
WHERE ID = @PD.{{_process_descriptor_id}};

{% set old_slash_path =process_descriptor["repository_path"] | replace(".","/") %}
{% set old_object_instance = process_descriptor["NAME"]+"__"+ old_slash_path %}
{% set new_slash_path =new_process_path | replace(".","/") %}
{% set new_object_instance = process_descriptor["NAME"]+"__"+ new_slash_path %}
UPDATE LOCALISED_FIELD
SET (OBJECT_INSTANCE) = ('{{new_object_instance}}')
WHERE object_instance = '{{old_object_instance}}';
