{% set description =" Display name will be computed from the name - 'ProductSupport' --> 'Product Support'"%} 
{% set __team_name = team_name | description("team_name (one word capitalize, e.g. ProductSupport)")  | print(description) %}
{% set rule_set_keyname = __team_name +"TeamQueue"%}
{% set rule_set_name = __team_name+"TeamQueue0" %}
INSERT INTO EVA_MIGRATABLE (TENANT_ID, ENTITY_ID, ENTITY_ENV_ID, RELEASE_ID, TYPE_NAME, MIGRATABLE_REFERENCE, VERSION, IS_REMOTE, ENTITY_VERSION,  IS_DELETED, INCLUDE_IN_EXPORT, EXPORT_LOCALE, ENTITY_MINOR_VERSION) 
VALUES
('default', 
	@RS.{{rule_set_keyname}},
	@ENV.Dflt,--RELEASE_ID
	@RELEASE.ID,--RELEASE_ID
	'RuleSetED',
	'{{rule_set_name}}',
	1,
	'N',
	0,
	'N',
	'Y',
	'ALL',
	0);
INSERT INTO FRB_RULE_SET (TENANT_ID, ID, NAME, TYPE, VERSION, FACTS_LIST, RULESET_JSON, ENV_ID, IS_DELETED, ENTITY_REFERENCES, IS_ORIGINAL) 
VALUES ('default',
       	@RS.{{rule_set_keyname}},
       	'{{rule_set_name}}',
       	'Queue',
       	1,
       	NULL,
	{%set team_display_name = __team_name | split_uppercase %} 
       	'{"name": "{{__team_name}}TeamQueue0", "description":"Rule Set for the queue {{team_display_name}} Team Queue", "rules":[]}',
	@ENV.Dflt,
       	'N',
       	NULL,
       	'Y'
);

INSERT INTO CWQ_QUEUE (ID, ENV_ID, RELEASE_ID, NAME, IS_DELETED, TRANSFER_ENTITLEMENT_ID, TRANSFER_ENTITLEMENT_ENV_ID, IS_OWNED, RULE_SET_NAME, UUID, TENANT_ID, ORG_REALM_ID) 
VALUES (
	@QUEUE.{{__team_name}}TeamQueue,--ID
       	@ENV.Dflt,--RELEASE_ID
       	@RELEASE.ID,--RELEASE_ID
       	'{{team_display_name}} Team Queue',--NAME
       	'N',--IS_DELETED
       	NULL,--TRANSFER_ENTITLEMENT_ID
       	NULL,--TRANSFER_ENTITLEMENT_ENV_ID
       	'Y',--IS_OWNED
       	'{{__team_name}}TeamQueue0',--RULE_SET_NAME
	{%set uuid_name = team_display_name.replace(" ","_") %}
       	'{{uuid_name}}_Team_Queue',--UUID
       	'default',--TENANT_ID
       	'organisat'--ORG_REALM_ID
);
{% set object_type = "QueueED" %}
{% set object_instance = uuid_name+"_Team_Queue" %}
{% set object_version = "@QUEUE."+__team_name+"TeamQueue" %}
{% set field_name = "displayName" %}
{% set text = team_display_name +" Team Queue" %}
{% set locale = _locale %}
{% include 'add_localised_field.sql' %}

INSERT INTO CE_TEAM (ID, ENV_ID, NAME, IS_DELETED, QUEUE_ID, QUEUE_ENV_ID, TENANT_ID, ORG_REALM_ID) 
VALUES (
	@TEAM.{{__team_name}},--ID
	@ENV.Dflt,--ENV_ID
       	'{{__team_name}}',--NAME
       	'N',--IS_DELETED
	@QUEUE.{{__team_name}}TeamQueue,--QUEUE_ID
       	@ENV.Dflt,--QUEUE_ENV_ID
       	'default',--TENANT_ID
       	'organisat'--ORG_REALM_ID
);
{% set object_type = "TeamED" %}
{% set object_instance = __team_name %}
{% set object_version = "@TEAM."+__team_name %}
{% set field_name = "displayName" %}
{% set text = team_display_name%}
{% include 'add_localised_field.sql' %}


{% set __homepage = homepage | suggest(_keynames.FULL_HP) | default("NULL")%}--HOMEPAGE_ID
{% if __homepage != 'NULL'%}
INSERT INTO FD_HOMEPAGE_ASSIGNMENT (TENANT_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, HOMEPAGE_ID, HOMEPAGE_ENV_ID, RELEASE_ID)
VALUES ('default',--TENANT_ID
       	@TEAM.{{__team_name}},--ENTITY_ID
       	@ENV.Dlft,--ENTITY_ENV_ID
       	@ET.Team,--ENTITY_TYPE_ID
       	@ENV.Dflt,--ENTITY_TYPE_ENV_ID
       	{{__homepage}},--HOMEPAGE_ID
       	@ENV.Dflt,--HOMEPAGE_ENV_ID
       	@RELEASE.ID--RELEASE_ID
);
{% endif %}
INSERT INTO CWQ_ENTITY__QUEUE (TENANT_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, QUEUE_ID, QUEUE_ENV_ID, RELEASE_ID)
VALUES (
	'default',--TENANT_ID
       	@TEAM.{{__team_name}},--ENTITY_ID
       	@ENV.Dflt,--ENTITY_TYPE_ENV_ID
       	@ET.Team,--ENTITY_TYPE_ID
       	@ENV.Dflt, --ENTITY_TYPE_ENV_ID
	@QUEUE.{{__team_name}}TeamQueue,--QUEUE_ID
       	@ENV.Dflt, --QUEUE_ENV_ID
       	@RELEASE.ID --RELEASE_ID
);

