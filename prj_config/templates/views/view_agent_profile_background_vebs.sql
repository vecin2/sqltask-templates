{% set desc = "This list does not contain the AbstractChannelStateManager start (CoreChannels.Implementation.AbstractChannelStateManager.Verbs.Start). That's because that verb is no implemented by neither of their child entities CampaignStateManager,TelephonyStateManager,DialerStateManager,MessagingStateManager"%}
{%set _see_msg_above = see_msg_above | print(desc)%}
SELECT bv.id,bv.verb_name, ed.name, ed.LOGICAL_OBJ_PATH, pd.REPOSITORY_PATH
FROM FA_BACKGROUND_VERB bv, FA_ENTITY__BACKGROUND_VERB ebv, EVA_ENTITY_DEFINITION ed, eva_verb v, EVA_PROCESS_DESC_REFERENCE pdr, EVA_PROCESS_DESCRIPTOR pd
where ebv.BACKGROUND_VERB_ID = bv.ID AND ebv.RELEASE_ID = bv.RELEASE_ID
and ed.type_id =bv.ENTITY_DEF_TYPE_ID
and v.ENTITY_DEF_ID = ed.id
and v.name = bv.VERB_NAME
and v.PROCESS_DESC_REF_ID = pdr.id
and pdr.PROCESS_DESCRIPTOR_ID = pd.id
and ENTITY_ID = 1
order by ed.name;
