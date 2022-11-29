# em_templates

It contains the configuration and the templates needed within a EM project to run em_automation

# Changing Locales

Different project could have different locales which might make some tests failed. Run a replace command to fix those. For example if we are using "en-GB" instead of "en-US" run:

grep -rl en-US . | xargs sed -i 's/en-US/en-GB/g'

Then you can run the tests

# Pre Loaded Data

Some test scripts need some data to be present in order to work:

Please execute `sqltask run-sql --template <<template-name>>` where template name and arguments are the following:

- test_add_team_position: add_team.sql {"team":"ProductSupport","Home":NULL}
