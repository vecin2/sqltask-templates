
SELECT ed.name, v.name,pd.REPOSITORY_PATH 
FROM EVA_DYNAMIC_VERB_LIST edvl, EVA_ENTITY_DEFINITION ed, eva_verb v, EVA_PROCESS_DESC_REFERENCE pdr, EVA_PROCESS_DESCRIPTOR pd
where  edvl.ENTITY_TYPE_ID = ed.TYPE_ID
and v.ENTITY_DEF_ID = ed.id
and v.name = edvl.verb_name
and v.PROCESS_DESC_REF_ID = pdr.id
and pdr.PROCESS_DESCRIPTOR_ID = pd.id
and edvl.TYPE_ID =@EDVLT.RegisterContactListeners;
