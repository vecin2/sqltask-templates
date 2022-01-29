--{"entity_type_id":"Customer","verb_name":"inlineSearch"}
INSERT INTO EVA_DYNAMIC_VERB_LIST (ID,ENV_ID,RELEASE_ID,TYPE_ID,TYPE_ENV_ID,ENTITY_TYPE_ID,ENTITY_TYPE_ENV_ID,VERB_NAME,SEQUENCE_NO,TENANT_ID)
VALUES (@EDVL.CustomerInlineSearch, --ID
		@ENV.Dflt, --ENV_ID
		@RELEASE.ID, --RELEASE_ID
		@EDVLT.InlineViewContactConfig, -- TYPE_ID
		@ENV.Dflt, --TYPE_ENV_ID
		@ET.Customer, --ENTITY_TYPE_ID
		@ENV.Dflt,--ENTITY_TYPE_ENV_ID
		'inlineSearch',--VERB_NAME
		@RELEASE.ID,--RELEASE_ID
		'default'--TENANT_ID
		);
