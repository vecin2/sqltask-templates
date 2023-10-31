{% set _agent_keyname = agent_keyname | suggest(_keynames.PERSON) %}
{% set _queue_keyname = queue_keyname | suggest(_keynames.QUEUE) %}
INSERT INTO CWQ_ENTITY__QUEUE (TENANT_ID, ENTITY_ID, ENTITY_ENV_ID, ENTITY_TYPE_ID, ENTITY_TYPE_ENV_ID, QUEUE_ID, QUEUE_ENV_ID, RELEASE_ID) 
VALUES ('default',
	@PERSON.{{_agent_keyname}},
	@ENV.Dflt,
	@ET.Agent,
	@ENV.Dflt,
	@QUEUE.{{_queue_keyname}},
	@ENV.Dflt,
	@RELEASE.ID);
