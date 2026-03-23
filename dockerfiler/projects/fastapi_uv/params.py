from dataclasses import dataclass, field
from dockerfiler.projects.uv_base.params import UVBaseParams
from dockerfiler.projects.utils import ask

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
