from typing import Union, Protocol


class Writeable(Protocol):
    def write(self, content: Union[str, bytes]): ...


def write(content: Union[str, bytes], to: Writeable, formatter=None, colorizer=None):
    """
    Writes content to a writable object, optionally formatting and colorizing it.

    Args:
        content (Union[str, bytes]): The content to write. Can be a string or bytes.
        to (Writeable): The writable object where the content will be written.
        formatter (callable, optional): A function to format the content if it is a string. Defaults to None.
        colorizer (callable, optional): A function to colorize the content if it is a string. Defaults to None.

    Returns:
        None
    """
    if isinstance(content, str):
        content = formatter(content) if formatter else content
        content = colorizer(content) if colorizer else content
        content = "\n" + content + "\n"
    to.write(content)
