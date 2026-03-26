import dockerfiler.projects.django_uv.params as p
from dataclasses import dataclass
from dockerfiler.projects.utils import ask

@dataclass
class Params(p.Params):
    tailwind_version: int = ask(
        question="Tailwind version?", default="3.4.17", type="text"
    )

@dataclass
class IgnoreParams(p.IgnoreParams):
    pass