INSERT INTO EVA_CONTEXT_VERB_ENTRY (CONFIG_ID,CONFIG_ENV_ID,VERB,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,SEQUENCE_NUMBER,RELEASE_ID) 
VALUES (
	 @CC.{{__context_config_id}},--config_id
  	 @ENV.Dflt, --config_env_id
  	 '{{__verb_name}}', --verbname
  	 @ET.{{__entity_type}}, --entity_type
  	 @ENV.Dflt, --entity_def_type_env_id
  	 {{__sequence_number}}, --sequence_number
  	 @RELEASE.ID --release_id
       );
