DELETE FROM EVA_ENTITY__ENTITLEMENT
WHERE ENTITY_TYPE_ID = @ET.Agent
{% set __person_keyname = agent | suggest(_keynames.PERSON) %}
and ENTITY_ID = @PERSON.{{__person_keyname}}
{% set entitlement_keynames = _db.fetch.entity_entitlements("@ET.Agent","@PERSON."+__person_keyname).column('KEYNAME') %}
and ENTITLEMENT_ID = @ENTLMNT.{{entitlement | suggest(entitlement_keynames)}}
