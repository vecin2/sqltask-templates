--{"perspective_id":"CUSTOMER","verb_keyname":"AuxBookmarkWidget"}
DELETE FROM FD_ENTITY__AUX_VERBS 
where entity_id= @PPTIVE.CUSTOMER
and AUXILIARY_VERB_ID = @V.AuxBookmarkWidget;
