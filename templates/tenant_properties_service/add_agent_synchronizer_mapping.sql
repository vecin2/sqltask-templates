{% set agent_synchronizer_mappings = _tps.fetch.agent_synchronizer_property_mappings() %}
{% set help_msg = agent_synchronizer_mappings | string + "\nAbove is shown the list of existing 'agentPropertyName' mappings.\nIf nothing is displayed, enter 1 as sequence number, otherwise pick the next number available" %}
{% set __sequence_number =  sequence_number | print(help_msg) %}
{% set attribute_msg ="ssoAttributeName and ssoAttributeValue are the attributes used by the Identity Provider (IDP). Any valid string can be used both for attribute name and attribute value. You can configure the mapping rules based on your requirements." %}
{% set __sso_attribute_name = sso_attribute_name | print(attribute_msg) %}
INSERT INTO TENANT_PROPERTY
(NAME, SHORT_TEXT, LONG_TEXT, LAST_MODIFIED_BY, LAST_MODIFIED_DATE)
VALUES('agent-synchronizer.mapping.{{__sequence_number}}.ssoAttributeName', '{{__sso_attribute_name}}', NULL, 'admin', SYSDATE);

INSERT INTO TENANT_PROPERTY
(NAME, SHORT_TEXT, LONG_TEXT, LAST_MODIFIED_BY, LAST_MODIFIED_DATE)
VALUES('agent-synchronizer.mapping.{{__sequence_number}}.ssoAttributeValue', '{{ssoAttributeValue}}', NULL, 'admin', SYSDATE);

INSERT INTO TENANT_PROPERTY
(NAME, SHORT_TEXT, LONG_TEXT, LAST_MODIFIED_BY, LAST_MODIFIED_DATE)
{% set __operator = operator | suggest(["Contains","Equals"]) | default("Equals") %}
VALUES('agent-synchronizer.mapping.{{__sequence_number}}.ssoAttributeOperator', '{{operator}}', NULL, 'admin', SYSDATE);

INSERT INTO TENANT_PROPERTY
(NAME, SHORT_TEXT, LONG_TEXT, LAST_MODIFIED_BY, LAST_MODIFIED_DATE)
{% set agent_properties =["profile", "organisation", "team", "role", "givenName", "familyName", "qualityAssuranceEntitlement", "supervisor", "qualityAssuranceRatio", "saveForLaterEntitlement", "desktopLocale", "contentLocale", "homepage" ] %}
{% set __agent_property_name = agent_property_name | suggest(agent_properties) %}
VALUES('agent-synchronizer.mapping.{{__sequence_number}}.agentPropertyName', '{{__agent_property_name}}', NULL, 'admin', SYSDATE);

INSERT INTO TENANT_PROPERTY
(NAME, SHORT_TEXT, LONG_TEXT, LAST_MODIFIED_BY, LAST_MODIFIED_DATE)
VALUES('agent-synchronizer.mapping.{{__sequence_number}}.agentPropertyValue', '{{agent_property_value | print("The profile name, if the agent_property_name is \"profile\" or a team name if the agent_property_name is \"team\"")}}' , NULL, 'admin', SYSDATE);
