{% set _entity_definition_keyname = entity_definition_keyname | suggest(_keynames.ED) %}
{% set entity_def = _db.fetch.ed_by_keyname(_entity_definition_keyname) %}
{% set _new_entity_def_name = new_entity_def_name | suggest(_keynames.ED) | print(entity_def)%}
{% set _new_interface_path = new_interface_path | codepath() %}
{% set _new_logical_object_path = new_logical_object_path | codepath() %}
UPDATE EVA_ENTITY_DEFINITION 
SET (NAME,UUID,TYPE_UUID,INTERFACE_PATH,LOGICAL_OBJ_PATH) = ('{{_new_entity_def_name}}','{{_new_entity_def_name}}','{{_new_entity_def_name}}','{{_new_interface_path}}','{{_new_logical_object_path}}')
WHERE ID = @ED.{{_entity_definition_keyname}};

UPDATE LOCALISED_FIELD
SET (OBJECT_INSTANCE) = ('{{_new_entity_def_name}}')
WHERE OBJECT_TYPE = 'EntityDefinitionED'
and OBJECT_VERSION = @ED.{{_entity_definition_keyname}};
