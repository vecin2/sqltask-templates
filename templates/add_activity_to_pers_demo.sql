{% set __config_keyname = context_keyname | suggest(_keynames.CC) %}
{% set __entity_type = entity_type | suggest(_keynames.ET) %}
{% set __verb_names = entity_type | suggest(_keynames.ET) %}
INSERT INTO EVA_CONTEXT_VERB_ENTRY (CONFIG_ID,CONFIG_ENV_ID,VERB,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,SEQUENCE_NUMBER,RELEASE_ID) 
VALUES (
	 @CC.{{__config_keyname}},--config_id
  	 @ENV.Dflt, --config_env_id
  	 'InlineCreate', --verbname
  	 @ET.{{__entity_type}}, --entity_type
  	 @ENV.Dflt, --entity_def_type_env_id
  	 1, --sequence_number
  	 @RELEASE.ID --release_id
       );
