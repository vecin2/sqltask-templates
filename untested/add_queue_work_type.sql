INSERT INTO CWQ_QUEUE (ID, ENV_ID, RELEASE_ID, NAME, DESCRIPTION, IS_DELETED, TRANSFER_ENTITLEMENT_ID, TRANSFER_ENTITLEMENT_ENV_ID, IS_OWNED, RULE_SET_NAME, UUID, TENANT_ID, ORG_REALM_ID) 
VALUES (@QUEUE.{{queue_keyname}}, @ENV.Dflt, @RELEASE.ID, '{{display_name}}Queue', '{{display_name}}Queue', 'N', @ENTLMNT.{{entitlement_key | suggest (_keynames.ENTLMNT)}}, @ENV.Dflt, 'N', 'MPMSAirNZNABEscalationsQueue0', '{{queue_keyname}}Queue', 'default', 'organisat');

