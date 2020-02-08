--{"entity_name":"AgreementED","entity_display_name":"Agreement","entity_description":"Agreement Description","_locale":"en-US","summary":"Article2 [title]"}
INSERT INTO EVA_ENTITY_DEFINITION (ID, ENV_ID, NAME, UUID, TYPE_UUID, TYPE_ID, TYPE_ENV_ID, LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID, IS_DELETED, IS_BASIC, SUPPORTS_READONLY,IS_EXPANDABLE, ICON_PATH, INSTANCE_ICON_PATH) VALUES (
@ED.Agreement, -- ID
@ENV.Dflt, -- ENV_ID
'AgreementED', -- NAME
'AgreementED', -- UUID
'AgreementED', -- TYPE_UUID
@ET.Agreement, -- TYPE_ID
@ENV.Dflt, -- TYPE_ENV_ID
'FrameworkDynamicEntities.Implementation.DynamicEntity.Objects.DynamicEntity', -- LOGICAL_OBJECT_PATH
'FrameworkDynamicEntities.API.EntityInterfaces.EIDynamicEntity', -- INTERFACE_PATH
@ED.BaseDynamicEntity, -- SUPER_ENTITY_DEFINITION
@ENV.Dflt, -- SUPER_ENTITY_DEFINITION_ENV_ID
'N', -- IS_DELETED
'N', -- IS_BASIC
'Y', --SUPPORTS_READONLY
'N', --IS_EXPANDABLE
NULL, -- ICON_PATH
NULL -- INSTANCE_ICON_PATH
);

INSERT INTO EVA_CATEGORY_ENTRY(CATEGORY_ID, CATEGORY_ENV_ID, ENTITY_ID, ENTITY_ENV_ID) VALUES (
@EC.DynamicEntity, -- CATEGORY_ID
@ENV.Dflt, -- CATEGORY_ENV_ID
@ED.Agreement, -- ENTITY_ID
@ENV.Dflt -- ENTITY_ENV_ID
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'DynamicEntityDefinitionED', -- OBJECT_TYPE
'AgreementED', -- OBJECT_INSTANCE
@ED.Agreement, -- OBJECT_VERSION
'displayName', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'Agreement', --TEXT
'N' --IS_DELETED
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'DynamicEntityDefinitionED', -- OBJECT_TYPE
'AgreementED', -- OBJECT_INSTANCE
@ED.Agreement, -- OBJECT_VERSION
'description', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'Agreement Description', --TEXT
'N' --IS_DELETED
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'DynamicEntityDefinitionED', -- OBJECT_TYPE
'AgreementED', -- OBJECT_INSTANCE
@ED.Agreement, -- OBJECT_VERSION
'summaryExpression', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'Article2 [title]', --TEXT
'N' --IS_DELETED
);

INSERT INTO EVA_DYNAMIC_ENTITY_DEF (ID,ENV_ID,RELEASE_ID) 
VALUES (
	@ED.Agreement,
	@ENV.Dflt, --ENV_ID
	@RELEASE.ID --RELEASE_ID
	);
