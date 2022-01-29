
{% set pptive_ids = _keynames.PPTIVE %}
{% set temp_pptive_id = perspective_id | suggest(pptive_ids)%}
{% set verb_ids = _keynames.V %}
{% set last_sequence_num = _db.fetch.av_topseq_by_pers_keyname(perspective_id).column('SEQUENCE_NUM') %}
{% set sequence_desc ="Sequence_no (Last in sequece was "+last_sequence_num[0].__str__()+")"  %}
{% set __sequence_number = sequence_num | description(sequence_desc) %}
INSERT INTO FD_ENTITY__AUX_VERBS (ENTITY_ID,ENTITY_ENV_ID,ENTITY_TYPE_ID,ENTITY_TYPE_ENV_ID,AUXILIARY_VERB_ID,SEQUENCE_NUM,RELEASE_ID,TENANT_ID)
VALUES (
	@PPTIVE.{{perspective_id}}, -- entity_id 
	@ENV.Dflt, --entity_env_id
	@ET.Perspective,--entity_type_id
	@ENV.Dflt, --entity_type_env_id
	@V.{{verb_id | suggest(verb_ids)}}, --auxiliary_verb_id
	{{__sequence_number}},--sequence_num
	@RELEASE.ID,--relase_id
	'default' --tenant_id
);

