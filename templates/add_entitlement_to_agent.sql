{% set ent_entity_type = "Agent" %}
{% set entity_keyset = "PERSON" %}
{% set message = "Please note that the agent should have been created using scrips, otherwise there will be no keyname for the agent.\nThere is also issues with agents scripted with username matching out of the box usernames, e.g. 'ccagent','batchUser'... as the keyname resolves to the wrong ID."%}
{% set all_agents = _db.fetch.all_agents() %}
{% set usernames = all_agents.column("USERNAME") %}
{% set _username = username | print(message)| suggest(usernames)%}
{% set agent = all_agents.where(USERNAME=_username) %}
{% set entity_keyname = agent[0]["KEYNAME"]%}
{% include 'hidden_templates/add_entity_entitlement.sql' %}
