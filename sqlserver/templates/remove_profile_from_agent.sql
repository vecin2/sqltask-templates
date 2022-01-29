DELETE 
FROM FD_USER_PROFILE_TYPE
WHERE USER_ID =@USER.{{username | suggest(_keynames.USER) }}
{% set profiles = _db.fetch.user_profiles(username).column('KEYNAME')%}

and PROFILE_TYPE_ID=@PROFILE.{{profile_id | suggest(profiles)}};
