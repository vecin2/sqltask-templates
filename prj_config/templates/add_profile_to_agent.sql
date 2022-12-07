{%set suggested_profiles = _db.fetch.all_active_profiles().column('KEYNAME') %}
INSERT INTO FD_USER_PROFILE_TYPE (TENANT_ID, USER_ID, PROFILE_TYPE_ID, PROFILE_TYPE_ENV_ID, IS_DELETED)
VALUES ('default',
        @USER.{{username | suggest(_keynames.USER) }}, 
        @PROFILE.{{profile_id | suggest(suggested_profiles)}}, 666, 'N');
