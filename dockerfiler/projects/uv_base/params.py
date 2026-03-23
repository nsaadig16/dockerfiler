from dataclasses import dataclass
from dockerfiler.projects.utils import ask, PYTHON_VERSIONS
from typing import Optional

@dataclass
class UVBaseParams:
    version: str = ask(
        question="Python version?",
        default="3.12",
        type="select",
        choices=PYTHON_VERSIONS,
    )
    port: Optional[int] = ask(question="Port?", default="8000", type="text")
    entrypoint: Optional[str] = ask(
        question="Entrypoint?", default="main.py", type="text", list_parse=True
    )
