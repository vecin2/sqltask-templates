{% set __dynamic_field_property_keyname = dynamic_field_property_keyname | suggest(_keynames.EDEFP) %}
{% set tagset_names = _db.fetch.tagset_names().column("NAME") %}
{% set __tagset_name = tagset_name | suggest(tagset_names) %}
{% set __is_multiselect = is_multiselect | description("is_multiselect (Y/N)") %} 
INSERT INTO EVA_DYN_ENTITY_FIELD_TAGSET_PR (TENANT_ID, ID, RELEASE_ID, TAGSET_NAME, IS_MULTISELECT) VALUES (
'default',  -- TENANT_ID
@EDEFP.{{__dynamic_field_property_keyname}},  -- ID
@RELEASE.ID,  -- RELEASE_ID
'{{__tagset_name}}',  -- TAGSET_NAME
'{{__is_multiselect}}' -- IS_MULTISELECT
);

