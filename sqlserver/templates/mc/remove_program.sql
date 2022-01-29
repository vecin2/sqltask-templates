{%set all_programs = _db.fetch.all_programs()%}
{%set all_program_names = all_programs.column('NAME')%}
{%set __program_name = program_name | suggest(all_program_names)%}
{%set __program_id = all_programs.where(NAME=__program_name)[0]['ID']%}
DELETE FROM MC_REWARDS_PROGRAM WHERE ID ={{__program_id}}

{% set _remove_queue = remove_queue | description("Do you want to also want to remove queued email type (Y/N)") %}
{% if _remove_queue =='Y'%}
{%set __queued_email_type_id = queued_email_type_id | suggest(_keynames.QWT)%}
DELETE FROM LOCALISED_FIELD WHERE OBJECT_TYPE ='QueuedWorkTypeED' AND OBJECT_VERSION='@QWT.{{__queued_email_type_id}}';
DELETE FROM CHANN_QUEUED_EMAIL_TYPE  where ID = @QWT.{{__queued_email_type_id}}
DELETE FROM CWQ_QUEUED_WORK_TYPE where id = @QWT.{{__queued_email_type_id}}
{% endif %}
