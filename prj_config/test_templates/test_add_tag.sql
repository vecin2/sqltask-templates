--["pepe3","CONTENTCAT","CONTENTCAT","@TAG.CCDOCUP","15","","1","","","1"]
INSERT INTO eva_tag (ID,ENV_ID,RELEASE_ID,TAGSET_ID,TAGSET_ENV_ID,TAGSET_RELEASE_ID,PARENT_TAG,PARENT_TAG_ENV_ID,PARENT_TAG_RELEASE_ID,PREVIOUS_TAG,PREVIOUS_TAG_ENV_ID,PREVIOUS_TAG_RELEASE_ID,NAME,IS_SYSTEM,IS_DELETED,IS_RETIRED,EXPAND_DIRECTION,CREATED_DATE,LAST_MODIFIED_DATE,LEFT_VAL,RIGHT_VAL,DEPTH_VAL,DISPLAY_ORDER,SYSTEM_CODE) 
VALUES (@TAG.pepe3, --ID
	@ENV.Dflt, --ENV_ID
	@RELEASE.ID, --RELEASE_ID
	@TAG.CONTENTCAT, -- TAGSET_ID
	@ENV.Dflt,-- TAGSET_ENV_ID
	@RELEASE.ID,-- TAGSET_RELEASE_ID
	@TAG.CONTENTCAT,--PARENT_TAG_ID
	@ENV.Dflt,--PARENT_TAG_ENV_ID
	@RELEASE.ID,--PARENT_TAG_RELEASE_ID
	@TAG.CCDOCUP,--PREVIOUS_TAG
	@ENV.Dflt,--PREVIOUS_TAG_ENV_ID
	@RELEASE.ID,--PREVIOUS_TAG_RELEASE_ID
	'content_pepe3', --NAME
	'N', --IS_SYSTEM
	'N',--IS_DELETED
	'N',--IS_RETIRED
	null,--EXPAND_DIRECTION
	sysdate, -- created
	sysdate, --LAST_MODIFIED
	15, --LEFT_VAL
	16, --RIGHT_VAL
	1, --DEPTH_VAL
	null, -- DISPLAY_ORDER
	'content_pepe3' --SYSTEM_CODE
);
update eva_tag
set (RIGHT_VAL)=(17)
where id =@TAG.CONTENTCAT;

INSERT INTO eva_tag_loc (ID,ENV_ID,RELEASE_ID,LOCALE,DESCRIPTION,ICON_URI,REPORTING_LABEL) 
VALUES (@TAG.pepe3,--id
	   @ENV.Dflt,--env_id
	   @RELEASE.ID,--release_id
	   'en-GB',--locale
	   'pepe3',--description
	   null,--icon_uri
	   'pepe3' --reporting_label
);
INSERT INTO EVA_TAG_DISPLAY_NAME (ID,ENV_ID,RELEASE_ID,DISPLAY_NAME_TYPE_ID,DISPLAY_NAME_TYPE_ENV_ID,DISPLAY_NAME_TYPE_RELEASE_ID)
VALUES (@TAG.pepe3,--id
	   @ENV.Dflt,--env_id
	   @RELEASE.ID,--release_id
	   1,--display_name_type
	   @ENV.Dflt, --display_name_type_env_id
	   @RELEASE.ID--display_name_type_release_id
);

INSERT INTO EVA_TAG_DISPLAY_NAME_LOC (ID,ENV_ID,RELEASE_ID,LOCALE,DISPLAY_NAME,DISPLAY_NAME_TYPE_ID,DISPLAY_NAME_TYPE_ENV_ID,DISPLAY_NAME_TYPE_RELEASE_ID)
VALUES (@TAG.pepe3,--id
	   @ENV.Dflt,--env_id
	   @RELEASE.ID,--release_id
	   'en-GB',--locale
	   'pepe3',--display_name
	   1, --display_name_type_id
	   @ENV.Dflt,--display_name_type_env_id
	   @RELEASE.ID--display_name_type_release_id
);
