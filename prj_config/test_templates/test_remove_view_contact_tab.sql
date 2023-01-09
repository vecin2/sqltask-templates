--{'entity_verb':'ContactHistoryEntitiyDefinitionViewContactWrapupDetails'}
DELETE FROM EVA_DYNAMIC_VERB_LIST 
WHERE ID = @EDVL.ViewContactWrapupDetails;

DELETE FROM CCADMIN_IDMAP 
WHERE KEYSET = 'EDVL' AND KEYNAME='ViewContactWrapupDetails';
