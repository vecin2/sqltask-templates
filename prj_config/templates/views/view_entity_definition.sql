--its meant to show details from an entity definition
{% set entity_names = _db.fetch.all_ed().column('NAME') %}
SELECT id, name, LOGICAL_OBJ_PATH, INTERFACE_PATH FROM eva_entity_definition where name ='{{ entity_name | suggest(entity_names)}}';
