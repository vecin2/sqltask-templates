SELECT V.ID as verb_ID,id.keyname v_keyname, v.NAME as verb_name, pd.repository_path, V.IS_INSTANCE, V.IS_INSTANCE_DEFAULT as IS_DFLT,v.IS_USER_VISIBLE, pdr.config_id,pdr.config_type_id,pd.config_process_id
FROM EVA_VERB v, EVA_PROCESS_DESC_REFERENCE pdr, EVA_PROCESS_DESCRIPTOR PD,CCADMIN_IDMAP id
where v.process_desc_ref_id = pdr.id
AND v.id = id.ID  AND id.KEYSET ='V'
and pdr.process_descriptor_id = pd.id
and entity_def_id = @ED.{{entity_def_id | suggest(_keynames.ED)}}
order by v.name;
