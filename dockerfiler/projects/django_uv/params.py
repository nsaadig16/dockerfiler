from dataclasses import dataclass, field
from dockerfiler.projects.uv_base.params import UVBaseParams
from dockerfiler.projects.utils import ask

@dataclass
class DjangoUVParams(UVBaseParams):
    port: int = ask(question="Port?", default="8080", type="text")
    host: str = ask(question="Host?", default="0.0.0.0", type="text")
    entrypoint: None = field(default=None)
