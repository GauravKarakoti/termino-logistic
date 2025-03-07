from pygments import highlight
from pygments.lexers.data import JsonLexer, YamlLexer
from pygments.lexers.html import HtmlLexer, XmlLexer
from pygments.formatters.terminal256 import TerminalTrueColorFormatter
from pygments.formatters.terminal import TerminalFormatter


# Function to colorize YAML metadata strings
def colorize_metadata_string(text) -> str:
    colorized = highlight(text, YamlLexer(), TerminalTrueColorFormatter())
    return colorized


# Function to colorize JSON strings
def colorize_json_string(text) -> str:
    colorized = highlight(text, JsonLexer(), TerminalFormatter())
    return colorized


# Function to colorize XML strings
def colorize_xml_string(text) -> str:
    colorized = highlight(text, XmlLexer(), TerminalFormatter())
    return colorized


# Function to colorize HTML strings
def colorize_html_string(text) -> str:
    colorized = highlight(text, HtmlLexer(), TerminalFormatter())
    return colorized


# Function to return the text without any colorization
def no_colorizer(text) -> str:
    return text
