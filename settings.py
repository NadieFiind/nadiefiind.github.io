from typing import Dict, List, Any


def _route(title: str) -> Dict[str, Any]:
    return {
        "title": f"{title} | Nadie Fiind" if title else "Nadie Fiind",
        "icon": "/favicon.ico",
        "head": ['<link rel="stylesheet" href="/style.css" />'],
    }


ROUTES: Dict[str, Dict[str, Any]] = {
    "/": _route(""),
    "/about": _route("About"),
    "/skills": _route("Skills"),
    "/projects": _route("Projects"),
    "/services": _route("Services"),
}

PYTHON_DEPENDENCIES: List[str] = []
