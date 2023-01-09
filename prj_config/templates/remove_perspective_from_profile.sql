DELETE FROM FD_PROFILE_TYPE_PERSPECTIVE 
WHERE PROFILE_ID = @PROFILE.{{profile_keyname | suggest(_keynames.PROFILE)}}
AND PERSPECTIVE_ID = @PPTIVE.{{perspective_keyname | suggest(_keynames.PPTIVE)}};
