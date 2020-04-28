DELETE 
FROM FD_USER_PROFILE_TYPE
WHERE USER_ID =@USER.{{username | suggest(_keynames.USER) }}
and PROFILE_TYPE_ID=@PROFILE.{{profile_id | suggest(_keynames.PROFILE)}};
