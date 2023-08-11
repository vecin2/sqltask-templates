{% set __dynamic_entity_field = dynamic_entity_field | suggest(_keynames.EDEF) %}
{% set __entitlement = entitlement | suggest(_keynames.ENTLMNT) %}
{% set type_help_message = "Entitlement type could be VIEW, EDIT or BOTH" %}
{% set __entitlement_type = entitlement_type | suggest(["VIEW","EDIT","BOTH"]) | print(type_help_message) %}

{% if __entitlement_type == "EDIT" or __entitlement_type =="BOTH" %}
INSERT INTO EVA_DYNAMIC_ENTITY_ENTITLEMENT (FIELD_ID, FIELD_REL_ID, ENTITLEMENT_ID, ENTITLEMENT_ENV_ID, ENTITLEMENT_REL_ID, TYPE) 
VALUES (
	@EDEF.{{__dynamic_entity_field}},
	@RELEASE.ID,
	@ENTLMNT.{{__entitlement}},
	@ENV.Dflt,
	@RELEASE.ID,
	0 --EDIT_ENTITLEMENT_TYPE
);
{% endif %}

{% if __entitlement_type == "VIEW" or __entitlement_type =="BOTH" %}
INSERT INTO EVA_DYNAMIC_ENTITY_ENTITLEMENT (FIELD_ID, FIELD_REL_ID, ENTITLEMENT_ID, ENTITLEMENT_ENV_ID, ENTITLEMENT_REL_ID, TYPE) 
VALUES (
	@EDEF.{{__dynamic_entity_field}},
	@RELEASE.ID,
	@ENTLMNT.{{__entitlement}},
	@ENV.Dflt,
	@RELEASE.ID,
	1 --VIEW_ENTITLEMENT_TYPE
);
{% endif %}
