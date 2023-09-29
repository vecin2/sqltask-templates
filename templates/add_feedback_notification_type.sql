{% set help_msg ="A feedback notification type defines how the agent entering the feedback wants to be notified, e.g email. It points to an entity definition that implements 'EIAbstractFeedbackNotification', and should implement two verbs: 'inlineCreate', which is displayed when the feedback is created, and 'notifyAction', which is run within 'PostSubmitRequestAnswerWorkItem' verb and it send the notification back to the feedback requester" %}
{% set __entity_type = entity_type | suggest(_keynames.ET) %}
{% set __notification_type_name = notification_type_name  |  description("notification_type_name (e.g. Email)") | default(__entity_type)%}

INSERT INTO AKF_FEEDBACK_NOTIFICATION_TYPE (ID, ENV_ID, RELEASE_ID, ENTITY_DEF_TYPE_ID, ENTITY_DEF_TYPE_ENV_ID, NAME) VALUES (
@AFNT.{{__notification_type_name.upper()}}, --ID
@ENV.Dflt, -- ENV_ID
@RELEASE.ID, --RELEASE_ID
@ET.{{__entity_type}}, -- ENTITY_DEF_TYPE_ID
@ENV.Dflt, -- ENTITY_DEF_TYPE_ENV_ID
'{{__notification_type_name}}' --NAME
);
