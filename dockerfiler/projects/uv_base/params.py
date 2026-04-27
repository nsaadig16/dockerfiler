#uv_base/params.py
import dockerfiler.projects.base._params as p
from dataclasses import dataclass
from dockerfiler.projects.utils import ask, PYTHON_VERSIONS
from typing import Optional

@dataclass
class Params(p.Params):
    version: Optional[str] = ask(
        question="Python version?",
        default="3.12",
        type="select",
        choices=PYTHON_VERSIONS,
    )
    port: Optional[str] = ask(question="Port?", default="8000", type="text")
    entrypoint: Optional[str] = ask(
        question="Entrypoint?", default="main.py", type="text", list_parse=True
    )

@dataclass
class IgnoreParams(p.IgnoreParams):
    pass