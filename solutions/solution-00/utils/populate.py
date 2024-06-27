""" Populate the database with some data at the start of the application"""

from src.persistence.repository import Repository


def populate_db(repo: Repository) -> None:
    """Populates the db with a dummy country"""
    from src.models.country import Country

    countries = [
        Country(name="Uruguay", code="UY"),
        Country(name="France", code="FR"),
        Country(name="USA", code="US"),
        Country(name="Espagne", code="ES"),
        Country(name="Canada", code="CA"),
    ]

    for country in countries:
        if (repo.get("country", country.code) is None):
            repo.save(country)

    print("Memory DB populated")
