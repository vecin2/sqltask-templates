--{"team_keyname":"BUSINESS_ADMIN","entitlement_name":"TelephonyAutoAnswer0"}
INSERT INTO EVA_ENTITY__ENTITLEMENT (ENTITLEMENT_ID, ENTITLEMENT_ENV_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, IS_DELETED, RELEASEID, TENANT_ID) 
VALUES (
	@ENTLMNT.TelephonyAutoAnswer, --ENTITLEMENT_ID
	@ENV.Dflt,--ENTITY_ENV_ID
       	@PROFILE.BUSINESS_ADMIN, --ENTITY_ID
	@ENV.Dflt,--ENTITY_ENV_ID
       	@ET.ProfileType,
       	@ENV.Dflt,
       	'N',
       	@RELEASE.ID,
       	'default');
