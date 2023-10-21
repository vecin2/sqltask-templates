{#
[oneline_description]
Adds reason code or avilable status codes


[long_description]

*Template Design notes*
Currently is using relatives IDs  for ID column, which is fine for this scenario.
This template could be changed to allow entering the ID manually so it matches the code on a phone system.
Ordering is computing following OTB code: CoreChannels.Implementation.ReasonCode.Integration.Adapters.ReasonCodeAdapter.getOrderingNumber

[related_tasks]
remove_reason_code.sql
#}

{% set _id =  id | print("ID is the numeric code")%}
{% set _name = name %}
{% set _system_name = system_name | default(_name) %}
{% set _description = description | default('') %}
{% set _is_default_state = is_default_state | default("N") | suggest(['Y','N']) %}
{% set _is_available_state = is_available_state | default("N") | suggest(['Y','N']) %}

-- ADDING REASON CODE '{{_name}}'
INSERT INTO GTCC_REASON_CODE
(ID, RELEASE_ID, "ORDERING", DEFAULT_STATE, AVAILABLE_STATE, SYSTEM_NAME, IS_DELETED, TENANT_ID)
VALUES(
	{{_id}},--ID
	@RELEASE.ID,--RELEASE_ID
	{{_id | int *100+100}}, --ORDERING
	'{{_is_default_state}}',--DEFAULT_STATE 
	'{{_is_available_state}}', --AVAILABLE_STATE
	'{{_name}}',--SYSTEM_NAME
	'N', --IS_DELETED
	'default' --TENANT_ID
);

{% set object_type ="ReasonCodeED" %}
{% set object_instance = _system_name.replace(" ","") %}
{% set object_version = _id %}
{% set field_name = "name" %}
{% set text = _name %}
{% set locale = _default_locale %}
{% include 'add_localised_field.sql' %}

{% set field_name = "description" %}
{% set text = _description %}
{% include 'add_localised_field.sql' %}
-- END ADDING REASON CODE '{{_name}}'
