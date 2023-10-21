SELECT v.name,ee.SYSTEM_NAME ,ld.TEXT as DISPLAY_NAME
FROM EVA_VERB_ENTITLEMENT eve
INNER JOIN EVA_VERB v ON eve.VERB_ID =v.ID
INNER JOIN EVA_ENTITLEMENT ee ON eve.ENTITLEMENT_ID = ee.ID  
LEFT JOIN LOCALISED_FIELD ld on ld.OBJECT_TYPE='EntitlementED' and ld.FIELD_NAME='displayName' and ee.SYSTEM_NAME = ld.OBJECT_INSTANCE and ld.LOCALE='{{_default_locale}}'
WHERE eve.verb_id =@V.{{verb_keyname | suggest(_keynames.V)}}
