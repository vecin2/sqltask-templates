{% set default_display_name =  verb_name | description("create_verb_name(e.g createArticle, editFAQ, etc)")| split_uppercase() %}
{% set __verb_display_name = verb_display_name | description("verb_display_name")
			       | default(default_display_name)%}
{% set __verb_description = verb_description | description("verb_description")
			       | default(default_display_name)%}


{% set __entity_def_id ="DynamicContentCase" %}

{# next line capitalize only the first letter. We cant user capitalize or title because 
they put the  res of the letter to lower case, but we want to leave them as they are #}
{% set titled_verb_name = verb_name[0].upper() + verb_name[1:] %}
{% set default_verb_id = __entity_def_id+titled_verb_name %}
{% set __verb_id = verb_id | description("verb_id") | default(default_verb_id) %}
{% set process_descriptor_id = __verb_id %}
{% set repository_path ="AddKnowContentCase.Implementation.DynamicContentCase.Verbs.Create"%}
{% set process_descriptor_type = 'Verb' %}
{% set config_process_id = 'NULL' %}
{% include 'add_process_descriptor.sql' %}

{% set process_descriptor_ref_id = __verb_id %}
{% set pdr_config_id = dynamic_entity_keyname | suggest(_keynames.FULL_ED) %}
{% set pdr_config_type_id = 'NULL' %}
{% include 'hidden_templates/add_process_descriptor_ref.sql' %}


{% set entity_ids = _keynames.ED %}
INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE) VALUES (
@V.{{__verb_id}}, --ID
'{{verb_name}}', -- NAME
@PDR.{{process_descriptor_ref_id}}, --PROCESS_DESC_REF_ID
@ED.{{__entity_def_id | suggest(entity_ids)}}, -- ENTITY_DEF_ID
@ENV.Dflt, -- ENTITY_DEF_ENV_ID
{% set is_instance ='N' %}
'{{is_instance | description("is_instance (Y/N)")}}', --IS_INSTANCE
'N', -- IS_DEFAULT
{% if is_instance == 'N'%} {% set is_instance_default = 'N' %} {%endif%}
'{{is_instance_default | description("is_instance_default (Y/N)")}}', -- IS_INSTANCE_DEFAULT
{% set is_user_visible = 'Y' %} 
'{{is_user_visible}}' -- IS_USER_VISIBLE
);

{% set entity = _db.find.ed_by_keyname(__entity_def_id) %}
{% set object_type = "VerbED" %}
{% set object_instance =  entity["NAME"]+"__"+verb_name %}
{% set object_version = "@V."+__verb_id %}
{% set text = __verb_display_name %}
{% set field_name= 'displayName'  %}
{% include 'add_localised_field.sql' %}

{% set field_name= 'description'  %}
{% set text = __verb_description %}
{% include 'add_localised_field.sql' %}


{% set perspective_id = "KMAuthoringHome" %}
{% set entity_type = "DynamicContentCase" %}
{% set is_alphabetical_order = "Y" %}
{% include 'add_activity_to_perspective.sql' %}
