--{"verb_name":"inlineEdit","verb_display_name":"Inline Edit","verb_description":"Allows editing the customer inline","entity_def_id":"Customer","process_desc_ref_id":"PCCustomerInlineEdit","process_desc_id":"PCCustomerInlineEdit","repository_path":"PCCustomer.Verbs.CustomerInlineEdit","config_process_id":"NULL","process_descriptor_type":"","locale":"en-US","config_id":"NULL","is_instance":"Y","is_default":"N","is_user_visible":"Y","record_for_wrapup":"N"}

INSERT INTO EVA_PROCESS_DESCRIPTOR (ID, ENV_ID, NAME, REPOSITORY_PATH, CONFIG_PROCESS_ID, IS_DELETED,TYPE) VALUES (
@PD.PCCustomerInlineEdit, -- ID
@ENV.Dflt, -- ENV_ID
'PCCustomerInlineEdit', -- NAME
'PCCustomer.Verbs.CustomerInlineEdit', -- REPOSITORY_PATH
NULL, --CONFIG_PROCESS_ID
'N', --IS_DELETED
@PDT.Verb --TYPE
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'ProcessDescriptorED', -- OBJECT_TYPE
'PCCustomerInlineEdit__PCCustomer/Verbs/CustomerInlineEdit', -- OBJECT_INSTANCE
@PD.PCCustomerInlineEdit, -- OBJECT_VERSION
'displayName', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'PCCustomerInlineEdit', -- TEXT
'N'
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'ProcessDescriptorED', -- OBJECT_TYPE
'PCCustomerInlineEdit__PCCustomer/Verbs/CustomerInlineEdit', -- OBJECT_INSTANCE
@PD.PCCustomerInlineEdit, -- OBJECT_VERSION
'description', -- FIELD_NAME
'en-US', -- LOCALE
'default', -- LOOKUP_LOCALE
'PCCustomerInlineEdit', -- TEXT
'N'
);

INSERT INTO EVA_PROCESS_DESC_REFERENCE (ID, PROCESS_DESCRIPTOR_ID, PROCESS_DESCRIPTOR_ENV_ID, CONFIG_ID, CONFIG_TYPE_ID, IS_SHARED) VALUES (
@PDR.PCCustomerInlineEdit, --ID
@PD.PCCustomerInlineEdit, --PROCESS_DESCRIPTOR_ID
@ENV.Dflt, --PROCESS_DESCRIPTOR_ENV_ID
NULL, --CONFIG_ID
NULL, --config_type_id
'N' -- IS_SHARED
);

INSERT INTO EVA_VERB (ID, NAME, PROCESS_DESC_REF_ID, ENTITY_DEF_ID, ENTITY_DEF_ENV_ID, IS_INSTANCE, IS_DEFAULT, IS_INSTANCE_DEFAULT, IS_USER_VISIBLE,RECORD_FOR_WRAPUP) VALUES (
@V.CustomerInlineEdit, --ID
'inlineEdit', -- NAME
@PDR.PCCustomerInlineEdit, --PROCESS_DESC_REF_ID
@ED.Customer, -- ENTITY_DEF_ID
@ENV.Dflt, -- ENTITY_DEF_ENV_ID
'Y', --IS_INSTANCE
'N', -- IS_DEFAULT
'N', -- IS_INSTANCE_DEFAULT
'Y', -- IS_USER_VISIBLE
'N' -- RECORD_FOR_WRAPUP
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'VerbED',-- OBJECT_TYPE
'CustomerED__inlineEdit',-- OBJECT_INSTANCE
@V.CustomerInlineEdit,-- OBJECT_VERSION
'displayName',-- FIELD_NAME
'en-US',-- LOCALE
'default', -- LOOKUP_LOCALE
'Inline Edit', -- TEXT
'N'
);

INSERT INTO LOCALISED_FIELD (OBJECT_TYPE, OBJECT_INSTANCE, OBJECT_VERSION, FIELD_NAME, LOCALE, LOOKUP_LOCALE,TEXT,IS_DELETED) VALUES (
'VerbED',-- OBJECT_TYPE
'CustomerED__inlineEdit',-- OBJECT_INSTANCE
@V.CustomerInlineEdit,-- OBJECT_VERSION
'description', -- FIELD_NAME
'en-US',-- LOCALE
'default', -- LOOKUP_LOCALE
'Allows editing the customer inline', -- TEXT
'N'
);
