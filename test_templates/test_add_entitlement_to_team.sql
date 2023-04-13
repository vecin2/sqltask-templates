--{"team_keyname":"ADMINTEAM","entitlement_name":"TelephonyAutoAnswer0"}
INSERT INTO EVA_ENTITY__ENTITLEMENT (ENTITLEMENT_ID, ENTITLEMENT_ENV_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, IS_DELETED, RELEASEID, TENANT_ID) 
VALUES (
	@ENTLMNT.TelephonyAutoAnswer, --ENTITLEMENT_ID
	@ENV.Dflt,--ENTITY_ENV_ID
       	@TEAM.ADMINTEAM, --ENTITY_ID
	@ENV.Dflt,--ENTITY_ENV_ID
       	@ET.Team,
       	@ENV.Dflt,
       	'N',
       	@RELEASE.ID,
       	'default');
