from pathlib import Path

from sqltask_lib.sqltasklib import Template

template1_text = """{#
short_description="this is a short desc" 
long_description="this is a long desc" 
#}
"""
path = Path("test/test_library/templates/template1.sql")
path.write_text(template1_text)
template = Template(Path("./test/test_libary"), "templates/template1.sql")
template.text = template1_text
print(template.short_description())
