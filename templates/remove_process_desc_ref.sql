{%set process_desc_ref_keyname = _process_desc_ref_keyname | suggest(_keynames.PDR)%}
{% set process_descriptor_keyname = _db.find.pdr_by_keyname(process_desc_ref_keyname)['PD_KEYNAME'] %}

DELETE FROM EVA_PROCESS_DESC_REFERENCE 
WHERE ID = @PDR.{{process_desc_ref_keyname}};

DELETE FROM LOCALISED_FIELD 
WHERE OBJECT_TYPE ='ProcessDescriptorED'
AND OBJECT_VERSION='@PD.{{process_descriptor_keyname}}';

DELETE FROM EVA_PROCESS_DESCRIPTOR
WHERE ID = @PD.{{process_descriptor_keyname}};

DELETE FROM CCADMIN_IDMAP 
WHERE KEYSET IN ('PDR','PD') AND KEYNAME = '{{process_descriptor_keyname}}';
