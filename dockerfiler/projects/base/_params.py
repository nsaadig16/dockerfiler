from dataclasses import dataclass
from dockerfiler.projects.utils import ask

@dataclass
class Params:
    pass

@dataclass
class IgnoreParams:
    ignore_docs: bool = ask(
        question="Do you wish to exclude the docs from the image?",
        default=True,
        type="confirm",
    )