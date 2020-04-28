SELECT V.ID as verb_ID, v.NAME as verb_name, pd.repository_path, V.IS_INSTANCE, V.IS_INSTANCE_DEFAULT as IS_DFLT,V.PROCESS_DESC_REF_ID as PDR, pdr.config_id,pdr.config_type_id,pd.config_process_id
FROM EVA_VERB v, EVA_PROCESS_DESC_REFERENCE pdr, EVA_PROCESS_DESCRIPTOR PD
where v.process_desc_ref_id = pdr.id
and pdr.process_descriptor_id = pd.id
and entity_def_id = @ED.{{entity_def_id | suggest(_keynames.ED)}}
order by v.name;
