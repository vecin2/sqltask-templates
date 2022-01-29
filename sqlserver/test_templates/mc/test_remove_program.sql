--{"program_name":"Altura","remove_queue":"Y","queueEmailTypeKeyName":"Generic"}

DELETE FROM MC_REWARDS_PROGRAM   WHERE ID =1
DELETE FROM CHANN_QUEUED_EMAIL_TYPE  where ID = @QWT.Generic
