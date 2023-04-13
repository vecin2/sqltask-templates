
SELECT V.ID as verb_ID, v.NAME as verb_name, pd.repository_path AS REPO_PATH, V.IS_INSTANCE AS IS_INST, V.IS_INSTANCE_DEFAULT as IS_DFLT,v.IS_USER_VISIBLE AS VISIBLE,eed.name AS ED_NAME, pdr.config_id,pdr.config_type_id,pd.config_process_id
FROM EVA_VERB v, EVA_PROCESS_DESC_REFERENCE pdr, EVA_PROCESS_DESCRIPTOR PD, EVA_ENTITY_DEFINITION eed 
where v.process_desc_ref_id = pdr.id
AND v.ENTITY_DEF_ID =eed.id
and pdr.process_descriptor_id = pd.id
and v.ID = @V.{{verb_keyname | suggest(_keynames.V)}}

order by v.name;
