import re
from dotenv import load_dotenv
from .cli import select_project, ask_params
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from .config import TEMPLATES_PATH, OUTPUT_PATH

env = Environment(loader=FileSystemLoader(Path(__file__).parent / TEMPLATES_PATH))
load_dotenv()


def main():
    try:
        project_id, project_class = select_project()
        params = ask_params(project_class)
    except KeyboardInterrupt:
        print("DockerFile creation aborted!")
        exit()

    dockerfile = generate_dockerfile(project_type=project_id, params=params)
    output_file = Path().cwd() / OUTPUT_PATH
    output_file.write_text(dockerfile.strip())

    print("=====DONE!=====")
    print("Your dockerfile has been created at " + OUTPUT_PATH)


def generate_dockerfile(project_type: str, params: dict) -> str:
    template = env.get_template(f"{project_type}.j2")
    content = template.render(**params)
    return re.sub(r"\n{3,}", "\n\n", content)


if __name__ == "__main__":
    main()
