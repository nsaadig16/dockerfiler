import dockerfiler.projects.uv_base.params as p
from dataclasses import dataclass, field
from dockerfiler.projects.utils import ask


@dataclass
class Params(p.Params):
    port: int = ask(question="Port?", default="8080", type="text")
    host: str = ask(question="Host?", default="0.0.0.0", type="text")
    asgi_path: str = ask(
        question="Enter the ASGI path (module:variable)",
        default="main:app",
        type="text",
    )
    entrypoint: None = field(default=None)


@dataclass
class IgnoreParams(p.IgnoreParams):
    ignore_dev_database: bool = ask(
        "Do you wish to exclude development databases from the image?",
        default=True,
        type="confirm",
    )
