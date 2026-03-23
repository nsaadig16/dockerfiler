from dataclasses import dataclass
from dockerfiler.projects.django_uv.params import DjangoUVParams
from dockerfiler.projects.utils import ask

@dataclass
class DjangoTailwindUVParams(DjangoUVParams):
    tailwind_version: int = ask(
        question="Tailwind version?", default="3.4.17", type="text"
    )
