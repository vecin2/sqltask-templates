{% set __profile_keyname = profile | suggest(_keynames.PROFILE) %}
{% set entitlement_keynames = _db.fetch.entity_entitlements("@ET.ProfileType","@PROFILE."+__profile_keyname).column('KEYNAME') %}

DELETE FROM EVA_ENTITY__ENTITLEMENT
WHERE ENTITY_TYPE_ID = @ET.ProfileType
and ENTITY_ID = @PROFILE.{{__profile_keyname}}
and ENTITLEMENT_ID = @ENTLMNT.{{entitlement | suggest(entitlement_keynames)}}
