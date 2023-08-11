{% set __entity_keyname= entity_keyname | suggest(_keynames.ED) %}
{% set __dynamic_field_name = dynamic_field_name | description("field_name (e.g title, publicBody...)") %}
{% set keyname =__entity_keyname+__dynamic_field_name[0].upper()+__dynamic_field_name[1:]%}
{% set __entity_field_type = entity_field_type | suggest(_keynames.EFT) %}
{% set query ="SELECT FIELD_SEQUENCE FROM EVA_DYNAMIC_ENTITY_FIELD WHERE ENTITY_DEF_ID = @ED.{} ORDER BY FIELD_SEQUENCE DESC".format(__entity_keyname) %}
{% set entity_fields =_database.fetch(query) %}
{% if entity_fields | length > 0 %}
 {% set default_seq =entity_fields[0]["FIELD_SEQUENCE"] +1%}
 {% else %}
 {% set default_seq =1 %}
{%endif%}

{% set __default_display_field_name = __dynamic_field_name |split_uppercase()%}
{% set __dynamic_field_display_name = dynamic_field_display_name | default(__default_display_field_name)%}
--ADD FIELD {{keyname}}
INSERT INTO EVA_DYNAMIC_ENTITY_FIELD (ID, ENTITY_DEF_ID, NAME, INITIAL_VALUE, FIELD_TYPE_ID, FIELD_SEQUENCE, ENTITY_DEF_ENV_ID)
VALUES (@EDEF.{{keyname}}, @ED.{{__entity_keyname}}, '{{__dynamic_field_name}}', '', @EFT.{{__entity_field_type}}, {{sequence | default(default_seq)}}, @ENV.Dflt);


{% set object_type ="DynamicEntityDefinitionED" %}
{% set object_instance = _db.find.ed_by_keyname(__entity_keyname)["NAME"] %}
{% set object_version = "@ED." +entity_keyname %}
{% set field_name = "fields."+__dynamic_field_name+".displayName" %}
{% set text = __dynamic_field_display_name %}
{% set locale = _locale %}
{% include 'add_localised_field.sql' %} 

INSERT INTO EVA_DYN_ENT_FIELD_PROPERTIES (ID, RELEASE_ID, FIELD_ID, ENTITY_DEF_TYPE_ID,ENTITY_DEF_TYPE_ENV_ID) 
VALUES (@EDEFP.{{keyname}}, @RELEASE.ID, @EDEF.{{keyname}}, @ET.{{property_type}},@ENV.Dflt);
