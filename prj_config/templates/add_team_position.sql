{% set __team_keyname =team_keyname | suggest(_keynames.TEAM)%}
{% set __person_keyname = person_keyname | suggest(_keynames.PERSON) %}
{% set __team_role_keyname = team_role_keyname | suggest(_keynames.TEAMROLE) %}
INSERT INTO CE_POSITION (TENANT_ID, ID, TEAM_ID, TEAM_ENV_ID, AGENT_ID, ROLE_ID) 
VALUES (
	'default',--TENANT_ID
       	@POSITION.{{__team_keyname}}_{{__person_keyname}}_{{__team_role_keyname}},--ID
       	@TEAM.{{__team_keyname}},--TEAM_ID
       	@ENV.Dflt,--TEAM_ENV_ID
       	@PERSON.{{__person_keyname}},--AGENT_ID
       	@TEAMROLE.{{__team_role_keyname}}--ROLE_ID
);
