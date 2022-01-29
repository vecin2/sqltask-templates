{% set entitlements = _db.fetch.all_entitlements() %}
{% set entitlement_names = entitlements.column('SYSTEM_NAME') %}
{% set __entitlement_name = entitlement_name | suggest(entitlement_names) %}
{% set entitlement = entitlements.find(SYSTEM_NAME=__entitlement_name) %}


INSERT INTO EVA_ENTITY__ENTITLEMENT (ENTITLEMENT_ID, ENTITLEMENT_ENV_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, IS_DELETED, RELEASEID, TENANT_ID) 
VALUES (
	@ENTLMNT.{{entitlement['KEYNAME']}}, --ENTITLEMENT_ID
	@ENV.Dflt,--ENTITY_ENV_ID
       	@{{entity_keyset}}.{{entity_keyname}},
	@ENV.Dflt,--ENTITY_ENV_ID
       	@ET.{{ent_entity_type}},
       	@ENV.Dflt,
       	'N',
       	@RELEASE.ID,
       	'default');
