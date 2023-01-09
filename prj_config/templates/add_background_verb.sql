--It add a background verb which can then be map to a profile
{% set entity_def_type_keyname = entity_type | suggest(_keynames.ET) %}
{% set entity_verbs = _db.fetch.v_names_by_et(entity_def_type_keyname).column('NAME') %}
{% set __verb_name = verb_name | suggest(entity_verbs) %}

INSERT INTO FA_BACKGROUND_VERB (ID,RELEASE_ID,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,VERB_NAME,EXECUTION_PROFILE,TENANT_ID,EXECUTION_ORDER_GROUP)
VALUES (
	@BV.{{entity_def_type_keyname}}{{__verb_name}},
	1,
	@ET.{{entity_def_type_keyname}},
	@ENV.Dflt,
	'{{__verb_name}}',
	2,
	'default',
	1
);
