--{"program_name":"My Test Program","issuer_name":"API Aspire","add_queue":"New","from_address":"test@mastercard.com","bounce_address":"bounce@mastercard.com","repply_to_address":"reply_to_address@mastercard.com","autoreplytemplate_mig_ref":"abcedfhi","qatemplate_mig_ref":"12345abc","taglinetemplate_mig_ref":"NULL","signaturetemplate_mig_ref":"123abcdef","mark_as_complete":"Y","include_sig_in_auto_reply":"N","forward_original_email":"N"}

INSERT INTO CWQ_QUEUED_WORK_TYPE(ID, ENV_ID, RELEASE_ID, NAME, IS_DELETED, IS_RULES_RELEVANT, UUID, TYPE_UUID, TENANT_ID)
VALUES (
        @QWT.MyTestProgram, --ID
        @ENV.Dflt, --ENV_ID
        @RELEASE.ID, --RELEASE_ID
        'My Test Program', --NAME
        'N', --IS_DELETED
        'Y', --IS_RULES_RELEVANT
        'MyTestProgram', --UUID
        'QueuedEmailTypeED', --TYPE_UUID
        'default' --TENANT_ID
);
INSERT INTO CHANN_QUEUED_EMAIL_TYPE (ID, ENV_ID, RELEASE_ID, TENANT_ID, FROM_ADDRESS, BOUNCE_ADDRESS, REPLY_TO_ADDRESS, AUTOREPLYTEMPLATE_MIG_REF, QATEMPLATE_MIG_REF, TAGLINETEMPLATE_MIG_REF, SIGNATURETEMPLATE_MIG_REF, MARK_AS_COMPLETE, INCLUDE_SIG_IN_AUTO_REPLY, FORWARD_ORIGINAL_EMAIL, IS_DELETED) VALUES (
        @QWT.MyTestProgram, --ID
        @ENV.Dflt, --ENV_ID
        @RELEASE.ID, --RELEASE_ID
        'default',--TENANT_ID
        'test@mastercard.com', --FROM_ADDRESS
        'bounce@mastercard.com', --BOUNCE_ADDRESS
        'reply_to_address@mastercard.com', --REPLY_TO_ADDRESS
        'abcedfhi', --AUTOREPLYTEMPLATE_MIG_REF
        '12345abc', --qATENMPLATE_MIG_REF
        'NULL', --TAGLINETEMPLATE_MIG_REF
        '123abcdef', --SIGNATURETEMPLATE_MIG_REF
        'Y', -- MARK_AS_COMPLETE
        'N', --INCLUDE_SIG_IN_AUTO_REPLY
        'N', --FORWARD_ORIGINAL_EMAIL
        'N' --IS_DELETED
);
INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'QueuedWorkTypeED', -- OBJECT_TYPE
'MyTestProgram', -- OBJECT_INSTANCE
@QWT.MyTestProgram, -- OBJECT_VERSION
'displayName', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'My Test Program', --TEXT
'N' --IS_DELETED
);

INSERT INTO MC_REWARDS_PROGRAM (ID, NAME, ISSUER_ID, QUEUED_EMAIL_WORK_TYPE_ID) 
VALUES (
	114,
       	'My Test Program',
       	44,
       	@QWT.MyTestProgram
);
