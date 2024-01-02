INSERT INTO GTCC_MEMBEROFBLEND (TENANT_ID, AGENT_ID, BLEND_ID) 
VALUES (
'default', --TENANT_ID
@PERSON.{{agent_keyname | suggest(_keynames.PERSON) }}, --AGENT_ID
@BLEND.{{blend_keyname | suggest(_keynames.BLEND)}} --BLEND
);
