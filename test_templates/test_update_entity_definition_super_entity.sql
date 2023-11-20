--{"entity_definition_keyname":"Customer","super_entity_def_keyname":"BasicEntity"}
UPDATE EVA_ENTITY_DEFINITION 
SET (SUPER_ENTITY_DEFINITION) = (@ED.BasicEntity)
WHERE ID = @ED.Customer;
