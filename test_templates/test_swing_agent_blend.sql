--{"agent_keyname":"SYSTEMADMIN","blend_keyname":"Email"}
INSERT INTO GTCC_MEMBEROFBLEND (TENANT_ID, AGENT_ID, BLEND_ID) 
VALUES (
'default', --TENANT_ID
@PERSON.SYSTEMADMIN, --AGENT_ID
@BLEND.Email --BLEND
);
