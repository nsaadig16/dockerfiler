from dataclasses import dataclass, field
from .utils import ask, PYTHON_VERSIONS
from typing import Optional


@dataclass
class UVBaseParams:
    version: str = ask(
        question="Python version?",
        default="3.12",
        type="select",
        choices=PYTHON_VERSIONS,
    )
    port: Optional[int] = ask(question="Port?", default="", type="text")
    entrypoint: Optional[str] = ask(
        question="Entrypoint?", default="main.py", type="text", list_parse=True
    )


@dataclass
class DjangoUVParams(UVBaseParams):
    port: int = ask(question="Port?", default="8080", type="text")
    host: str = ask(question="Host?", default="0.0.0.0", type="text")
    entrypoint: None = field(default=None)


@dataclass
class FastapiUVParams(UVBaseParams):
    port: int = ask(question="Port?", default="8080", type="text")
    host: str = ask(question="Host?", default="0.0.0.0", type="text")
    asgi_path: str = ask(
        question="Enter the ASGI path (module:variable)",
        default="main:app",
        type="text",
    )
    entrypoint: None = field(default=None)
