all_properties=SELECT NAME, SHORT_TEXT, LONG_TEXT FROM TENANT_PROPERTY tp ORDER BY NAME
agent_synchronizer_property_mappings=SELECT NAME,SHORT_TEXT FROM TENANT_PROPERTY tp WHERE NAME LIKE 'agent-synchronizer.mapping.%' AND NAME LIKE '%agentPropertyName%' ORDER BY NAME;
