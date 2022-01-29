{% set __program_name = program_name %}
{% set _program_id = program_name.replace(" ","") %}
{% set all_issuers = _db.fetch.all_issuers()%}
{% set all_issuer_ids = all_issuers.column('NAME')%}
{% set __issuer_name = issuer_id | suggest(all_issuer_ids)%}
{% set condition = __issuer_name%}
{% set issuer_id = all_issuers.where(NAME=__issuer_name)[0]['ID'] %}
{% set program_id = _db.find.latest_program_id()['ID']+1 %}

{% set __add_queue = add_queue | description("Are you using an existing queued email type or adding a new one (Existing/New)") | default('New')%}

{% if __add_queue == 'New' %}
{% set __queued_email_type_id = _program_id %}
{% set queue_name = __program_name %}
{% include 'add_queue_email_work_type.sql' %}
{% else %}
{% set __queued_email_type_id = queued_email_type_id | suggest(_keynames.QWT) %}
{% endif %}

INSERT INTO MC_REWARDS_PROGRAM (ID, NAME, ISSUER_ID, QUEUED_EMAIL_WORK_TYPE_ID) VALUES (
				{{program_id}},
       	'{{program_name}}',
       	{{issuer_id}},
       	@QWT.{{__queued_email_type_id}}
);
