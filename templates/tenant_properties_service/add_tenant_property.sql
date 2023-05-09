{% set property_names = ["theme.default.logo","theme.default.em-enterprise-desktop.application-title","text.editor.fonts"] %}
{% set help_message = "Suggested property names are only a few examples. There will be property names that are valid and are not included in the suggested list." %}
INSERT INTO TENANT_PROPERTY
(NAME, SHORT_TEXT, LONG_TEXT, LAST_MODIFIED_BY, LAST_MODIFIED_DATE)
VALUES('{{property_name | print(help_message) | suggest(property_names)}}', '{{short_text}}', NULL, 'admin', SYSDATE);

