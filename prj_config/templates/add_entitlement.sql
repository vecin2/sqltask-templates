{% set __display_name = entitlement_display_name %}
{% set system_name = __display_name.replace(" ","") %}

INSERT INTO EVA_ENTITLEMENT (ID,ENV_ID,IS_DELETED,IS_WORKFLOW_ENTITLEMENT,RELEASE_ID,RESOLUTION_PROCESS,IS_CONTENT_ENTITLEMENT,SYSTEM_NAME,TENANT_ID,IS_PRIVILEGE_ENTITLEMENT,SCOPE_EXPAND_DIRECTION,IS_CONTEXT_ENTITLEMENT)
VALUES (
    @ENTLMNT.{{system_name}},--ID
    @ENV.Dflt,--ENV_ID
    'N',--IS_DELETED
    '{{is_worflow | description("is_workflow_entitlement (Y/N)")
		  | default("N")}}',--IS_WORKFLOW_ENTITLEMENT
    @RELEASE.ID, --RELEASE_ID
    null,--RESOLUTION_PROCESS
    'N', --IS_CONTENT_ENTITLEMENT
    '{{system_name}}', --SYSTEM_NAME
    'default',--TENANT_ID
    'N',--IS_PRIVILEGE_ENTITLEMENT
    null,--SCOPE_EXPAND_DIRECTION
    '{{is_context | description("is_content_entitlement (Y/N)")
		  | default("N")}}'--IS_CONTENT_ENTITLEMENT
);
{% set object_type = "EntitlementED" %}
{% set object_instance =  system_name%}
{% set object_version = "@ENTLMNT."+system_name %}
{% set text = __display_name %}
{% set field_name= 'displayName'  %}
{% include 'add_localised_field.sql' %}
