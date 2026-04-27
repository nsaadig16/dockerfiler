import dockerfiler.projects.uv_base.params as p
from dataclasses import dataclass
from dockerfiler.projects.utils import ask
from typing import Optional

@dataclass
class Params(p.Params):
    port : Optional[str] = ask(question="Port?", default="8501",type="text")

@dataclass
class IgnoreParams(p.IgnoreParams):
    pass
