--{"entity_id":"TelephonyConfig","verb_name":"start"}
INSERT INTO EVA_DYNAMIC_VERB_LIST (ID,ENV_ID,RELEASE_ID,TYPE_ID,TYPE_ENV_ID,ENTITY_TYPE_ID,ENTITY_TYPE_ENV_ID,VERB_NAME,SEQUENCE_NO,TENANT_ID)
VALUES (@EDVL.TelephonyConfigStart, --ID
		@ENV.Dflt, --ENV_ID
		@RELEASE.ID, --RELEASE_ID
		@EDVLT.RegisterContactListeners, -- TYPE_ID
		@ENV.Dflt, --TYPE_ENV_ID
		@ET.TelephonyConfig, --ENTITY_TYPE_ID
		@ENV.Dflt,--ENTITY_TYPE_ENV_ID
		'start',--VERB_NAME
		@RELEASE.ID,--RELEASE_ID
		'default'--TENANT_ID
		);