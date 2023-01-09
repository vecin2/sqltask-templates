{#
[short_description]
Adds a profile to an existing agent
#}
{% set profile_name = __profile_name | description("profile_name (e.g. Business Admin Profile)") %}
{% set profile_keyname = profile_name.replace(" ","") %}
INSERT INTO FD_PROFILE_TYPE (ID,ENV_ID,DESKTOP_PROCESS,IS_DELETED,NAME,SYSTEM_NAME,RELEASE_ID,TENANT_ID) 
VALUES (
	@PROFILE.{{profile_keyname}}, --ID
	@ENV.Dflt, --ENV_ID
	'{{desktop_process | default("FrameworkDesktop.Implementation.ProfileProcess.DesktopProfileProcess")}}', --DESKTOP_PROCESS
	'N', --IS_DELETED
	'{{profile_name}}', --NAME
	'{{profile_name.replace(" ","")}}', --SYSTEM_NAME
	@RELEASE.ID, --RELEASE_ID
	'default' --TENANT_ID
);
{% set add_perspectives = __add_perspectives | description("Do you want to add perspectives to the profile(y/n)?")%}

{% if add_perspectives.lower() =='y' %}
{% set profile_keyname = profile_keyname %} 
{% include 'add_perspective_to_profile.sql' %}
{% endif %}
