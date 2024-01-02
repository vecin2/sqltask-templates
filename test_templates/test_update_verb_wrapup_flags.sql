--{"entity_definition_keyname":"Customer","verb_keyname":"viewCustomer","record_for_wrapup":"N","display_at_wrapup":"Y"}
UPDATE EVA_VERB 
SET (RECORD_FOR_WRAPUP, DISPLAY_AT_WRAPUP) = ('N','Y')
WHERE ID = @V.viewCustomer;
