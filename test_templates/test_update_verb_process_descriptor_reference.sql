--{"entity_def_keyname":"CUSTOMER","verb_keyname":"CreateCustomer","new_process_descriptor_reference":"CallCustomer"}
UPDATE EVA_VERB
SET (PROCESS_DESC_REF_ID) = (@PDR.CallCustomer)
WHERE ID = @V.CreateCustomer;
