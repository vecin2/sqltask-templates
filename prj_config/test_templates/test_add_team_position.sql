--{"team_keyname":"ProductSupport","person_keyname":"SYSTEMADMIN","team_role_keyname":"Default"}
INSERT INTO CE_POSITION (TENANT_ID, ID, TEAM_ID, TEAM_ENV_ID, AGENT_ID, ROLE_ID) 
VALUES (
	'default',--TENANT_ID
       	@POSITION.ProductSupport_SYSTEMADMIN_Default,--ID
       	@TEAM.ProductSupport,--TEAM_ID
       	@ENV.Dflt,--TEAM_ENV_ID
       	@PERSON.SYSTEMADMIN,--AGENT_ID
       	@TEAMROLE.Default--ROLE_ID
);
