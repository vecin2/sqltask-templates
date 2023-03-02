--No need to create a new entity definition, because  pre-extended 
--customer object is provided OTB to facilate customer extensions
{%set message="If path ends with '.xml' the extension will be removed from the path when generating the template %"%}
UPDATE EVA_ENTITY_DEFINITION 
SET (LOGICAL_OBJ_PATH) = ('{{logical_object_path | print(message) | codepath() |replace(".xml","") }}') 
WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt;

UPDATE EVA_ENTITY_DEFINITION 
SET (INTERFACE_PATH) = ('{{interface_path | print(message) | codepath() |replace(".xml","")}}') 
WHERE ID = @ED.Customer AND ENV_ID = @ENV.Dflt;
