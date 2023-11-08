--{"display_name":"Create Customer5","host":"ExternalAgentDesktopHost123","path":"/customer-service/default/customers","request_type":"POST","content_type":"application/ld+json","body":"{number:1}"}
--skip.run-on-db
--We are no testing against the db for this template because we need a host to exist and there is not hosts OTB, so we will have to insert one host before running this test, and this is not supported on the tool at the moment
INSERT INTO EVA_MIGRATABLE (ENTITY_ID, ENTITY_ENV_ID, RELEASE_ID, TYPE_NAME, MIGRATABLE_REFERENCE, VERSION, IS_REMOTE, ENTITY_VERSION, IS_DELETED, INCLUDE_IN_EXPORT, EXPORT_LOCALE, ENTITY_MINOR_VERSION, TENANT_ID) VALUES (
    @WIU.CreateCustomer5, --ENTITY_ID 
	@ENV.Dflt, --ENTITY_ENV_ID
	@RELEASE.ID, --RELEASE_ID
	'WebIntegrationURLED',--TYPE_NAME
	'WebIntegrationURLED-Create Customer5',--MIGRATABLE_REFERENCE
	'1',--VERSION
	'N',--IS_REMOTE
	0,--ENTITY_VERSION
	'N',--IS_DELETED
	'N',--INCLUDE_IN_EXPORT
	'ALL',--EXPORT_LOCALE
	0,--ENTITY_MINOR_VERSION
	'default'--TENANT_ID
);

INSERT INTO EVA_TAGSET_SELECTION
(ID, ENV_ID, RELEASE_ID, TAG_NAME, TAGSET_NAME, TENANT_ID)
VALUES(
@TS.CreateCustomer5, 
@ENV.Dflt,
@RELEASE.ID,
'systemset_notmigratable',
'systemset', 
'default');

INSERT INTO EVA_TAGSET_SELECTION
(ID, ENV_ID, RELEASE_ID, TAG_NAME, TAGSET_NAME, TENANT_ID)
VALUES(
@TS.CreateCustomer5, 
@ENV.Dflt,
@RELEASE.ID,
'upurpose_smartmatch',
'upurpose',
'default');

INSERT INTO FWI_URL
(ID, ENV_ID, RELEASE_ID, NAME, IS_DELETED, TENANT_ID, HOST_ID, "PATH", REQUEST_TYPE, CONTENT_TYPE, MESSAGE_BODY, ADD_AUTH_HEADER, AUTHORISATION_SERVER_ID)
VALUES(@WIU.CreateCustomer5,  @ENV.Dflt, @RELEASE.ID, 'Create Customer5', 'N', 'default', @FWIH.ExternalAgentDesktopHost123, '/customer-service/default/customers', 'POST', 'application/ld+json', '{number:1}', 'Y', NULL);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'WebIntegrationURLED', -- OBJECT_TYPE
'CreateCustomer5', -- OBJECT_INSTANCE
@WIU.CreateCustomer5, -- OBJECT_VERSION
'displayName', -- FIELD_NAME
'en-GB', -- LOCALE
'default', -- LOOKUP_LOCALE
'Create Customer5', --TEXT
'N' --IS_DELETED
);

INSERT INTO EVA_ENTITY__TAGSET_SELECTION (TENANT_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, ENTITY_TYPE_RELEASE_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_RELEASE_ID, RELATIONSHIP_TYPE, TAG_SELECTION)
VALUES (
	'default',--TENANT_ID
	@ET.EmbeddedSite,--ENTITY_TYPE_ID
	@ENV.Dflt,--ENTITY_TYPE_ENV_ID
	@RELEASE.ID,--ENTITY_TYPE_RELEASE_ID
	@WIU.CreateCustomer5,--ENTITY_ID
	@ENV.Dflt,--ENTITY_ENV_ID
	@RELEASE.ID,--ENTITY_RELEASE_ID
	'urlpurposerelationshipkey',--RELATIONSHIP_TYPE
	@TS.CreateCustomer5--TAG_SELECTION
);

INSERT INTO EVA_ENTITY__TAGSET_SELECTION (TENANT_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, ENTITY_TYPE_RELEASE_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_RELEASE_ID, RELATIONSHIP_TYPE, TAG_SELECTION)
VALUES (
	'default',--TENANT_ID
	@ET.EmbeddedSite,--ENTITY_TYPE_ID
	@ENV.Dflt,--ENTITY_TYPE_ENV_ID
	@RELEASE.ID,--ENTITY_TYPE_RELEASE_ID
	@WIU.CreateCustomer5,--ENTITY_ID
	@ENV.Dflt,--ENTITY_ENV_ID
	@RELEASE.ID,--ENTITY_RELEASE_ID
	'migrationRelationshipKey',--RELATIONSHIP_TYPE
	@TS.CreateCustomer5--TAG_SELECTION
);

