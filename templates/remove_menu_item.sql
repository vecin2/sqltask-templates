
DELETE FROM LOCALISED_FIELD WHERE OBJECT_TYPE ='MenuItemED' AND OBJECT_VERSION=@MNI.{{menu_item_id | suggest(_keynames.MNI)}};

DELETE FROM FD_MENU_ITEM where ID = @MNI.{{menu_item_id}};

DELETE FROM CCADMIN_IDMAP where ID  = @MNI.{{menu_item_id}} AND KEYSET = 'MNI';
