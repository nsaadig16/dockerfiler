import re
from .cli import select_project, ask_params
from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))

def main(args):
    try:
        project_id, project_class = select_project()
        params = ask_params(project_class)
    except KeyboardInterrupt:
        print("DockerFile creation aborted!")
        exit()

    dockerfile = generate_dockerfile(project_type=project_id, params=params)
    output_file = Path.cwd() / args.output / "Dockerfile"
    output_file.write_text(dockerfile.strip())

    print("\033[32m=====DONE!=====\033[0m")
    print("\033[32mYour Dockerfile has been created at " + f"\033[35m{output_file}\033[0m")

def generate_dockerfile(project_type: str, params: dict) -> str:
    template = env.get_template(f"{project_type}.j2")
    content = template.render(**params)
    return re.sub(r"\n{3,}", "\n\n", content)


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Generate Dockerfiles interactively from templates"
    )
    parser.add_argument(
        "--output", "-o", type=str, default=".", help="Output path for the Dockerfile"
    )
    args = parser.parse_args()
    main(args)
