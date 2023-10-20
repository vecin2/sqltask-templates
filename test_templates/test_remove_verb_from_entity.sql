--{"entityid":"AbstractDuplicateChecker","verbid":"AbstractDuplicateCheckerConfig"}
DELETE FROM LOCALISED_FIELD where OBJECT_TYPE ='VerbED' and OBJECT_VERSION =@V.AbstractDuplicateCheckerConfig;

DELETE
FROM EVA_VERB
WHERE ID = @V.AbstractDuplicateCheckerConfig
and ENTITY_DEF_ID=@ED.AbstractDuplicateChecker;

DELETE FROM EVA_PROCESS_DESC_REFERENCE WHERE ID =@PDR.AbstractDuplicateCheckerConfig;

DELETE FROM LOCALISED_FIELD where OBJECT_TYPE ='ProcessDescriptorED' and OBJECT_VERSION =@PD.AbstractDuplicateCheckerConfig;

DELETE FROM EVA_PROCESS_DESCRIPTOR WHERE ID = @PD.AbstractDuplicateCheckerConfig;

