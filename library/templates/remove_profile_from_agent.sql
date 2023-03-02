{%set _username = username | suggest(_keynames.USER) %}
{%set _user_profiles= _db.fetch.user_profiles(_username) %}
{%set _user_profile_keynames=_user_profiles.column('PROFILE_KEYNAME')%}
{%set _profile_id = profile_id | print(_user_profiles)  | suggest(_user_profile_keynames)%}
DELETE 
FROM FD_USER_PROFILE_TYPE
WHERE USER_ID =@USER.{{_username | suggest(_keynames.USER) }}
and PROFILE_TYPE_ID=@PROFILE.{{profile_id | suggest(_user_profiles)}};
