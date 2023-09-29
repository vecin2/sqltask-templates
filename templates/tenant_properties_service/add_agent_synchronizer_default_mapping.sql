{% set default_properties = ["organisation","profile","team","role"] %}
{% set __property = property | suggest(default_properties) | print("Press tab to get a popup with valid default properties") %}
{% set __value = value | print("Press tab to get a popup with valid default properties") %}
INSERT INTO TENANT_PROPERTY
(NAME, SHORT_TEXT, LONG_TEXT, LAST_MODIFIED_BY, LAST_MODIFIED_DATE)
VALUES('agent-synchronizer.mapping.default.{{__property}}', '{{__value}}', NULL, 'admin', SYSDATE);
