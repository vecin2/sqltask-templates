--{"team_name":"ProServ","homepage":"@HP.ContactCentreDesktop"}
INSERT INTO FRB_RULE_SET (TENANT_ID, ID, NAME, TYPE, VERSION, FACTS_LIST, RULESET_JSON, ENV_ID, IS_DELETED, ENTITY_REFERENCES, IS_ORIGINAL) 
VALUES ('default',
       	@RS.ProServTeamQueue,
       	'ProServTeamQueue0',
       	'Queue',
       	1,
       	NULL,
       	'{"name": "ProServTeamQueue0", "description":"Rule Set for the queue Pro Serv Team Queue", "rules":[]}',
	@ENV.Dflt,
       	'N',
       	NULL,
       	'Y'
);

INSERT INTO CWQ_QUEUE (ID, ENV_ID, RELEASE_ID, NAME, IS_DELETED, TRANSFER_ENTITLEMENT_ID, TRANSFER_ENTITLEMENT_ENV_ID, IS_OWNED, RULE_SET_NAME, UUID, TENANT_ID, ORG_REALM_ID) 
VALUES (
	@QUEUE.ProServTeamQueue,--ID
       	@ENV.Dflt,--RELEASE_ID
       	@RELEASE.ID,--RELEASE_ID
       	'Pro Serv Team Queue',--NAME
       	'N',--IS_DELETED
       	NULL,--TRANSFER_ENTITLEMENT_ID
       	NULL,--TRANSFER_ENTITLEMENT_ENV_ID
       	'Y',--IS_OWNED
       	'ProServTeamQueue0',--RULE_SET_NAME
       	'Pro_Serv_Team_Queue',--UUID
       	'default',--TENANT_ID
       	'organisat'--ORG_REALM_ID
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'QueueED', -- OBJECT_TYPE
'Pro_Serv_Team_Queue',--OBJECT_INSTANCE
@QUEUE.ProServTeamQueue,--OBJECT_VERSION
'displayName', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'Pro Serv Team Queue', --TEXT
'N' --IS_DELETED
);

INSERT INTO CE_TEAM (ID, ENV_ID, NAME, IS_DELETED, QUEUE_ID, QUEUE_ENV_ID, TENANT_ID, ORG_REALM_ID) 
VALUES (
	@TEAM.ProServ,--ID
	@ENV.Dflt,--ENV_ID
       	'ProServ',--NAME
       	'N',--IS_DELETED
       	@QUEUE.ProServTeamQueue,--QUEUE_ID
       	@ENV.Dflt,--QUEUE_ENV_ID
       	'default',--TENANT_ID
       	'organisat'--ORG_REALM_ID
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'TeamED', -- OBJECT_TYPE
'ProServ',--OBJECT_INSTANCE
@TEAM.ProServ,--OBJECT_VERSION
'displayName', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'Pro Serv', --TEXT
'N' --IS_DELETED
);

INSERT INTO FD_HOMEPAGE_ASSIGNMENT (TENANT_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, HOMEPAGE_ID, HOMEPAGE_ENV_ID, RELEASE_ID)
VALUES ('default',--TENANT_ID
       	@TEAM.ProServ,--ENTITY_ID
       	@ENV.Dlft,--ENTITY_ENV_ID
       	@ET.Team,--ENTITY_TYPE_ID
       	@ENV.Dflt,--ENTITY_TYPE_ENV_ID
       	@HP.ContactCentreDesktop,--HOMEPAGE_ID
       	@ENV.Dflt,--HOMEPAGE_ENV_ID
       	@RELEASE.ID--RELEASE_ID
);
INSERT INTO CWQ_ENTITY__QUEUE (TENANT_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, QUEUE_ID, QUEUE_ENV_ID, RELEASE_ID)
VALUES (
	'default',--TENANT_ID
       	@TEAM.ProServ,--ENTITY_ID
       	@ENV.Dflt,--ENTITY_TYPE_ENV_ID
       	@ET.Team,--ENTITY_TYPE_ID
       	@ENV.Dflt, --ENTITY_TYPE_ENV_ID
       	@QUEUE.ProServTeamQueue,--QUEUE_ID
       	@ENV.Dflt, --QUEUE_ENV_ID
       	@RELEASE.ID --RELEASE_ID
);
