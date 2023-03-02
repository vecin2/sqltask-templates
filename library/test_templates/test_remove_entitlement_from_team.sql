--{"team_keyname":"ADMINTEAM","entitlement_name":"TelephonyAutoAnswer"}
DELETE FROM EVA_ENTITY__ENTITLEMENT
WHERE ENTITY_TYPE_ID = @ET.Team
and ENTITY_ID = @TEAM.ADMINTEAM
and ENTITLEMENT_ID = @ENTLMNT.TelephonyAutoAnswer;
