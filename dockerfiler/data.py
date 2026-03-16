from .projects import params

PROJECTS = {
    "Base Python (uv)": ("uv_base", params.UVBaseParams),
    "Django (uv)": ("django_uv", params.DjangoUVParams),
    "FastAPI (uv)": ("fastapi_uv", params.FastapiUVParams),
}
