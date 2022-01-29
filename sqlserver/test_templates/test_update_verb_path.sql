--{"process_descriptor_id":"EditVerb","new_process_path":"Customer.Implementation.MyProcess"}
UPDATE EVA_PROCESS_DESCRIPTOR
SET (REPOSITORY_PATH) = ('Customer.Implementation.MyProcess')
WHERE ID = @PD.EditVerb;
