{% set property_names = ["theme.default.logo","theme.default.em-enterprise-desktop.application-title","text.editor.fonts","km.content.feedback.hide-notify-me"] %}
{% set help_message = "Suggested property names are only a few examples. There will be property names that are valid and are not included in the suggested list." %}
{% set __property_name = property_name | suggest(property_names) %}
{% set __short_text = short_text %}
UPDATE TENANT_PROPERTY
SET (SHORT_TEXT) = ('{{__short_text}}')
where NAME ='{{__property_name}}';

