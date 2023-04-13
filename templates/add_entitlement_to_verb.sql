{% set __entity_keyname = entity_keyname | description("entity_keyname (Entity which owns the verb)") | suggest(_keynames.ED) %}
{% set entity_verbs = _db.fetch.verbs_by_ed(__entity_keyname).column('KEYNAME')%}
{% set __verb_keyname = verb_keyname | suggest(entity_verbs)%}
INSERT INTO EVA_VERB_ENTITLEMENT (ENTITLEMENT_ID,ENTITLEMENT_ENV_ID,VERB_ID,RELEASE_ID,TENANT_ID) 
VALUES (
	@ENTLMNT.{{entitlement_keyname | suggest(_keynames.ENTLMNT)}}, --ENTITLEMENT_ID
	@ENV.Dflt, --ENTITLEMENT_ENV_ID
	@V.{{__verb_keyname}}, --VERB_ID
	@RELEASE.ID, --RELEASE_ID
	'default' --TENANT_ID
	);
