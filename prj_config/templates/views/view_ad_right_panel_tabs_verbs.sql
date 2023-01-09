{% set pptive_ids = _keynames.PPTIVE %}
{% set __perspective_id = perspective_id | suggest(pptive_ids)%}
SELECT ed.name as entity_def_name, v.name as verb_name, idmap.keyname as verb_keyname, pd.repository_path, v.IS_INSTANCE, v.IS_USER_VISIBLE, v.RECORD_FOR_WRAPUP 
FROM FD_ENTITY__AUX_VERBS eav, eva_verb v, EVA_PROCESS_DESCRIPTOR pd, EVA_PROCESS_DESC_REFERENCE pdr, EVA_ENTITY_DEFINITION ed, CCADMIN_IDMAP idmap
where eav.AUXILIARY_VERB_ID = v.id
and v.PROCESS_DESC_REF_ID = pdr.id
and v.ENTITY_DEF_ID = ed.id
and v.id = idmap.id
and idmap.keyset ='V'
and pdr.process_descriptor_id =pd.id
and ENTITY_ID = @PPTIVE.{{__perspective_id}} -- entity_id 

