--{"profile_keyname":"SYSTEMADMIN","entitlement_name":"ManageTeams"}
DELETE FROM EVA_ENTITY__ENTITLEMENT
WHERE ENTITY_TYPE_ID = @ET.ProfileType
and ENTITY_ID = @PROFILE.SYSTEMADMIN
and ENTITLEMENT_ID = @ENTLMNT.ManageTeams;
