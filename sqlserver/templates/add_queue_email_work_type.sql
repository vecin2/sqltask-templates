{% set __queue_name = queue_name %}
{% set _queued_email_type_id = __queue_name.replace(" ","") %}
INSERT INTO CWQ_QUEUED_WORK_TYPE(ID, ENV_ID, RELEASE_ID, NAME, IS_DELETED, IS_RULES_RELEVANT, UUID, TYPE_UUID, TENANT_ID)
VALUES (
	@QWT.{{_queued_email_type_id}}, --ID
	@ENV.Dflt, --ENV_ID
       	@RELEASE.ID, --RELEASE_ID
       	'{{queue_name}}', --NAME
       	'N', --IS_DELETED
	'Y', --IS_RULES_RELEVANT
       	'{{_queued_email_type_id}}', --UUID
       	'QueuedEmailTypeED', --TYPE_UUID
       	'default' --TENANT_ID
);
INSERT INTO CHANN_QUEUED_EMAIL_TYPE (ID, ENV_ID, RELEASE_ID, TENANT_ID, FROM_ADDRESS, BOUNCE_ADDRESS, REPLY_TO_ADDRESS, AUTOREPLYTEMPLATE_MIG_REF, QATEMPLATE_MIG_REF, TAGLINETEMPLATE_MIG_REF, SIGNATURETEMPLATE_MIG_REF, MARK_AS_COMPLETE, INCLUDE_SIG_IN_AUTO_REPLY, FORWARD_ORIGINAL_EMAIL, IS_DELETED) VALUES (
@QWT.{{_queued_email_type_id}}, --ID
@ENV.Dflt, --ENV_ID
@RELEASE.ID, --RELEASE_ID
       	'default',--TENANT_ID
       	'{{from_address | description("from_email_address e.g. WestpacExtras_dev1@mastercard.com")}}', --FROM_ADDRESS
       	'{{bound_address | default("NULL")}}', --BOUNCE_ADDRESS
       	'{{reply_to_address | default("NULL")}}', --REPLY_TO_ADDRESS
       	'{{autoreplytemplate_mig_ref | default("NULL")}}', --AUTOREPLYTEMPLATE_MIG_REF
       	'{{qatemplate_mig_ref | default("NULL")}}', --qATENMPLATE_MIG_REF
       	'{{taglinetemplate_mig_ref | default("NULL")}}', --TAGLINETEMPLATE_MIG_REF
       	'{{signaturetemplate_mig_ref | default("NULL")}}', --SIGNATURETEMPLATE_MIG_REF
       	'{{mark_as_complete | default("N")}}', -- MARK_AS_COMPLETE
       	'{{include_sig_in_auto_reply | default("N")}}', --INCLUDE_SIG_IN_AUTO_REPLY
       	'{{forward_original_email | default("N")}}', --FORWARD_ORIGINAL_EMAIL
       	'N' --IS_DELETED
);
{% set object_type = "QueuedWorkTypeED" %}
{% set object_instance = _queued_email_type_id %}
{% set object_version = "@QWT."+_queued_email_type_id %}
{% set field_name = "displayName" %}
{% set text =  queue_name %}
{% set locale = _locale %}
{% include 'add_localised_field.sql' %}
