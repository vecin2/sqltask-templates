--{"display_name":"My New Entitlement","is_workflow":"","is_content":"","locale":"en-GB"}
INSERT INTO EVA_ENTITLEMENT (ID,ENV_ID,IS_DELETED,IS_WORKFLOW_ENTITLEMENT,RELEASE_ID,RESOLUTION_PROCESS,IS_CONTENT_ENTITLEMENT,SYSTEM_NAME,TENANT_ID,IS_PRIVILEGE_ENTITLEMENT,SCOPE_EXPAND_DIRECTION,IS_CONTEXT_ENTITLEMENT)
VALUES (
    @ENTLMNT.MyNewEntitlement,--ID
    @ENV.Dflt,--ENV_ID
    'N',--IS_DELETED
    'N',--IS_WORKFLOW_ENTITLEMENT
    @RELEASE.ID, --RELEASE_ID
    null,--RESOLUTION_PROCESS
    'N', --IS_CONTENT_ENTITLEMENT
    'MyNewEntitlement', --SYSTEM_NAME
    'default',--TENANT_ID
    'N',--IS_PRIVILEGE_ENTITLEMENT
    null,--SCOPE_EXPAND_DIRECTION
    'N'--IS_CONTEXT_ENTITLEMENT
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
    'EntitlementED', -- OBJECT_TYPE
    'MyNewEntitlement', -- OBJECT_INSTANCE
    @ENTLMNT.MyNewEntitlement, -- OBJECT_VERSION
    'displayName', -- FIELD_NAME
    'en-GB', -- LOCALE
    'default', -- LOOKUP_LOCALE
    'My New Entitlement', --TEXT
    'N' --IS_DELETED
);

