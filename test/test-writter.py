import unittest
from typing import Union
from app import writer


class FakeWriteable:
    def __init__(self):
        self.written_content = None

    def write(self, content: Union[str, bytes]):
        self.written_content = content


def fake_text_formatter(content: str):
    return "formatted_" + content


def fake_text_colorizer(content: str):
    return "colorized_" + content


def fake_bytes_formatter(content: bytes):
    return b"formatted_" + content


def fake_bytes_colorizer(content: bytes):
    return b"colorized_" + content


class TestWriter(unittest.TestCase):
    """
    Unit tests for the writer module.
    This test suite includes tests for writing text and bytes with various combinations
    of formatters and colorizers.
    Classes:
        TestWriter: Contains unit tests for the writer module.
    Methods:
        setUp: Initializes a FakeWriteable instance for use in tests.
        test_write_text_noformatter_nocolorizer: Tests writing text without a formatter or colorizer.
        test_write_text_withformatter_nocolorizer: Tests writing text with a formatter but no colorizer.
        test_write_text_noformatter_withcolorizer: Tests writing text with a colorizer but no formatter.
        test_write_text_withformatter_withcolorizer: Tests writing text with both a formatter and a colorizer.
        test_write_bytes_noformatter_nocolorizer: Tests writing bytes without a formatter or colorizer.
        test_write_bytes_withformatter_nocolorizer: Tests writing bytes with a formatter but no colorizer.
        test_write_bytes_noformatter_withcolorizer: Tests writing bytes with a colorizer but no formatter.
        test_write_bytes_withformatter_withcolorizer: Tests writing bytes with both a formatter and a colorizer.
    """

    def setUp(self) -> None:
        self.fake_writeable = FakeWriteable()

    def test_write_text_noformatter_nocolorizer(self):
        content = "const1"
        writer.write(content, self.fake_writeable, formatter=None, colorizer=None)
        self.assertEqual(self.fake_writeable.written_content.strip().strip(), content)

    def test_write_text_withformatter_nocolorizer(self):
        content = "const1"
        writer.write(
            content, self.fake_writeable, formatter=fake_text_formatter, colorizer=None
        )
        self.assertEqual(
            self.fake_writeable.written_content.strip(), fake_text_formatter(content)
        )

    def test_write_text_noformatter_withcolorizer(self):
        content = "const1"
        writer.write(
            content, self.fake_writeable, formatter=None, colorizer=fake_text_colorizer
        )
        self.assertEqual(
            self.fake_writeable.written_content.strip(), fake_text_colorizer(content)
        )

    def test_write_text_withformatter_withcolorizer(self):
        content = "const1"
        writer.write(
            content,
            self.fake_writeable,
            formatter=fake_text_formatter,
            colorizer=fake_text_colorizer,
        )
        self.assertEqual(
            self.fake_writeable.written_content.strip(),
            fake_text_colorizer(fake_text_formatter(content)),
        )

    def test_write_bytes_noformatter_nocolorizer(self):
        content = b"const1"
        writer.write(content, self.fake_writeable, formatter=None, colorizer=None)
        self.assertEqual(self.fake_writeable.written_content.strip(), content)

    def test_write_bytes_withformatter_nocolorizer(self):
        content = b"const1"
        writer.write(
            content, self.fake_writeable, formatter=fake_bytes_formatter, colorizer=None
        )
        self.assertEqual(self.fake_writeable.written_content.strip(), content)

    def test_write_bytes_noformatter_withcolorizer(self):
        content = b"const1"
        writer.write(
            content, self.fake_writeable, formatter=None, colorizer=fake_bytes_colorizer
        )
        self.assertEqual(self.fake_writeable.written_content.strip(), content)

    def test_write_bytes_withformatter_withcolorizer(self):
        content = b"const1"
        writer.write(
            content,
            self.fake_writeable,
            formatter=fake_bytes_formatter,
            colorizer=fake_bytes_colorizer,
        )
        self.assertEqual(self.fake_writeable.written_content.strip(), content)
