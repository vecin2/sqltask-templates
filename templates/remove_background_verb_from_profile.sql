
DELETE FROM FA_ENTITY__BACKGROUND_VERB
WHERE ENTITY_ID = @PROFILE.{{profile_keyname | suggest(_keynames.PROFILE)}}
AND ENTITY_TYPE_ID = @ET.ProfileType
AND BACKGROUND_VERB_ID= @BV.{{background_verb_keyname | suggest(_keynames.BV)}};
