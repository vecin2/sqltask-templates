INSERT INTO FD_USER_PROFILE_TYPE (TENANT_ID, USER_ID, PROFILE_TYPE_ID, PROFILE_TYPE_ENV_ID, IS_DELETED)
VALUES ('default',
        @USER.{{username | suggest(_keynames.USER) }}, 
        @PROFILE.{{profile_id | suggest(_keynames.PROFILE)}}, 666, 'N');