--{"entity_keyname":"Customer","verb_keyname":"IdentifyCustomer","entitlement_key":"TelephonyAutoAnswer"}
INSERT INTO EVA_VERB_ENTITLEMENT (ENTITLEMENT_ID,ENTITLEMENT_ENV_ID,VERB_ID,RELEASE_ID,TENANT_ID) 
VALUES (
	@ENTLMNT.TelephonyAutoAnswer, --ENTITLEMENT_ID
	@ENV.Dflt, --ENTITLEMENT_ENV_ID
	@V.IdentifyCustomer, --VERB_ID
	@RELEASE.ID, --RELEASE_ID
	'default' --TENANT_ID
	);
