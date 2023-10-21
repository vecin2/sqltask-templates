{% set description =" Display name will be computed from the name - 'ProductEngineer' --> 'Product Engineer'"%} 
{% set __team_role_name = team_role_name | description("team_role_name (one word capitalize, e.g. ProductEngineer)")  | print(description) %}
INSERT INTO CE_TEAM_ROLE (TENANT_ID, ID, NAME, ROLE_TYPE_ID, ROLE_TYPE_ENV_ID, IS_DELETED) 
VALUES (
	'default', --TENANT_ID
       	@TEAMROLE.{{__team_role_name}},--ID
       	'{{__team_role_name}}',--NAME
       	@TEAMROLETYPE.{{role_type_keyname | suggest(_keynames.TEAMROLETYPE)}},--ROLE_TYPE_ID
	@ENV.Dflt,--ROLE_TYPE_ENV_ID
       	'N'--IS_DELETED
);
{% set object_type = "TeamRoleED" %}
{% set object_instance = __team_role_name%}
{% set object_version = "@TEAMROLE."+__team_role_name%}
{% set field_name = "displayName" %}
{% set text = __team_role_name | split_uppercase %}
{% set locale = _default_locale %}
{% include 'add_localised_field.sql' %}
