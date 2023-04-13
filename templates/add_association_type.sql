{% set description = 'Left and right name are used to compute the association name. You can enter any name that represents your entities it does need to be the entity_def_name. e.g left_name=Customer Residential and right_name=Contact, will create a association name "Customer Residential-Contact"' %}
{% set __left_name = left_name | print(description) | description("left_name (e.g. ResidentialCustomer)")%}
{% set __right_name = right_name | description("right_name (e.g. Contact)")%}
{% set association_type_keyname = __left_name + __right_name %}
INSERT INTO EVA_ASSOCIATION_TYPE (ID,ENV_ID,OWNING_ENTITY_DEF_ID,OWNING_ENTITY_DEF_ENV_ID,LEFT_NAME,RIGHT_NAME,RIGHT_ENTITY_DEF_ID,RIGHT_ENTITY_DEF_ENV_ID,MIN_OCC,MAX_OCC,ASSOCIATION_INDEX,IS_DELETED,RELEASE_ID,CREATE_ED_VIEW_NAME,EDIT_ED_VIEW_NAME,OWNING_ENTITY_DEF_TYPE_ID,OWNING_ENTITY_DEF_TYPE_ENV_ID,RIGHT_ENTITY_DEF_TYPE_ID,RIGHT_ENTITY_DEF_TYPE_ENV_ID,TENANT_ID) 
VALUES (
	@EAT.{{association_type_keyname}}, --ID
	@ENV.Dflt, --ENV_ID
	@ED.{{left_entity_keyname | suggest(_keynames.ED)}}, -- OWNING_ENTITY_DEF_ID
	@ENV.Dflt, --OWNING_ENTITY_DEF_ENV_ID
	'{{__left_name}}-{{__right_name}}', --LEFT_NAME
	'{{__right_name}}-{{__left_name}}', --RIGHT_NAME
	@ED.{{right_entity_keyname | suggest(_keynames.ED)}}, --RIGHT_ENTITY_DEF_ID
	@ENV.Dflt, --RIGHT_ENTITY_DEF_ENV_ID
	1, --MIN_OCC
	1, --MAX_OCC
	1, --ASSOCIATION_INDEX
	'N', --IS_DELETED
	@RELEASE.ID, --RELEASE_ID
	null, --CREATE_ED_VIEW_NAME
	null, --EDIT_ED_VIEW_NAME
	{% set left_entity = _db.find.ed_by_keyname(left_entity_keyname) %}
	{{left_entity["TYPE_ID"]}}, --OWNING_ENTITY_DEF_TYPE_ID
	@ENV.Dflt, --OWNING_ENTITY_DEF_TYPE_ENV_ID
	{% set right_entity = _db.find.ed_by_keyname(right_entity_keyname) %}
	{{ right_entity["TYPE_ID"] }}, --RIGHT_ENTITY_DEF_TYPE_ID
	@ENV.Dflt, --RIGHT_ENTITY_DEF_TYPE_ENV_ID
	'default' --TENANT_ID
);
