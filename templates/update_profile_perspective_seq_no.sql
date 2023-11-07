{% set __profile_keyname = profile_keyname | suggest(_keynames.PROFILE) %}
{% set profile_pespectives = _db.fetch.perspectives_by_profile(__profile_keyname) %}
{% set __perspective_keyname = perspective_keyname | suggest(_keynames.PPTIVE) | print(profile_pespectives) %}
{% set __seq_no = seq_no %}

UPDATE  FD_PROFILE_TYPE_PERSPECTIVE 
set (SEQ_NO) = ({{__seq_no}})
WHERE PROFILE_ID = @PROFILE.{{__profile_keyname}}
AND PERSPECTIVE_ID = @PPTIVE.{{__perspective_keyname}};
