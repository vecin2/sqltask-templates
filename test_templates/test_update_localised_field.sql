--{"object_type":"ActionStateED","object_instance":"CANCELLED","field_name":"","locale":"en-GB","column_to_update":"OBJECT_VERSION","new_value":"'9'"}
UPDATE LOCALISED_FIELD
SET (OBJECT_VERSION) = ('9')
where OBJECT_TYPE ='ActionStateED' 
and OBJECT_INSTANCE = 'CANCELLED'
and LOCALE = 'en-GB';
