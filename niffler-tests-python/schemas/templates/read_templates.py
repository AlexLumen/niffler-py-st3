import os

import xmlschema
from jinja2 import Environment, select_autoescape, FileSystemLoader
from xmlschema import XMLSchema11

from schemas.templates.xsd.get_file import get_full_path_to_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR)
env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape(['html', 'xml'])
)


def country_iso_code_xml(country_iso_code: str) -> str:
    template = env.get_template('/xml/country_iso_code.xml')
    return template.render({'country_iso_code': country_iso_code})


def country_name_xml(country_name: str) -> str:
    template = env.get_template('/xml/country_name.xml')
    return template.render({'country_name': country_name})


# country_iso_code_xml = result
# pass

def xsd_response(operation: str) -> XMLSchema11:
    envelope_xsd = env.get_template('/xsd/envelope.xsd')
    country_iso_code_xsd_response = envelope_xsd.render(
        {'operation_xsd': f'{operation}.xsd', 'operation': operation})
    with open(get_full_path_to_file('temp.xsd'), 'w') as f:
        f.write(country_iso_code_xsd_response)

    return xmlschema.XMLSchema11(get_full_path_to_file('temp.xsd'))
