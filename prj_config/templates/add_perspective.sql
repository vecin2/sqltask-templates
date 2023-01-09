{% set description = "Adding a perspectives requires inserting into EVA_CONTEXT_CONFIG and FD_PERSPECTIVE tables" %}
{% set __perspective_name = perspective_name  | print(description) | description("perspective_name (it should be unique, e.g Agent Home)")%}
{% set perspective_keyname = __perspective_name.replace(" ","") %}
{% set new_context_desc = "Perspectives are mapped to context configurations, which define the activities that are shown in the left hand side. You can reuse and existing configuration or just create a new one" %}
{% set __is_new_context = new_context | print(new_context_desc) | description ("Create a new context configuration (y/n)") %}
{% if __is_new_context.lower() == 'y' %}
INSERT INTO EVA_CONTEXT_CONFIG (ID,ENV_ID,NAME,IS_DELETED,RELEASE_ID,TENANT_ID) VALUES (
	@CC.{{perspective_keyname}}Context,
	@ENV.Dflt,
	'{{__perspective_name}} Context',
	'N',
	@RELEASE.ID,
	'default'
);
{% set config_keyname = perspective_keyname+"Context" %}
{% endif %}

INSERT INTO FD_PERSPECTIVE (ID,ENV_ID,NAME,PERSPECTIVE_PROCESS,CONTEXT_CONFIG_ID,CONTEXT_CONFIG_ENV_ID,USER_ADDABLE,IS_DELETED,RELEASE_ID,CAN_MODIFY_DISPLAY_NAME,TENANT_ID,RUN_DESKTOP_RULES,SHOW_SUGGESTIONS_PANEL,MAX_VISIBLE_SUGGESTIONS) 
VALUES (@PPTIVE.{{perspective_keyname}},--ID
	@ENV.Dflt,--ENV_ID
	'{{__perspective_name}}', --NAME
	'{{PERSPECTIVE_PROCESS | codepath()}}', --PERSPECTIVE_PROCESS
	@CC.{{config_keyname | suggest(_keynames.CC)}},--CONTEXT_CONFIG_ID
	@ENV.Dflt, --CONTEXT_CONFIG_ENV_ID
	'{{USER_ADDABLE | default("Y")}}', --USER_ADDABLE
	'N', --IS_DELETED
	@RELEASE.ID,   --RELEASE_ID
	'Y', --CAN_MODIFY_DISPLAY_NAME
	'default', --TENANT_ID
	'{{RUN_DESKTOP_RULES | default("Y")}}', --RUN_DESKTOP_RULES
	'{{SHOW_SUGGESTIONS_PANEL | default("N")}}', --SHOW_SUGGESTIONS_PANEL
	{{MAX_VISIBLE_SUGGESTIONS | default(5)}} --MAX_VISIBLE_SUGGESTIONS
);
