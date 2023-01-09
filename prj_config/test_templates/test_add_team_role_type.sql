--{"role_type_name":"Test Engineer"}
INSERT INTO CE_TEAM_ROLE_TYPE (TENANT_ID, ID, ENV_ID, RELEASE_ID, ROLE_NAME, IS_DELETED) 
VALUES (
	'default',--TENANT_ID
       	@TEAMROLETYPE.TestEngineer,--ID
	@ENV.Dflt,--ENV_ID
       	@RELEASE.ID,--RELEASE_ID
       	'Test Engineer',--ROLE_NAME
       	'N'--IS_DELETED
);
