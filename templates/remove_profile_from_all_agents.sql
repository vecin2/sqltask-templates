{#
[oneline_description]
Removes a profile from all the users that is currently assigned to

[long_description]
It requires the profile keyname and it suggests a list with all the profile keynames

[related_tasks]
remove_profile_from_agent.sql
#}
DELETE 
FROM FD_USER_PROFILE_TYPE
WHERE PROFILE_TYPE_ID=@PROFILE.{{profile_id | suggest(_keynames.PROFILE)}};
