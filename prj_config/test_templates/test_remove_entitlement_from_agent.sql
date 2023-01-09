--{"person_keyname":"admin","entitlement_name":"TelephonyAutoAnswer"}
DELETE FROM EVA_ENTITY__ENTITLEMENT
WHERE ENTITY_TYPE_ID = @ET.Agent
and ENTITY_ID = @PERSON.admin
and ENTITLEMENT_ID = @ENTLMNT.TelephonyAutoAnswer;
