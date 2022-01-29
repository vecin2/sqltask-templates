--["KnowledgeArticle","title2","","StringField","1","Y","StringFieldProperties","125"]
INSERT INTO EVA_DYNAMIC_ENTITY_FIELD (ID, ENTITY_DEF_ID, NAME, INITIAL_VALUE, FIELD_TYPE_ID, FIELD_SEQUENCE, ENTITY_DEF_ENV_ID)
VALUES (@EDEF.KnowledgeArticleTitle2, @ED.KnowledgeArticle, 'title2', '', @EFT.StringField, 1, @ENV.Dflt);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE,OBJECT_INSTANCE,OBJECT_VERSION,FIELD_NAME,LOCALE,LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES ('DynamicEntityDefinitionED','KnowledgeArticleED',@ED.KnowledgeArticle,'fields.title2.displayName','en-US','default','Title2','N');


INSERT INTO EVA_DYN_ENT_FIELD_PROPERTIES (ID, RELEASE_ID, FIELD_ID, ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID) 
VALUES (@EDEFP.KnowledgeArticleTitle2, @RELEASE.ID, @EDEF.KnowledgeArticleTitle2, @ET.StringFieldProperties,@ENV.Dflt);

INSERT INTO EVA_DYN_ENTITY_FIELD_STRING_PR (ID, RELEASE_ID, MAX_LENGTH) VALUES (@EDEFP.KnowledgeArticleTitle2, @RELEASE.ID, 125);
