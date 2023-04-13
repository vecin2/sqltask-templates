SELECT V.ENTITY_DEF_ID, ED.NAME as ED_NAME, ci.keyname as v_keyname,V.ID as v_ID, v.NAME as verb_name, pd.repository_path, V.IS_INSTANCE,V.PROCESS_DESC_REF_ID
FROM EVA_ENTITY_DEFINITION ED, EVA_VERB v, EVA_PROCESS_DESC_REFERENCE pdr, EVA_PROCESS_DESCRIPTOR PD, CCADMIN_IDMAP ci 
where v.PROCESS_DESC_REF_ID = pdr.id
and pdr.PROCESS_DESCRIPTOR_ID = pd.id
and v.ENTITY_DEF_ID = ED.ID
AND ci.id = V.id AND ci.KEYSET ='V'
and pd.REPOSITORY_PATH = '{{repository_path |codepath()}}'
order by v.name;
