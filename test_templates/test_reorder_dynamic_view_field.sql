--{"dynamic_entity":"KnowledgeSegment","view":"KnowledgeSegmentCreate","view_field":"KnowledgeSegmentCreateTopic","view_field_sequence":"3" }

--Changing View KnowledgeSegmentCreate
--make space for field  KnowledgeSegmentCreateTopic
UPDATE EVA_DYNAMIC_ENTITY_VIEW_FIELD
SET (VIEW_FIELD_SEQUENCE) =(4)
WHERE ID = @EDEVF.KnowledgeSegmentCreateKBase;
UPDATE EVA_DYNAMIC_ENTITY_VIEW_FIELD
SET (VIEW_FIELD_SEQUENCE) =(5)
WHERE ID = @EDEVF.KnowledgeSegmentCreateProduct;

--move field KnowledgeSegmentCreateTopic to position
 UPDATE EVA_DYNAMIC_ENTITY_VIEW_FIELD
 SET (VIEW_FIELD_SEQUENCE) =(3)
 WHERE ID = @EDEVF.KnowledgeSegmentCreateTopic;

