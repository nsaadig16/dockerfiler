from dataclasses import field
from typing import Optional, List

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]


def ask(
    question: str,
    default: str = "",
    type: str = "text",
    choices: Optional[List] = None,
    list_parse: bool = False,
):
    return field(
        default=None,
        metadata={
            "question": question,
            "default": default,
            "type": type,
            "choices": choices,
            "list_parse": list_parse,
        },
    )
