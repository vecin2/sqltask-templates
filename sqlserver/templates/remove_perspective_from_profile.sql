{%set __profile_keyname = profile_keyname | suggest(_keynames.PROFILE)%}
{% set perspective_keynames = _db.fetch.perspectives_by_profile(profile_keyname).column('KEYNAME')%}
DELETE FROM FD_PROFILE_TYPE_PERSPECTIVE 
WHERE PROFILE_ID = @PROFILE.{{__profile_keyname}}
AND PERSPECTIVE_ID = @PPTIVE.{{perspective_keyname | suggest(perspective_keynames)}};
