--{"team_keyname":"ProductSupport","person_keyname":"SYSTEMADMIN","team_role_keyname":"Default"}
--skip.run-on-db
--We are no testing against the db for this template because we need a team to exist and there is not teams OTB, so we will have to insert one team before running this test, and this is not supported on the tool at the moment
INSERT INTO CE_POSITION (TENANT_ID, ID, TEAM_ID, TEAM_ENV_ID, AGENT_ID, ROLE_ID) 
VALUES (
	'default',--TENANT_ID
       	@POSITION.ProductSupport_SYSTEMADMIN_Default,--ID
       	@TEAM.ProductSupport,--TEAM_ID
       	@ENV.Dflt,--TEAM_ENV_ID
       	@PERSON.SYSTEMADMIN,--AGENT_ID
       	@TEAMROLE.Default--ROLE_ID
);
