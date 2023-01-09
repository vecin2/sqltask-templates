INSERT INTO CE_TEAM_ROLE_TYPE (TENANT_ID, ID, ENV_ID, RELEASE_ID, ROLE_NAME, IS_DELETED) 
VALUES (
	'default',--TENANT_ID
	{% set role_type_keyname = role_type_name.replace(" ","") %}
       	@TEAMROLETYPE.{{role_type_keyname}},--ID
	@ENV.Dflt,--ENV_ID
       	@RELEASE.ID,--RELEASE_ID
       	'{{role_type_name}}',--ROLE_NAME
       	'N'--IS_DELETED
);
