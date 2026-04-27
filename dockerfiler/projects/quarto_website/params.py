import dockerfiler.projects.base._params as p
from dataclasses import dataclass
from dockerfiler.projects.utils import ask, QUARTO_VERSIONS
from typing import Optional

@dataclass
class Params(p.Params):
    version : Optional[str] = ask(
        question="Quarto version?",
        default="1.9.32",
        type="select",
        choices=QUARTO_VERSIONS
    )
    port : Optional[str] = ask(question="Port?", default="7722",type="text")
    host : Optional[str] = ask(question="Host?", default="0.0.0.0",type="text")
    main_file : Optional[str] = ask(
        question="Name of the index file?",
        default="index.qmd",
        type="text"
    )

@dataclass
class IgnoreParams(p.IgnoreParams):
    pass