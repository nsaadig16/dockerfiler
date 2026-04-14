from dataclasses import field
from typing import Optional, List

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]
QUARTO_VERSIONS = ["1.7.0","1.8.0", "1.9.0","1.9.32","1.10.0"]

def ask(
    question: str,
    default: str = "",
    type: str = "text",
    choices: Optional[List] = None,
    list_parse: bool = False,
):
    metadata={
        "question": question,
        "default": default,
        "type": type,
        "list_parse": list_parse,
    }
    if choices is not None:
        metadata["choices"] = choices
    return field(
        default=None,
        metadata=metadata,
    )
