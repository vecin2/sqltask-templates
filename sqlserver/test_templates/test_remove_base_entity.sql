--{"extension_entity_id":"Customer"}
UPDATE EVA_ENTITY_DEFINITION
SET (LOGICAL_OBJ_PATH, INTERFACE_PATH, SUPER_ENTITY_DEFINITION, SUPER_ENTITY_DEFINITION_ENV_ID) = ('CoreEntities.Implementation.Customer.Customer', 'CoreEntities.API.Interfaces.EICustomer', @ED.Person, @ENV.Dflt) 
WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt AND RELEASE_ID = @RELEASE.ID;

DELETE FROM EVA_ENTITY_DEFINITION 
WHERE ID = @ED.PreExtendedBaseCustomer;

DELETE FROM EVA_CATEGORY_ENTRY WHERE ENTITY_ID = @ED.PreExtendedBaseCustomer; 

DELETE FROM LOCALISED_FIELD 
WHERE OBJECT_VERSION = @ED.PreExtendedBaseCustomer
AND OBJECT_TYPE = 'EntityDefinitionED';

DELETE
FROM CCADMIN_IDMAP
WHERE KEYSET = 'ED'
AND ID =@ED.PreExtendedBaseCustomer;
