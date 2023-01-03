{%set _entity_keyname = entity_keyname | suggest(_keynames.ED) %}
{% set entity_verb_keynames = _db.fetch.v_names_by_ed(_entity_keyname).column('KEYNAME') %}
{% set _verb_keyname = verb_keyname | suggest(entity_verb_keynames)%}
UPDATE EVA_VERB
set (IS_INSTANCE_DEFAULT) = ('N')
where ENTITY_DEF_ID = @ED.{{_entity_keyname}};

UPDATE EVA_VERB
set (IS_INSTANCE_DEFAULT) = ('Y')
where ID = @V.{{_verb_keyname}};

