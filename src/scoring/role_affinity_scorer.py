TECHNICAL_TITLES = [
    "engineer",
    "developer",
    "scientist",
    "architect",
    "ml",
    "machine learning",
    "ai",
    "backend",
    "frontend",
    "full stack",
    "data",
    "analytics",
    "devops",
    "cloud"
]


def calculate_role_affinity_score(title):

    title = title.lower()

    for keyword in TECHNICAL_TITLES:
        if keyword in title:
            return 100

    return 0