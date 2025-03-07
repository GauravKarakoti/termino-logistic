import json
from lxml import etree, html


# Formats metadata from a JSON string into a human-readable string with each key-value pair on a new line
def format_metadata(text: str) -> str:
    json_obj: dict = json.loads(text)
    lines = [
        f"{key}: {value}" for key, value in sorted(json_obj.items(), key=_by_key_lower)
    ]
    formatted = "\n".join(lines)
    return formatted


# Formats a JSON string with specified indentation
def format_json_string(text: str, indent=4) -> str:
    json_obj: dict = json.loads(text)
    formatted = json.dumps(json_obj, indent=indent)
    return formatted


# Formats an XML string with specified indentation
def format_xml_string(text: str, indent=2) -> str:
    xml_obj = etree.fromstring(text)
    etree.indent(xml_obj, space=" " * indent)
    formatted = etree.tostring(xml_obj, encoding="unicode")
    return formatted


# Formats an HTML string with specified indentation
def format_html_string(text: str, indent=2) -> str:
    html_obj = html.fromstring(text)
    etree.indent(html_obj, space=" " * indent)
    formatted = html.tostring(html_obj, encoding="unicode")
    return formatted


# Returns the input text without any formatting
def no_format(text: str):
    return text


# Helper function to sort dictionary items by key in a case-insensitive manner
def _by_key_lower(dict_item: tuple):
    key, val = dict_item
    return key.lower()
