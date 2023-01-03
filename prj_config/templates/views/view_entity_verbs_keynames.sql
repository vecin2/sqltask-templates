SELECT V.ID as verb_ID,id.keyname v_keyname, v.NAME as verb_name, pd.repository_path, pdr_id.keyname as pdr_keyname, pd_id.keyname as pd_keyname
FROM EVA_VERB v, EVA_PROCESS_DESC_REFERENCE pdr, EVA_PROCESS_DESCRIPTOR PD,CCADMIN_IDMAP id, CCADMIN_IDMAP pdr_id, CCADMIN_IDMAP pd_id
where v.process_desc_ref_id = pdr.id
AND v.id = id.ID  AND id.KEYSET ='V'
AND pdr.id = pdr_id.ID  AND pdr_id.KEYSET ='PDR'
AND pd.id = pd_id.ID  AND pd_id.KEYSET ='PD'
and pdr.process_descriptor_id = pd.id
and entity_def_id = @ED.{{entity_def_id | suggest(_keynames.ED)}}
order by v.name;
