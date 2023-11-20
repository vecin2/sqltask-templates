{% set _entity_definition_keyname = entity_definition_keyname | suggest(_keynames.ED) %}
{% set entity_def = _db.fetch.ed_by_keyname(_entity_definition_keyname) %}
{% set _super_entity_def_keyname = super_entity_def_keyname | suggest(_keynames.ED) | print(entity_def)%}
UPDATE EVA_ENTITY_DEFINITION 
SET (SUPER_ENTITY_DEFINITION) = (@ED.{{_super_entity_def_keyname}})
WHERE ID = @ED.{{_entity_definition_keyname}};
