--{'edvl_id':'StartInteractionFactMonitor'}
DELETE FROM EVA_DYNAMIC_VERB_LIST 
WHERE ID = @EDVL.StartInteractionFactMonitor;

DELETE FROM CCADMIN_IDMAP 
WHERE KEYSET = 'EDVL' AND KEYNAME='StartInteractionFactMonitor';