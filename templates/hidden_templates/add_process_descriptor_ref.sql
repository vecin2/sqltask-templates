INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID,CONFIG_TYPE_ID, IS_SHARED) 
VALUES (
        @PDR.{{process_descriptor_ref_id}}, --id
        @PD.{{process_descriptor_id}}, --process_descriptor_id
	@ENV.Dflt, --process_descriptor_env_id
	{% set _pdr_config_id =pdr_config_id | default('NULL')%}
	{{_pdr_config_id}}, --config_id
	{% if _pdr_config_id == 'NULL' %}
	  {% set pdr_config_type_id = 'NULL' %}
	{% endif %}
	{{pdr_config_type_id | default('NULL')| suggest(_keynames.FULL_ET)}}, --ocnfig_type_id
       	'N' --is_shared
       );
