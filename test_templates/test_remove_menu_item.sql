--{"MENU_ID":"OrganisationMenuinlineSearch"}

DELETE FROM LOCALISED_FIELD WHERE OBJECT_TYPE ='MenuItemED' AND OBJECT_VERSION=@MNI.OrganisationMenuinlineSearch;

DELETE FROM FD_MENU_ITEM where ID = @MNI.OrganisationMenuinlineSearch;

DELETE FROM CCADMIN_IDMAP where ID  = @MNI.OrganisationMenuinlineSearch AND KEYSET = 'MNI'
