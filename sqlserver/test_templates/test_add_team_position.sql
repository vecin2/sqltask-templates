--{"team_keyname":"ADMINTEAM","person_keyname":"BATCHUSER","team_role_keyname":"ADMINTEAMROLE"}
INSERT INTO CE_POSITION (TENANT_ID, ID, TEAM_ID, TEAM_ENV_ID, AGENT_ID, ROLE_ID) 
VALUES (
	'default',--TENANT_ID
       	@POSITION.ADMINTEAM_BATCHUSER_ADMINTEAMROLE,--ID
       	@TEAM.ADMINTEAM,--TEAM_ID
       	@ENV.Dflt,--TEAM_ENV_ID
       	@PERSON.BATCHUSER,--AGENT_ID
       	@TEAMROLE.ADMINTEAMROLE--ROLE_ID
);
