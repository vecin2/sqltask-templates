--{"entity_type_id":"Customer","verb_name":"inlineSearch"}
INSERT INTO FA_BACKGROUND_VERB (ID,RELEASE_ID,ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID,VERB_NAME,EXECUTION_PROFILE,TENANT_ID,EXECUTION_ORDER_GROUP)
VALUES (
	@BV.CustomerinlineSearch,
	1,
	@ET.Customer,
	@ENV.Dflt,
	'inlineSearch',
	2,
	'default',
	1
);
