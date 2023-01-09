{% set __is_new_perspective = is_new__perspective | description("Are you creating a new perspective?(y/n)") %}
{% if __is_new_perspective.lower() == 'y' %}
{% include 'add_perspective.sql' %}
{% endif %}

INSERT INTO FD_PROFILE_TYPE_PERSPECTIVE (PROFILE_ID,PROFILE_ENV_ID,PERSPECTIVE_ID,PERSPECTIVE_ENV_ID,SEQ_NO,RELEASE_ID,TENANT_ID,CONTEXT_UPDATER_DEFAULT) VALUES (
	@PROFILE.{{profile_keyname | suggest(_keynames.PROFILE)}}, --PROFILE_ID
	@ENV.Dflt, --PROFILE_ENV_ID
	@PPTIVE.{{perspective_keyname | suggest(_keynames.PPTIVE)}}, --PERSPECTIVE_ID
	@ENV.Dflt, --PERSPECTIVE_ENV_ID
	{% set perspectives = _db.fetch.perspectives_by_profile(profile_keyname) %}
	{% set default_seq_no = 0 %}
	{% if perspectives | length > 0%}
	{% set default_seq_no = perspectives[0]['SEQ_NO'] + 1%}
	{% endif %}
	{{seq_no | default(default_seq_no)}}, --SEQ_NO
	@RELEASE.ID, --RELEASE_ID
	'default', --TENANT_ID
	'N' --CONTEXT_UPDATER_DEFAULT
);

