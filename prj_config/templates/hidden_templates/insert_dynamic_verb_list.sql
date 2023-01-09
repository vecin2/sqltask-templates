{%set entity_type_id = entity_id | suggest(_keynames.ET)%}
{% set verb_names = _db.fetch.v_names_by_et(entity_type_id).column('NAME') %}

{%set __verb_name = verb_name | suggest(verb_names)%} 
{% set edvl_id =entity_id + __verb_name.capitalize()%}
INSERT INTO EVA_DYNAMIC_VERB_LIST (ID,ENV_ID,RELEASE_ID,TYPE_ID,TYPE_ENV_ID,ENTITY_TYPE_ID,ENTITY_TYPE_ENV_ID,VERB_NAME,SEQUENCE_NO,TENANT_ID)
VALUES (@EDVL.{{edvl_id}}, --ID
		@ENV.Dflt, --ENV_ID
		@RELEASE.ID, --RELEASE_ID
		@EDVLT.{{edvl_type_keyname}}, -- TYPE_ID
		@ENV.Dflt, --TYPE_ENV_ID
		@ET.{{entity_type_id}}, --ENTITY_TYPE_ID
		@ENV.Dflt,--ENTITY_TYPE_ENV_ID
		'{{__verb_name}}',--VERB_NAME
		@RELEASE.ID,--RELEASE_ID
		'default'--TENANT_ID
		);
