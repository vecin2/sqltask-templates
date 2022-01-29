--["KnowledgeArticle","Create2","ContentView","N","ContentAuthoringLayout","",""]
INSERT INTO EVA_DYNAMIC_ENTITY_VIEW (ID,ENTITY_DEF_ID,ENTITY_DEF_ENV_ID,NAME,RELEASE_ID,VIEW_TYPE_ID,VIEW_TYPE_ENV_ID,USE_TABS,TENANT_ID) 
VALUES (
	@DEV.KnowledgeArticleCreate2, --ID
	@ED.KnowledgeArticle, --ENTITY_DEF_ID
	@ENV.Dflt, --ENTITY_DEF_ENV_ID
	'Create2', --NAME
	@RELEASE.ID, --RELEASE_ID
	@ET.ContentView, --VIEW_TYPE_ID
	@ENV.Dflt, --VIEW_TYPE__ENV_ID
	'N', --USE_TABS
	'default');

INSERT INTO EVA_DYNAMIC_ENTITY_VIEW_LAYOUT (ID,RELEASE_ID,LAYOUT_TYPE_ID,TENANT_ID) 
VALUES (
	@DEV.KnowledgeArticleCreate2,
	@RELEASE.ID, --RELEASE_ID
	@ELT.ContentAuthoringLayout,
	'default');

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'DynamicEntityDefinitionED', -- OBJECT_TYPE
'KnowledgeArticleED', -- OBJECT_INSTANCE
@ED.KnowledgeArticle, -- OBJECT_VERSION
'views.Create2.displayName', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'KnowledgeArticleCreate2', --TEXT
'N' --IS_DELETED
);
