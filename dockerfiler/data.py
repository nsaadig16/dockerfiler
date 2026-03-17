from .projects import params

PROJECTS = {
    "Base Python (uv)": ("uv_base", params.UVBaseParams),
    "Django (uv)": ("django_uv", params.DjangoUVParams),
    "Django + Tailwind (uv)": ("django_tailwind_uv", params.DjangoTailwindUVParams),
    "FastAPI (uv)": ("fastapi_uv", params.FastapiUVParams),
}
