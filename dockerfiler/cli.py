import json
from dataclasses import fields
from InquirerPy import inquirer
from dockerfiler.projects import PROJECTS
from typing import Dict

def select_project():
    project = inquirer.fuzzy(
        message="Select project type:",
        choices=list(PROJECTS.keys()),
    ).execute()
    return PROJECTS[project]


def ask_params(dataclass_type) -> Dict[str, str]:
    params = {}
    for f in fields(dataclass_type):
        meta = f.metadata
        if not meta:
            continue
        if meta["type"] == "text":
            answer = inquirer.text(meta["question"], default=meta["default"]).execute()
            if meta.get("list_parse"):
                answer = json.dumps(answer.split())[1:-1]
        elif meta["type"] == "select":
            answer = inquirer.select(
                meta["question"], choices=meta["choices"]
            ).execute()
        elif meta["type"] == "confirm":
            answer = inquirer.confirm(
                meta["question"], default=meta["default"]
            ).execute()
        params[f.name] = answer

    return params
