--["Customer","InlineSearchCustomer"]
DELETE FROM LOCALISED_FIELD where OBJECT_TYPE ='VerbED' and OBJECT_VERSION =@V.InlineSearchCustomer;

DELETE
FROM EVA_VERB
WHERE ID =@V.InlineSearchCustomer
and ENTITY_DEF_ID=@ED.Customer;

DELETE FROM EVA_PROCESS_DESC_REFERENCE WHERE ID =@PDR.InlineSearchCustomer;

DELETE FROM LOCALISED_FIELD where OBJECT_TYPE ='ProcessDescriptorED' and OBJECT_VERSION =@PD.InlineSearchCustomer;

DELETE FROM EVA_PROCESS_DESCRIPTOR WHERE ID = @PD.InlineSearchCustomer;

