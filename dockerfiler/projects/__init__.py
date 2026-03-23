from pathlib import Path
from importlib import import_module

def discover_projects():
    projects = {}
    base_path = Path(__file__).parent

    for init_file in base_path.rglob("*/__init__.py"):
        if init_file.parent == base_path:
            continue

        relative_path = init_file.parent.relative_to(base_path)
        module_name = (
            f"dockerfiler.projects.{relative_path.as_posix().replace('/', '.')}"
        )

        try:
            module = import_module(module_name)
            if hasattr(module, "PROJECT"):
                key = (
                    module.PROJECT["display_name"]
                )
                projects[key] = module.PROJECT
        except ImportError:
            pass  # ignore folders without projects

    return projects

PROJECTS = discover_projects()
