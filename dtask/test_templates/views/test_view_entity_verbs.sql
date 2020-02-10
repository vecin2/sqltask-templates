--{"entity_def_id":"Customer"}
SELECT V.ID as verb_ID, v.NAME as verb_name, pd.repository_path 
FROM EVA_VERB v, EVA_PROCESS_DESC_REFERENCE pdr, EVA_PROCESS_DESCRIPTOR PD
where v.process_desc_ref_id = pdr.id
and pdr.process_descriptor_id = pd.id
and entity_def_id = @ED.Customer; 
