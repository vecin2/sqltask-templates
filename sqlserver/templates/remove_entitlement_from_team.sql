
DELETE FROM EVA_ENTITY__ENTITLEMENT
WHERE ENTITY_TYPE_ID = @ET.Team
{% set __team_keyname = team | suggest(_keynames.TEAM) %}
and ENTITY_ID = @TEAM.{{__team_keyname}}
{% set entitlement_keynames = _db.fetch.entity_entitlements("@ET.Team","@TEAM."+__team_keyname).column('KEYNAME') %}
and ENTITLEMENT_ID = @ENTLMNT.{{entitlement | suggest(entitlement_keynames)}}
