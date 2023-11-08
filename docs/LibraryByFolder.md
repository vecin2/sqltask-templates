
SQLTask Library
===============


This  library has currently a total of 140 templates, divided in 8 sections; 92 [scripts](#scripts), 12 [hidden_templates](#hidden_templates), 1 [pepi-one](#pepi-one), 1 [pepi_one](#pepi_one), 5 [tenant_properties_service](#tenant_properties_service), 21 [views](#views), 7 [tutorials](#tutorials), 1 [oracle](#oracle)

Tables of Contents
==================

* [scripts](#scripts)
	* [Add Activity To Pers Demo](#add-activity-to-pers-demo)
	* [Add Activity To Perspective](#add-activity-to-perspective)
	* [Add Activity To Perspective With Seq No](#add-activity-to-perspective-with-seq-no)
	* [Add Agent For Commit](#add-agent-for-commit)
	* [Add Agent For Dev](#add-agent-for-dev)
	* [Add Agent To Queue](#add-agent-to-queue)
	* [Add All Background Verbs From Another Profile](#add-all-background-verbs-from-another-profile)
	* [Add Association Type](#add-association-type)
	* [Add Background Verb](#add-background-verb)
	* [Add Background Verb To Profile](#add-background-verb-to-profile)
	* [Add Basic Entity Definition](#add-basic-entity-definition)
	* [Add Category](#add-category)
	* [Add Content Field Index Mapping](#add-content-field-index-mapping)
	* [Add Content Type](#add-content-type)
	* [Add Dynamic Content Verb](#add-dynamic-content-verb)
	* [Add Dynamic Entity](#add-dynamic-entity)
	* [Add Dynamic Entity Def](#add-dynamic-entity-def)
	* [Add Dynamic Entity String Field](#add-dynamic-entity-string-field)
	* [Add Dynamic Entity Tagset Field](#add-dynamic-entity-tagset-field)
	* [Add Dynamic Entity View](#add-dynamic-entity-view)
	* [Add Dynamic Entity View Field](#add-dynamic-entity-view-field)
	* [Add Entitlement](#add-entitlement)
	* [Add Entitlement To Agent](#add-entitlement-to-agent)
	* [Add Entitlement To Dynamic Entity Field](#add-entitlement-to-dynamic-entity-field)
	* [Add Entitlement To Profile](#add-entitlement-to-profile)
	* [Add Entitlement To Team](#add-entitlement-to-team)
	* [Add Entitlement To Verb](#add-entitlement-to-verb)
	* [Add Entity Definition](#add-entity-definition)
	* [Add Feedback Notification Type](#add-feedback-notification-type)
	* [Add Localised Field](#add-localised-field)
	* [Add Menu Item](#add-menu-item)
	* [Add Migration Domain](#add-migration-domain)
	* [Add Perspective](#add-perspective)
	* [Add Perspective To Profile](#add-perspective-to-profile)
	* [Add Process Descriptor](#add-process-descriptor)
	* [Add Profile](#add-profile)
	* [Add Profile To Agent](#add-profile-to-agent)
	* [Add Reason Code](#add-reason-code)
	* [Add Report](#add-report)
	* [Add Static Menu](#add-static-menu)
	* [Add Tab To Ad Right Panel](#add-tab-to-ad-right-panel)
	* [Add Tag](#add-tag)
	* [Add Team](#add-team)
	* [Add Team Position](#add-team-position)
	* [Add Team Role](#add-team-role)
	* [Add Team Role Type](#add-team-role-type)
	* [Add Url With Smartmatch Purpose](#add-url-with-smartmatch-purpose)
	* [Add Url With Smartmatch Purpose Rollback](#add-url-with-smartmatch-purpose-rollback)
	* [Add Verb To Entity](#add-verb-to-entity)
	* [Add Verb With Existing Pdr](#add-verb-with-existing-pdr)
	* [Add View Contact Tab](#add-view-contact-tab)
	* [Add Web Integration Host](#add-web-integration-host)
	* [Change Max Count Work Area](#change-max-count-work-area)
	* [Config New Content Type](#config-new-content-type)
	* [Extend Customer](#extend-customer)
	* [Extend Entity](#extend-entity)
	* [Extend Verb](#extend-verb)
	* [Extend Verb With Config](#extend-verb-with-config)
	* [Register Channel State Manager Listener](#register-channel-state-manager-listener)
	* [Remove Activity From Perspective](#remove-activity-from-perspective)
	* [Remove Agent For Dev](#remove-agent-for-dev)
	* [Remove Background Verb From Profile](#remove-background-verb-from-profile)
	* [Remove Base Entity](#remove-base-entity)
	* [Remove Entitlement From Agent](#remove-entitlement-from-agent)
	* [Remove Entitlement From Profile](#remove-entitlement-from-profile)
	* [Remove Entitlement From Team](#remove-entitlement-from-team)
	* [Remove Entitlement From Verb](#remove-entitlement-from-verb)
	* [Remove Entity Definition](#remove-entity-definition)
	* [Remove Menu Item](#remove-menu-item)
	* [Remove Perspective From Profile](#remove-perspective-from-profile)
	* [Remove Process Desc Ref](#remove-process-desc-ref)
	* [Remove Profile From Agent](#remove-profile-from-agent)
	* [Remove Profile From All Agents](#remove-profile-from-all-agents)
	* [Remove Reason Code](#remove-reason-code)
	* [Remove Tab From Ad Right Panel](#remove-tab-from-ad-right-panel)
	* [Remove Tagset And All Tags](#remove-tagset-and-all-tags)
	* [Remove Team](#remove-team)
	* [Remove Team Role](#remove-team-role)
	* [Remove Team Role Type](#remove-team-role-type)
	* [Remove Verb From Entity](#remove-verb-from-entity)
	* [Remove View Contact Tab](#remove-view-contact-tab)
	* [Reorder Dynamic View Field](#reorder-dynamic-view-field)
	* [Set Entity Default Instance Verb](#set-entity-default-instance-verb)
	* [Unregister Channel State Manager Listener](#unregister-channel-state-manager-listener)
	* [Update Agent Password](#update-agent-password)
	* [Update Ccadmin Version](#update-ccadmin-version)
	* [Update Localised Field](#update-localised-field)
	* [Update Profile Perspective Seq No](#update-profile-perspective-seq-no)
	* [Update Url With Smartmatch Purpose](#update-url-with-smartmatch-purpose)
	* [Update Verb Path](#update-verb-path)
	* [Update Verb Process Descriptor Reference](#update-verb-process-descriptor-reference)
	* [Update Verb User Visible Flag](#update-verb-user-visible-flag)
* [hidden_templates](#hidden_templates)
	* [Add Dynamic Entity Field Without Specific Props](#add-dynamic-entity-field-without-specific-props)
	* [Add Dynamic String Field Property](#add-dynamic-string-field-property)
	* [Add Dynamic Tagset Field Property](#add-dynamic-tagset-field-property)
	* [Add Entity Entitlement](#add-entity-entitlement)
	* [Add Process Descriptor Ref](#add-process-descriptor-ref)
	* [Base Add Entity Def](#base-add-entity-def)
	* [Generic Set Update Values](#generic-set-update-values)
	* [Insert Context Verb Entry](#insert-context-verb-entry)
	* [Insert Dynamic Verb List](#insert-dynamic-verb-list)
	* [Insert Dynamic Verb Parameter](#insert-dynamic-verb-parameter)
	* [Remove Dynamic Verb List](#remove-dynamic-verb-list)
	* [Remove Idmap](#remove-idmap)
* [pepi-one](#pepi-one)
	* [Test](#test)
* [pepi_one](#pepi_one)
	* [Test](#test)
* [tenant_properties_service](#tenant_properties_service)
	* [Add Agent Synchronizer Default Mapping](#add-agent-synchronizer-default-mapping)
	* [Add Agent Synchronizer Mapping](#add-agent-synchronizer-mapping)
	* [Add Tenant Property](#add-tenant-property)
	* [Remove Tenant Property](#remove-tenant-property)
	* [Update Tenant Property](#update-tenant-property)
* [views](#views)
	* [View Tps Property](#view-tps-property)
	* [View Ad Right Panel Tabs Verbs](#view-ad-right-panel-tabs-verbs)
	* [View Agent](#view-agent)
	* [View Agent Profile Background Vebs](#view-agent-profile-background-vebs)
	* [View Channel State Manager Listeners](#view-channel-state-manager-listeners)
	* [View Entitlements By System Name](#view-entitlements-by-system-name)
	* [View Entity Definition](#view-entity-definition)
	* [View Entity Displayed Verbs](#view-entity-displayed-verbs)
	* [View Entity Verbs](#view-entity-verbs)
	* [View Entity Verbs Keynames](#view-entity-verbs-keynames)
	* [View Entitydef By Keyname](#view-entitydef-by-keyname)
	* [View Keynames](#view-keynames)
	* [View Keynames By Id](#view-keynames-by-id)
	* [View Process Descriptor Ref By Repo Path](#view-process-descriptor-ref-by-repo-path)
	* [View Process Descriptor Reference From Repo Path](#view-process-descriptor-reference-from-repo-path)
	* [View Profile Entitlements](#view-profile-entitlements)
	* [View Profile Verbs](#view-profile-verbs)
	* [View User Profiles](#view-user-profiles)
	* [View Verb By Keyname](#view-verb-by-keyname)
	* [View Verb Entitlements](#view-verb-entitlements)
	* [View Verbs From Repo Path](#view-verbs-from-repo-path)
* [tutorials](#tutorials)
	* [Filters](#filters)
	* [Globals And String Functions Tutorial](#globals-and-string-functions-tutorial)
	* [How To Add Content Type](#how-to-add-content-type)
	* [Include](#include)
	* [Keynames](#keynames)
	* [Querying Db](#querying-db)
	* [Variable And Prompts](#variable-and-prompts)
* [oracle](#oracle)
	* [View Table Name From Foreign Key Name](#view-table-name-from-foreign-key-name)

# scripts
  
There are currently 92 templates in this section
## Add Activity To Pers Demo
  
*Template:* [add_activity_to_pers_demo.sql](../templates/add_activity_to_pers_demo.sql)



  

## Add Activity To Perspective
  
*Template:* [add_activity_to_perspective.sql](../templates/add_activity_to_perspective.sql)  
*Test:* [test_add_activity_to_perspective.sql](../test_templates/test_add_activity_to_perspective.sql)  
*Related Tasks:* [Remove Activity From Perspective](#remove-activity-from-perspective), [Update Verb User Visible Flag](#update-verb-user-visible-flag), [Set Entity Default Instance Verb](#set-entity-default-instance-verb)



  

## Add Activity To Perspective With Seq No
  
*Template:* [add_activity_to_perspective_with_seq_no.sql](../templates/add_activity_to_perspective_with_seq_no.sql)  
*Test:* [test_add_activity_to_perspective_with_seq_no.sql](../test_templates/test_add_activity_to_perspective_with_seq_no.sql)



  

## Add Agent For Commit
  
*Template:* [add_agent_for_commit.sql](../templates/add_agent_for_commit.sql)



  

## Add Agent For Dev
  
*Template:* [add_agent_for_dev.sql](../templates/add_agent_for_dev.sql)  
*Test:* [test_add_agent_for_dev.sql](../test_templates/test_add_agent_for_dev.sql)



  

## Add Agent To Queue
  
*Template:* [add_agent_to_queue.sql](../templates/add_agent_to_queue.sql)  
*Test:* [test_add_agent_to_queue.sql](../test_templates/test_add_agent_to_queue.sql)



  

## Add All Background Verbs From Another Profile
  
*Template:* [add_all_background_verbs_from_another_profile.sql](../templates/add_all_background_verbs_from_another_profile.sql)



  

## Add Association Type
  
*Template:* [add_association_type.sql](../templates/add_association_type.sql)  
*Test:* [test_add_association_type.sql](../test_templates/test_add_association_type.sql)



  

## Add Background Verb
  
*Template:* [add_background_verb.sql](../templates/add_background_verb.sql)  
*Test:* [test_add_background_verb.sql](../test_templates/test_add_background_verb.sql)



  

## Add Background Verb To Profile
  
*Template:* [add_background_verb_to_profile.sql](../templates/add_background_verb_to_profile.sql)  
*Test:* [test_add_background_verb_to_profile.sql](../test_templates/test_add_background_verb_to_profile.sql)



  

## Add Basic Entity Definition
  
*Template:* [add_basic_entity_definition.sql](../templates/add_basic_entity_definition.sql)



  

## Add Category
  
*Template:* [add_category.sql](../templates/add_category.sql)  
*Test:* [test_add_category.sql](../test_templates/test_add_category.sql)



  

## Add Content Field Index Mapping
  
*Template:* [add_content_field_index_mapping.groovy](../templates/add_content_field_index_mapping.groovy)  
*Test:* [test_add_content_field_index_mapping.groovy](../test_templates/test_add_content_field_index_mapping.groovy)



  

## Add Content Type
  
*Template:* [add_content_type.sql](../templates/add_content_type.sql)  
*Test:* [test_add_content_type.sql](../test_templates/test_add_content_type.sql)



  

## Add Dynamic Content Verb
  
*Template:* [add_dynamic_content_verb.sql](../templates/add_dynamic_content_verb.sql)  
*Test:* [test_add_dynamic_content_verb.sql](../test_templates/test_add_dynamic_content_verb.sql)



  

## Add Dynamic Entity
  
*Template:* [add_dynamic_entity.sql](../templates/add_dynamic_entity.sql)  
*Test:* [test_add_dynamic_entity.sql](../test_templates/test_add_dynamic_entity.sql)



  

## Add Dynamic Entity Def
  
*Template:* [add_dynamic_entity_def.sql](../templates/add_dynamic_entity_def.sql)



  

## Add Dynamic Entity String Field
  
*Template:* [add_dynamic_entity_string_field.sql](../templates/add_dynamic_entity_string_field.sql)  
*Test:* [test_add_dynamic_entity_string_field.sql](../test_templates/test_add_dynamic_entity_string_field.sql)



  

## Add Dynamic Entity Tagset Field
  
*Template:* [add_dynamic_entity_tagset_field.sql](../templates/add_dynamic_entity_tagset_field.sql)  
*Test:* [test_add_dynamic_entity_tagset_field.sql](../test_templates/test_add_dynamic_entity_tagset_field.sql)



  

## Add Dynamic Entity View
  
*Template:* [add_dynamic_entity_view.sql](../templates/add_dynamic_entity_view.sql)  
*Test:* [test_add_dynamic_entity_view.sql](../test_templates/test_add_dynamic_entity_view.sql)



  

## Add Dynamic Entity View Field
  
*Template:* [add_dynamic_entity_view_field.sql](../templates/add_dynamic_entity_view_field.sql)  
*Test:* [test_add_dynamic_entity_view_field.sql](../test_templates/test_add_dynamic_entity_view_field.sql)



  

## Add Entitlement
  
*Template:* [add_entitlement.sql](../templates/add_entitlement.sql)  
*Test:* [test_add_entitlement.sql](../test_templates/test_add_entitlement.sql)



  

## Add Entitlement To Agent
  
*Template:* [add_entitlement_to_agent.sql](../templates/add_entitlement_to_agent.sql)  
*Test:* [test_add_entitlement_to_agent.sql](../test_templates/test_add_entitlement_to_agent.sql)



  

## Add Entitlement To Dynamic Entity Field
  
*Template:* [add_entitlement_to_dynamic_entity_field.sql](../templates/add_entitlement_to_dynamic_entity_field.sql)  
*Test:* [test_add_entitlement_to_dynamic_entity_field.sql](../test_templates/test_add_entitlement_to_dynamic_entity_field.sql)



  

## Add Entitlement To Profile
  
*Template:* [add_entitlement_to_profile.sql](../templates/add_entitlement_to_profile.sql)  
*Test:* [test_add_entitlement_to_profile.sql](../test_templates/test_add_entitlement_to_profile.sql)



  

## Add Entitlement To Team
  
*Template:* [add_entitlement_to_team.sql](../templates/add_entitlement_to_team.sql)  
*Test:* [test_add_entitlement_to_team.sql](../test_templates/test_add_entitlement_to_team.sql)



  

## Add Entitlement To Verb
  
*Template:* [add_entitlement_to_verb.sql](../templates/add_entitlement_to_verb.sql)  
*Test:* [test_add_entitlement_to_verb.sql](../test_templates/test_add_entitlement_to_verb.sql)



  

## Add Entity Definition
  
*Template:* [add_entity_definition.sql](../templates/add_entity_definition.sql)  
*Test:* [test_add_entity_definition.sql](../test_templates/test_add_entity_definition.sql)



  

## Add Feedback Notification Type
  
*Template:* [add_feedback_notification_type.sql](../templates/add_feedback_notification_type.sql)  
*Test:* [test_add_feedback_notification_type.sql](../test_templates/test_add_feedback_notification_type.sql)



  

## Add Localised Field
  
*Template:* [add_localised_field.sql](../templates/add_localised_field.sql)



  

## Add Menu Item
  
*Template:* [add_menu_item.sql](../templates/add_menu_item.sql)  
*Test:* [test_add_menu_item.sql](../test_templates/test_add_menu_item.sql)



  

## Add Migration Domain
  
*Template:* [add_migration_domain.sql](../templates/add_migration_domain.sql)



  

## Add Perspective
  
*Template:* [add_perspective.sql](../templates/add_perspective.sql)  
*Test:* [test_add_perspective.sql](../test_templates/test_add_perspective.sql)



  

## Add Perspective To Profile
  
*Template:* [add_perspective_to_profile.sql](../templates/add_perspective_to_profile.sql)  
*Test:* [test_add_perspective_to_profile.sql](../test_templates/test_add_perspective_to_profile.sql)



  

## Add Process Descriptor
  
*Template:* [add_process_descriptor.sql](../templates/add_process_descriptor.sql)  
*Test:* [test_add_process_descriptor.sql](../test_templates/test_add_process_descriptor.sql)



  

## Add Profile
  
*Template:* [add_profile.sql](../templates/add_profile.sql)  
*Test:* [test_add_profile.sql](../test_templates/test_add_profile.sql)



  

## Add Profile To Agent
  
*Template:* [add_profile_to_agent.sql](../templates/add_profile_to_agent.sql)  
*Test:* [test_add_profile_to_agent.sql](../test_templates/test_add_profile_to_agent.sql)



  

## Add Reason Code
  
*Template:* [add_reason_code.sql](../templates/add_reason_code.sql)  
*Test:* [test_add_reason_code.sql](../test_templates/test_add_reason_code.sql)  
*Related Tasks:* [Remove Reason Code](#remove-reason-code)

Adds reason code or avilable status codes





*Template Design notes*
Currently is using relatives IDs  for ID column, which is fine for this scenario.
This template could be changed to allow entering the ID manually so it matches the code on a phone system.
Ordering is computing following OTB code: CoreChannels.Implementation.ReasonCode.Integration.Adapters.ReasonCodeAdapter.getOrderingNumber

  

## Add Report
  
*Template:* [add_report.sql](../templates/add_report.sql)  
*Test:* [test_add_report.sql](../test_templates/test_add_report.sql)



  

## Add Static Menu
  
*Template:* [add_static_menu.sql](../templates/add_static_menu.sql)  
*Test:* [test_add_static_menu.sql](../test_templates/test_add_static_menu.sql)



  

## Add Tab To Ad Right Panel
  
*Template:* [add_tab_to_ad_right_panel.sql](../templates/add_tab_to_ad_right_panel.sql)



  

## Add Tag
  
*Template:* [add_tag.sql](../templates/add_tag.sql)  
*Test:* [test_add_tag.sql](../test_templates/test_add_tag.sql)



  

## Add Team
  
*Template:* [add_team.sql](../templates/add_team.sql)  
*Test:* [test_add_team.sql](../test_templates/test_add_team.sql)



  

## Add Team Position
  
*Template:* [add_team_position.sql](../templates/add_team_position.sql)  
*Test:* [test_add_team_position.sql](../test_templates/test_add_team_position.sql)



  

## Add Team Role
  
*Template:* [add_team_role.sql](../templates/add_team_role.sql)  
*Test:* [test_add_team_role.sql](../test_templates/test_add_team_role.sql)



  

## Add Team Role Type
  
*Template:* [add_team_role_type.sql](../templates/add_team_role_type.sql)  
*Test:* [test_add_team_role_type.sql](../test_templates/test_add_team_role_type.sql)



  

## Add Url With Smartmatch Purpose
  
*Template:* [add_url_with_smartmatch_purpose.sql](../templates/add_url_with_smartmatch_purpose.sql)  
*Test:* [test_add_url_with_smartmatch_purpose.sql](../test_templates/test_add_url_with_smartmatch_purpose.sql)  
*Related Tasks:* [Add Web Integration Host](#add-web-integration-host)

Adds a URL and makes it available to be used in rules editor




A use case is setting up an inbound rule, within the Rules Editor, which calls a URL when something happens.
For example creating a customer when the customer is not identified. We could do that by making a request to create customer URL REST API. This URL needs to be previously configured and saved in the database. This is what this template does.

Currently only saves to the URL table, it does not save to FWI_URL_HEADER or FWI_URL_PARAM table. Once we encounter a use case that needs to save to those tables this template could be modified to save to those tables as well or, a additional templates could be created.

Note also that "EXPORT_LOCALE" is set "N", this is equivalent to make this URL non migratable, we do this because we are scripting and any modification to the rule is expected to be done through script, not using migration.

A URL is added to an existing host, which is an entry  on the `FWI_HOST` table. Use the template `add_web_integration_host.groovy` to create a host.

  
  
**Images**  
  
![1](../templates/add_url_with_smartmatch_purpose1.PNG)  
**<center>Image 1</center>**  
  
![2](../templates/add_url_with_smartmatch_purpose2.PNG)  
**<center>Image 2</center>**  

## Add Url With Smartmatch Purpose Rollback
  
*Template:* [add_url_with_smartmatch_purpose_rollback.sql](../templates/add_url_with_smartmatch_purpose_rollback.sql)  
*Test:* [test_add_url_with_smartmatch_purpose_rollback.sql](../test_templates/test_add_url_with_smartmatch_purpose_rollback.sql)



  

## Add Verb To Entity
  
*Template:* [add_verb_to_entity.sql](../templates/add_verb_to_entity.sql)  
*Test:* [test_add_verb_to_entity.sql](../test_templates/test_add_verb_to_entity.sql)



  

## Add Verb With Existing Pdr
  
*Template:* [add_verb_with_existing_pdr.sql](../templates/add_verb_with_existing_pdr.sql)



  

## Add View Contact Tab
  
*Template:* [add_view_contact_tab.sql](../templates/add_view_contact_tab.sql)  
*Test:* [test_add_view_contact_tab.sql](../test_templates/test_add_view_contact_tab.sql)



  

## Add Web Integration Host
  
*Template:* [add_web_integration_host.groovy](../templates/add_web_integration_host.groovy)  
*Test:* [test_add_web_integration_host.groovy](../test_templates/test_add_web_integration_host.groovy)



  

## Change Max Count Work Area
  
*Template:* [change_max_count_work_area.sql](../templates/change_max_count_work_area.sql)  
*Test:* [test_change_max_count_work_area.sql](../test_templates/test_change_max_count_work_area.sql)



  

## Config New Content Type
  
*Template:* [config_new_content_type.sql](../templates/config_new_content_type.sql)



  

## Extend Customer
  
*Template:* [extend_customer.sql](../templates/extend_customer.sql)  
*Test:* [test_extend_customer.sql](../test_templates/test_extend_customer.sql)



  

## Extend Entity
  
*Template:* [extend_entity.sql](../templates/extend_entity.sql)  
*Test:* [test_extend_entity.sql](../test_templates/test_extend_entity.sql)



  

## Extend Verb
  
*Template:* [extend_verb.sql](../templates/extend_verb.sql)  
*Test:* [test_extend_verb.sql](../test_templates/test_extend_verb.sql)



  

## Extend Verb With Config
  
*Template:* [extend_verb_with_config.sql](../templates/extend_verb_with_config.sql)  
*Test:* [test_extend_verb_with_config.sql](../test_templates/test_extend_verb_with_config.sql)



  

## Register Channel State Manager Listener
  
*Template:* [register_channel_state_manager_listener.sql](../templates/register_channel_state_manager_listener.sql)  
*Test:* [test_register_channel_state_manager_listener.sql](../test_templates/test_register_channel_state_manager_listener.sql)



  

## Remove Activity From Perspective
  
*Template:* [remove_activity_from_perspective.sql](../templates/remove_activity_from_perspective.sql)



  

## Remove Agent For Dev
  
*Template:* [remove_agent_for_dev.sql](../templates/remove_agent_for_dev.sql)  
*Test:* [test_remove_agent_for_dev.sql](../test_templates/test_remove_agent_for_dev.sql)



  

## Remove Background Verb From Profile
  
*Template:* [remove_background_verb_from_profile.sql](../templates/remove_background_verb_from_profile.sql)



  

## Remove Base Entity
  
*Template:* [remove_base_entity.sql](../templates/remove_base_entity.sql)  
*Test:* [test_remove_base_entity.sql](../test_templates/test_remove_base_entity.sql)



  

## Remove Entitlement From Agent
  
*Template:* [remove_entitlement_from_agent.sql](../templates/remove_entitlement_from_agent.sql)  
*Test:* [test_remove_entitlement_from_agent.sql](../test_templates/test_remove_entitlement_from_agent.sql)



  

## Remove Entitlement From Profile
  
*Template:* [remove_entitlement_from_profile.sql](../templates/remove_entitlement_from_profile.sql)  
*Test:* [test_remove_entitlement_from_profile.sql](../test_templates/test_remove_entitlement_from_profile.sql)



  

## Remove Entitlement From Team
  
*Template:* [remove_entitlement_from_team.sql](../templates/remove_entitlement_from_team.sql)  
*Test:* [test_remove_entitlement_from_team.sql](../test_templates/test_remove_entitlement_from_team.sql)



  

## Remove Entitlement From Verb
  
*Template:* [remove_entitlement_from_verb.sql](../templates/remove_entitlement_from_verb.sql)  
*Test:* [test_remove_entitlement_from_verb.sql](../test_templates/test_remove_entitlement_from_verb.sql)



  

## Remove Entity Definition
  
*Template:* [remove_entity_definition.sql](../templates/remove_entity_definition.sql)  
*Test:* [test_remove_entity_definition.sql](../test_templates/test_remove_entity_definition.sql)



  

## Remove Menu Item
  
*Template:* [remove_menu_item.sql](../templates/remove_menu_item.sql)  
*Test:* [test_remove_menu_item.sql](../test_templates/test_remove_menu_item.sql)



  

## Remove Perspective From Profile
  
*Template:* [remove_perspective_from_profile.sql](../templates/remove_perspective_from_profile.sql)  
*Test:* [test_remove_perspective_from_profile.sql](../test_templates/test_remove_perspective_from_profile.sql)



  

## Remove Process Desc Ref
  
*Template:* [remove_process_desc_ref.sql](../templates/remove_process_desc_ref.sql)  
*Test:* [test_remove_process_desc_ref.sql](../test_templates/test_remove_process_desc_ref.sql)



  

## Remove Profile From Agent
  
*Template:* [remove_profile_from_agent.sql](../templates/remove_profile_from_agent.sql)



  

## Remove Profile From All Agents
  
*Template:* [remove_profile_from_all_agents.sql](../templates/remove_profile_from_all_agents.sql)  
*Test:* [test_remove_profile_from_all_agents.sql](../test_templates/test_remove_profile_from_all_agents.sql)  
*Related Tasks:* [Remove Profile From Agent](#remove-profile-from-agent)

Removes a profile from all the users that is currently assigned to



It requires the profile keyname and it suggests a list with all the profile keynames

  

## Remove Reason Code
  
*Template:* [remove_reason_code.sql](../templates/remove_reason_code.sql)  
*Test:* [test_remove_reason_code.sql](../test_templates/test_remove_reason_code.sql)  
*Related Tasks:* [Add Reason Code](#add-reason-code)

Removes reason code or avilable status codes



It takes a range of reason codes IDs and it removes all the reason codes within that range including both ends.

  

## Remove Tab From Ad Right Panel
  
*Template:* [remove_tab_from_ad_right_panel.sql](../templates/remove_tab_from_ad_right_panel.sql)  
*Test:* [test_remove_tab_from_ad_right_panel.sql](../test_templates/test_remove_tab_from_ad_right_panel.sql)



  

## Remove Tagset And All Tags
  
*Template:* [remove_tagset_and_all_tags.sql](../templates/remove_tagset_and_all_tags.sql)



  

## Remove Team
  
*Template:* [remove_team.sql](../templates/remove_team.sql)  
*Test:* [test_remove_team.sql](../test_templates/test_remove_team.sql)



  

## Remove Team Role
  
*Template:* [remove_team_role.sql](../templates/remove_team_role.sql)  
*Test:* [test_remove_team_role.sql](../test_templates/test_remove_team_role.sql)



  

## Remove Team Role Type
  
*Template:* [remove_team_role_type.sql](../templates/remove_team_role_type.sql)  
*Test:* [test_remove_team_role_type.sql](../test_templates/test_remove_team_role_type.sql)



  

## Remove Verb From Entity
  
*Template:* [remove_verb_from_entity.sql](../templates/remove_verb_from_entity.sql)  
*Test:* [test_remove_verb_from_entity.sql](../test_templates/test_remove_verb_from_entity.sql)



  

## Remove View Contact Tab
  
*Template:* [remove_view_contact_tab.sql](../templates/remove_view_contact_tab.sql)  
*Test:* [test_remove_view_contact_tab.sql](../test_templates/test_remove_view_contact_tab.sql)



  

## Reorder Dynamic View Field
  
*Template:* [reorder_dynamic_view_field.sql](../templates/reorder_dynamic_view_field.sql)  
*Test:* [test_reorder_dynamic_view_field.sql](../test_templates/test_reorder_dynamic_view_field.sql)  
*Related Tasks:* [Add Dynamic Entity View Field](#add-dynamic-entity-view-field)

Reorder dynamic view field by moving it up or down to a given position




If we take as example the following fields:

|            KEYNAME            | VIEW_FIELD_SEQUENCE |
|-------------------------------|---------------------|
|   KnowledgeSegmentCreateBody  |          1          |
|  KnowledgeSegmentCreateKBase  |          2          |
| KnowledgeSegmentCreateProduct |          3          |
|  KnowledgeSegmentCreateTopic  |          4          |
|  KnowledgeSegmentCreateRegion |          5          |


**Moving Up**

Selecting 'KnowledgeSegmentCreateTopic' and entering sequence_no '2' will change to:

|            KEYNAME            | VIEW_FIELD_SEQUENCE |
|-------------------------------|---------------------|
|   KnowledgeSegmentCreateBody  |          1          |
|  KnowledgeSegmentCreateTopic  |          2          |
|  KnowledgeSegmentCreateKBase  |          3          |
| KnowledgeSegmentCreateProduct |          4          |
|  KnowledgeSegmentCreateRegion |          5          |


**Moving Down**

Now we can move 'KnowledgeSegmentCreateTopic' back to his original place by selecting 'KnowledgeSegmentCreateTopic' and entering sequence_no '4'.

  
  
**Images**  
  
![1](../templates/reorder_dynamic_view_field1.PNG)  
**<center>Image 1</center>**  
  
![2](../templates/reorder_dynamic_view_field2.PNG)  
**<center>Image 2</center>**  
  
![3](../templates/reorder_dynamic_view_field3.PNG)  
**<center>Image 3</center>**  

## Set Entity Default Instance Verb
  
*Template:* [set_entity_default_instance_verb.sql](../templates/set_entity_default_instance_verb.sql)  
*Test:* [test_set_entity_default_instance_verb.sql](../test_templates/test_set_entity_default_instance_verb.sql)  
*Related Tasks:* [Update Verb User Visible Flag](#update-verb-user-visible-flag), [Add Activity To Perspective](#add-activity-to-perspective)  
*Related Views:* [View Entity Displayed Verbs](#view-entity-displayed-verbs), [View Entity Verbs](#view-entity-verbs)

Determines what verb runs when user clicks on a entity displayed on context



This template prompts to select an entity keyname and then it prompts the instance verbs for that entity. Once the user has selected a verb, the generated SQL runs an update that sets the default instance flag on all the entity verbs to 'N' and then updates the specified verb to 'Y'.

### What is an Entity Default Instance Verb?
On agent desktop, when entity is added into context it displays on the left hand side activities panel showing as title the entities `toString()` result and underneath its "user visible" intance verbs.
User can run each verb by clicking on the verb title. User can also click on the entities title and it will run the default instance verb.  

## Unregister Channel State Manager Listener
  
*Template:* [unregister_channel_state_manager_listener.sql](../templates/unregister_channel_state_manager_listener.sql)  
*Test:* [test_unregister_channel_state_manager_listener.sql](../test_templates/test_unregister_channel_state_manager_listener.sql)



  

## Update Agent Password
  
*Template:* [update_agent_password.sql](../templates/update_agent_password.sql)  
*Test:* [test_update_agent_password.sql](../test_templates/test_update_agent_password.sql)



  

## Update Ccadmin Version
  
*Template:* [update_ccadmin_version.sql](../templates/update_ccadmin_version.sql)  
*Test:* [test_update_ccadmin_version.sql](../test_templates/test_update_ccadmin_version.sql)



  

## Update Localised Field
  
*Template:* [update_localised_field.sql](../templates/update_localised_field.sql)  
*Test:* [test_update_localised_field.sql](../test_templates/test_update_localised_field.sql)



  

## Update Profile Perspective Seq No
  
*Template:* [update_profile_perspective_seq_no.sql](../templates/update_profile_perspective_seq_no.sql)  
*Test:* [test_update_profile_perspective_seq_no.sql](../test_templates/test_update_profile_perspective_seq_no.sql)



  

## Update Url With Smartmatch Purpose
  
*Template:* [update_url_with_smartmatch_purpose.sql](../templates/update_url_with_smartmatch_purpose.sql)  
*Test:* [test_update_url_with_smartmatch_purpose.sql](../test_templates/test_update_url_with_smartmatch_purpose.sql)



  

## Update Verb Path
  
*Template:* [update_verb_path.sql](../templates/update_verb_path.sql)  
*Test:* [test_update_verb_path.sql](../test_templates/test_update_verb_path.sql)



  

## Update Verb Process Descriptor Reference
  
*Template:* [update_verb_process_descriptor_reference.sql](../templates/update_verb_process_descriptor_reference.sql)  
*Test:* [test_update_verb_process_descriptor_reference.sql](../test_templates/test_update_verb_process_descriptor_reference.sql)



  

## Update Verb User Visible Flag
  
*Template:* [update_verb_user_visible_flag.sql](../templates/update_verb_user_visible_flag.sql)  
*Test:* [test_update_verb_user_visible_flag.sql](../test_templates/test_update_verb_user_visible_flag.sql)



  

# hidden_templates
  
There are currently 12 templates in this section
## Add Dynamic Entity Field Without Specific Props
  
*Template:* [add_dynamic_entity_field_without_specific_props.sql](../templates/hidden_templates/add_dynamic_entity_field_without_specific_props.sql)



  

## Add Dynamic String Field Property
  
*Template:* [add_dynamic_string_field_property.sql](../templates/hidden_templates/add_dynamic_string_field_property.sql)



  

## Add Dynamic Tagset Field Property
  
*Template:* [add_dynamic_tagset_field_property.sql](../templates/hidden_templates/add_dynamic_tagset_field_property.sql)



  

## Add Entity Entitlement
  
*Template:* [add_entity_entitlement.sql](../templates/hidden_templates/add_entity_entitlement.sql)



  

## Add Process Descriptor Ref
  
*Template:* [add_process_descriptor_ref.sql](../templates/hidden_templates/add_process_descriptor_ref.sql)



  

## Base Add Entity Def
  
*Template:* [base_add_entity_def.sql](../templates/hidden_templates/base_add_entity_def.sql)



  

## Generic Set Update Values
  
*Template:* [generic_set_update_values.sql](../templates/hidden_templates/generic_set_update_values.sql)



  

## Insert Context Verb Entry
  
*Template:* [insert_context_verb_entry.sql](../templates/hidden_templates/insert_context_verb_entry.sql)



  

## Insert Dynamic Verb List
  
*Template:* [insert_dynamic_verb_list.sql](../templates/hidden_templates/insert_dynamic_verb_list.sql)



  

## Insert Dynamic Verb Parameter
  
*Template:* [insert_dynamic_verb_parameter.sql](../templates/hidden_templates/insert_dynamic_verb_parameter.sql)



  

## Remove Dynamic Verb List
  
*Template:* [remove_dynamic_verb_list.sql](../templates/hidden_templates/remove_dynamic_verb_list.sql)



  

## Remove Idmap
  
*Template:* [remove_idmap.sql](../templates/hidden_templates/remove_idmap.sql)



  

# pepi-one
  
There are currently 1 templates in this section
## Test
  
*Template:* [test.sql](../templates/pepi-one/test.sql)



  

# pepi_one
  
There are currently 1 templates in this section
## Test
  
*Template:* [test.sql](../templates/pepi_one/test.sql)



  

# tenant_properties_service
  
There are currently 5 templates in this section
## Add Agent Synchronizer Default Mapping
  
*Template:* [add_agent_synchronizer_default_mapping.sql](../templates/tenant_properties_service/add_agent_synchronizer_default_mapping.sql)  
*Test:* [test_add_agent_synchronizer_default_mapping.sql](../test_templates/tenant_properties_service/test_add_agent_synchronizer_default_mapping.sql)



  

## Add Agent Synchronizer Mapping
  
*Template:* [add_agent_synchronizer_mapping.sql](../templates/tenant_properties_service/add_agent_synchronizer_mapping.sql)  
*Test:* [test_add_agent_synchronizer_mapping.sql](../test_templates/tenant_properties_service/test_add_agent_synchronizer_mapping.sql)



  

## Add Tenant Property
  
*Template:* [add_tenant_property.sql](../templates/tenant_properties_service/add_tenant_property.sql)  
*Test:* [test_add_tenant_property.sql](../test_templates/tenant_properties_service/test_add_tenant_property.sql)



  

## Remove Tenant Property
  
*Template:* [remove_tenant_property.sql](../templates/tenant_properties_service/remove_tenant_property.sql)  
*Test:* [test_remove_tenant_property.sql](../test_templates/tenant_properties_service/test_remove_tenant_property.sql)



  

## Update Tenant Property
  
*Template:* [update_tenant_property.sql](../templates/tenant_properties_service/update_tenant_property.sql)  
*Test:* [test_update_tenant_property.sql](../test_templates/tenant_properties_service/test_update_tenant_property.sql)



  

# views
  
There are currently 21 templates in this section
## View Tps Property
  
*Template:* [view_tps_property.sql](../templates/tenant_properties_service/views/view_tps_property.sql)



  

## View Ad Right Panel Tabs Verbs
  
*Template:* [view_ad_right_panel_tabs_verbs.sql](../templates/views/view_ad_right_panel_tabs_verbs.sql)



  

## View Agent
  
*Template:* [view_agent.sql](../templates/views/view_agent.sql)



  

## View Agent Profile Background Vebs
  
*Template:* [view_agent_profile_background_vebs.sql](../templates/views/view_agent_profile_background_vebs.sql)



  

## View Channel State Manager Listeners
  
*Template:* [view_channel_state_manager_listeners.sql](../templates/views/view_channel_state_manager_listeners.sql)



  

## View Entitlements By System Name
  
*Template:* [view_entitlements_by_system_name.sql](../templates/views/view_entitlements_by_system_name.sql)



  

## View Entity Definition
  
*Template:* [view_entity_definition.sql](../templates/views/view_entity_definition.sql)



  

## View Entity Displayed Verbs
  
*Template:* [view_entity_displayed_verbs.sql](../templates/views/view_entity_displayed_verbs.sql)



  

## View Entity Verbs
  
*Template:* [view_entity_verbs.sql](../templates/views/view_entity_verbs.sql)  
*Test:* [test_view_entity_verbs.sql](../test_templates/views/test_view_entity_verbs.sql)



  

## View Entity Verbs Keynames
  
*Template:* [view_entity_verbs_keynames.sql](../templates/views/view_entity_verbs_keynames.sql)



  

## View Entitydef By Keyname
  
*Template:* [view_entitydef_by_keyname.sql](../templates/views/view_entitydef_by_keyname.sql)



  

## View Keynames
  
*Template:* [view_keynames.sql](../templates/views/view_keynames.sql)



  

## View Keynames By Id
  
*Template:* [view_keynames_by_id.sql](../templates/views/view_keynames_by_id.sql)



  

## View Process Descriptor Ref By Repo Path
  
*Template:* [view_process_descriptor_ref_by_repo_path.sql](../templates/views/view_process_descriptor_ref_by_repo_path.sql)



  

## View Process Descriptor Reference From Repo Path
  
*Template:* [view_process_descriptor_reference_from_repo_path.sql](../templates/views/view_process_descriptor_reference_from_repo_path.sql)



  

## View Profile Entitlements
  
*Template:* [view_profile_entitlements.sql](../templates/views/view_profile_entitlements.sql)



  

## View Profile Verbs
  
*Template:* [view_profile_verbs.sql](../templates/views/view_profile_verbs.sql)



  

## View User Profiles
  
*Template:* [view_user_profiles.sql](../templates/views/view_user_profiles.sql)  
*Test:* [test_view_user_profiles.sql](../test_templates/views/test_view_user_profiles.sql)



  

## View Verb By Keyname
  
*Template:* [view_verb_by_keyname.sql](../templates/views/view_verb_by_keyname.sql)



  

## View Verb Entitlements
  
*Template:* [view_verb_entitlements.sql](../templates/views/view_verb_entitlements.sql)



  

## View Verbs From Repo Path
  
*Template:* [view_verbs_from_repo_path.sql](../templates/views/view_verbs_from_repo_path.sql)



  

# tutorials
  
There are currently 7 templates in this section
## Filters
  
*Template:* [filters.txt](../templates/tutorials/filters.txt)



  

## Globals And String Functions Tutorial
  
*Template:* [globals_and_string_functions_tutorial.txt](../templates/tutorials/globals_and_string_functions_tutorial.txt)



  

## How To Add Content Type
  
*Template:* [how_to_add_content_type.txt](../templates/tutorials/how_to_add_content_type.txt)



  

## Include
  
*Template:* [include.txt](../templates/tutorials/include.txt)



  

## Keynames
  
*Template:* [keynames.txt](../templates/tutorials/keynames.txt)



  

## Querying Db
  
*Template:* [querying_db.txt](../templates/tutorials/querying_db.txt)



  

## Variable And Prompts
  
*Template:* [variable_and_prompts.txt](../templates/tutorials/variable_and_prompts.txt)



  

# oracle
  
There are currently 1 templates in this section
## View Table Name From Foreign Key Name
  
*Template:* [view_table_name_from_foreign_key_name.sql](../templates/views/oracle/view_table_name_from_foreign_key_name.sql)



  
