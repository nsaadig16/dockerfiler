import re
from dockerfiler.cli import select_project, ask_params
from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader
from rich import print
from pathlib import Path
from typing import Dict

env = Environment(
    loader=FileSystemLoader(Path(__file__).parent / "projects"),
    trim_blocks=True,
    lstrip_blocks=True)


def main():
    args = parse_args()

    try:
        project = select_project()
        params = ask_params(project["params"])
        ignore_params = ask_params(project["ignore_params"])
    except KeyboardInterrupt:
        print("[bright_red]DockerFile creation aborted!")
        exit()

    dockerfile_template = project["folder"] + '/' + 'dockerfiler.j2'
    dockerfile = generate_file(template_path=dockerfile_template, params=params)
    output_dockerfile = Path.cwd() / args.output_dockerfile
    output_dockerfile.write_text(dockerfile.strip())
    
    dockerignore_template = project["folder"] + '/' 'ignore.j2'
    dockerignore = generate_file(template_path=dockerignore_template, params=ignore_params)
    output_dockerignore = Path.cwd() / args.output_dockerignore
    output_dockerignore.write_text(dockerignore.strip())

    print("[bright_green]========== DONE! ==========")
    print(
        "[bright_green]Your Dockerfile has been created at " + f"[magenta]{output_dockerfile}\n"
        "[bright_green]Your .dockerignore has been created at " + f"[magenta]{output_dockerignore}"
    )

def parse_args():
    parser = ArgumentParser(
        description="Generate Dockerfiles interactively from templates"
    )
    parser.add_argument(
        "--output-dockerfile",
        "-od",
        type=str,
        default="./Dockerfile",
        help="Output path for the Dockerfile",
    )
    parser.add_argument(
        "--output-dockerignore",
        "-oi",
        type=str,
        default="./.dockerignore",
        help="Output path for the .dockerignore",
    )
    return parser.parse_args()

def generate_file(template_path : str, params: Dict[str,str]) -> str:
    template = env.get_template(str(template_path))
    content = template.render(**params)
    return re.sub(r"\n{3,}", "\n\n", content)


if __name__ == "__main__":
    main()
