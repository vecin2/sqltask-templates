--{"entity_definition_keyname":"Customer","new_entity_def_name":"MyNewCustomer","new_interface_path":"my.new.interface_path","new_logical_object_path":"my.new.logical_object_path"}
UPDATE EVA_ENTITY_DEFINITION 
SET (NAME,UUID,TYPE_UUID,INTERFACE_PATH,LOGICAL_OBJ_PATH) = ('MyNewCustomer','MyNewCustomer','MyNewCustomer','my.new.interface_path','my.new.logical_object_path')
WHERE ID = @ED.Customer;

UPDATE LOCALISED_FIELD
SET (OBJECT_INSTANCE) = ('MyNewCustomer')
WHERE OBJECT_TYPE = 'EntityDefinitionED'
and OBJECT_VERSION = @ED.Customer;
