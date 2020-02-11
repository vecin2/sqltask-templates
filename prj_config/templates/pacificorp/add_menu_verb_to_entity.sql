{% set default_image_path = '/CorePageSetEditor/Implementation/ScriptingMenu/UI/Images/sciboodleManageScriptingPageSetsUp64x64' %}
{% set menu_ids = _keynames.MN %}
{% set __menu_name = menu_name | description("menu_name - This will be the verb name as well(e.g. manageReports)") %}
{% set menu_id = __menu_name+"Menu" %}
INSERT INTO FD_MENU (ID, ENV_ID, NAME, IMAGE_PATH, PARENT_ID, PARENT_ENV_ID, IS_DELETED)
VALUES(
	@MN.{{menu_id}},--ID
	@ENV.Dflt,--ENV_ID
	'{{__menu_name}}',--NAME
	'{{image_path | default(default_image_path) }}',--IMAGE_PATH
       	@MN.{{parent_menu_id  | suggest(menu_ids) | default("RootMenu")}},--PARENT_ID
       	@ENV.Dflt,--IS_DELETED
       	'N'
);
--This is the verb add to the current entity
{%set process_desc_id= "entityMenu"%}
{% set process_desc_ref_id = menu_name %}
{%set pro_desc_config_id = "@MN."+menu_id%}
{%set verb_name = __menu_name %}
{% include 'add_verb_to_entity.sql' %}

--Menu are implemented as verbs within the Menu entity so we need an entry here as well
{% set entity_def_id = "Menu" %}
{% set process_desc_ref_id = menu_name %}
{% include 'add_verb_with_existing_pdr.sql' %}



