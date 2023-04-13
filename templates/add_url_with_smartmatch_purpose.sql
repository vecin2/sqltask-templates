{#
[oneline_description]
Adds a URL and makes it available to be used in rules editor


[long_description]
A use case is setting up an inbound rule, within the Rules Editor, which calls a URL when something happens.
For example creating a customer when the customer is not identified. We could do that by making a request to create customer URL REST API. This URL needs to be previously configured and saved in the database. This is what this template does.

Currently only saves to the URL table, it does not save to FWI_URL_HEADER or FWI_URL_PARAM table. Once we encounter a use case that needs to save to those tables this template should be modified to save to those tables as well.

Note also that "EXPORT_LOCALE" is set "N", this is equivalent to make this URL non migratable, we do this because we are scripting and any modification to the rule is expected to be done through script, not using migration.
#}
{%set _display_name = display_name %}
{%set _keyname = display_name.replace(" ","") %}
{%set _host = host | suggest(_keynames.FWIH) %}
{%set _path = path | print("The url path, e.g: /customer-service/default/customers")%}
{%set request_types =["GET", "HEAD","DELETE","POST","PUT","PATCH"]%}
{%set _request_type = request_type | print("Request type could be POST,GET...") | suggest(request_types) %}
{%set content_types =["text/plain", "application/xml", "text/html", "application/json","application/ld+json","image/gif" ,"image/jpeg"]%}
{%set _content_type = content_type | print('Content type could be something like "text/plain", "application/xml", "text/html", "application/json","application/ld+json","image/gif" ,"image/jpeg"...') | suggest(content_types) %}
{%set _body = body | print('Copy the body from the request and paste below.\nThe body of the request should in line with content_type, e.g. if content "application/json" body could be something like this {firstname: "John", lastname:"Smith"}') | suggest(content_types) %}

INSERT INTO EVA_MIGRATABLE (ENTITY_ID, ENTITY_ENV_ID, RELEASE_ID, TYPE_NAME, MIGRATABLE_REFERENCE, VERSION, IS_REMOTE, ENTITY_VERSION, IS_DELETED, INCLUDE_IN_EXPORT, EXPORT_LOCALE, ENTITY_MINOR_VERSION, TENANT_ID) VALUES (
    @WIU.{{_keyname}}, --ENTITY_ID 
	@ENV.Dflt, --ENTITY_ENV_ID
	@RELEASE.ID, --RELEASE_ID
	'WebIntegrationURLED',--TYPE_NAME
	'WebIntegrationURLED-{{_display_name}}',--MIGRATABLE_REFERENCE
	'1',--VERSION
	'N',--IS_REMOTE
	0,--ENTITY_VERSION
	'N',--IS_DELETED
	'N',--INCLUDE_IN_EXPORT
	'ALL',--EXPORT_LOCALE
	0,--ENTITY_MINOR_VERSION
	'default'--TENANT_ID
);
INSERT INTO EVA_TAGSET_SELECTION
(ID, ENV_ID, RELEASE_ID, TAG_NAME, TAGSET_NAME, TENANT_ID)
VALUES(
@TS.{{_keyname}}, 
@ENV.Dflt,
@RELEASE.ID,
'systemset_notmigratable',
'systemset', 
'default');

INSERT INTO EVA_TAGSET_SELECTION
(ID, ENV_ID, RELEASE_ID, TAG_NAME, TAGSET_NAME, TENANT_ID)
VALUES(
@TS.{{_keyname}}, 
@ENV.Dflt,
@RELEASE.ID,
'upurpose_smartmatch',
'upurpose',
'default');

INSERT INTO FWI_URL
(ID, ENV_ID, RELEASE_ID, NAME, IS_DELETED, TENANT_ID, HOST_ID, "PATH", REQUEST_TYPE, CONTENT_TYPE, MESSAGE_BODY, ADD_AUTH_HEADER, AUTHORISATION_SERVER_ID)
VALUES(@WIU.{{_keyname}}, @ENV.Dflt, @RELEASE.ID, '{{display_name}}', 'N', 'default', @FWIH.{{_host}}, '{{path}}', '{{_request_type}}', '{{content_type}}', '{{_body}}', 'Y', NULL);

{% set object_type ="WebIntegrationURLED" %}
{% set object_instance = _keyname %}
{% set object_version = "@WIU."+_keyname %}
{% set field_name = "displayName" %}
{% set text = _display_name %}
{% set locale = _locale %}
{% include 'add_localised_field.sql' %}

INSERT INTO EVA_ENTITY__TAGSET_SELECTION (TENANT_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, ENTITY_TYPE_RELEASE_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_RELEASE_ID, RELATIONSHIP_TYPE, TAG_SELECTION)
VALUES (
	'default',--TENANT_ID
	@ET.EmbeddedSite,--ENTITY_TYPE_ID
	@ENV.Dflt,--ENTITY_TYPE_ENV_ID
	@RELEASE.ID,--ENTITY_TYPE_RELEASE_ID
	@WIU.{{_keyname}},--ENTITY_ID
	@ENV.Dflt,--ENTITY_ENV_ID
	@RELEASE.ID,--ENTITY_RELEASE_ID
	'urlpurposerelationshipkey',--RELATIONSHIP_TYPE
	@TS.{{_keyname}}--TAG_SELECTION
);

INSERT INTO EVA_ENTITY__TAGSET_SELECTION (TENANT_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, ENTITY_TYPE_RELEASE_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_RELEASE_ID, RELATIONSHIP_TYPE, TAG_SELECTION)
VALUES (
	'default',--TENANT_ID
	@ET.EmbeddedSite,--ENTITY_TYPE_ID
	@ENV.Dflt,--ENTITY_TYPE_ENV_ID
	@RELEASE.ID,--ENTITY_TYPE_RELEASE_ID
	@WIU.{{_keyname}},--ENTITY_ID
	@ENV.Dflt,--ENTITY_ENV_ID
	@RELEASE.ID,--ENTITY_RELEASE_ID
	'migrationRelationshipKey',--RELATIONSHIP_TYPE
	@TS.{{_keyname}}--TAG_SELECTION
);
