SCOPES_BY_ROLE = {
    "admin": {
        "usuarios:read",
        "usuarios:create",
        "laboratorios:read",
        "laboratorios:create",
        "laboratorios:update",
    },
    "usuario": {
        "laboratorios:read",
    },
}


def get_scopes_for_role(role: str) -> set[str]:
    return SCOPES_BY_ROLE.get(role, set())
