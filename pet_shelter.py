"""Manage a small in-memory pet shelter and its adoption status."""

import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE pets (id INTEGER PRIMARY KEY, name TEXT, species TEXT, "
    "age INTEGER, adopted INTEGER)"
)
ADOPTION_STATE = {"count": 0}


def register_pet(name, species, age, tags=None):
    """Register a pet and append its species to the supplied tags list.

    Args:
        name: The pet's name.
        species: The pet's species.
        age: The pet's age.
        tags: An optional list to append the species to.

    Returns:
        The updated tags list.
    """
    if tags is None:
        tags = []
    conn.execute(
        "INSERT INTO pets (name, species, age, adopted) VALUES (?, ?, ?, 0)",
        (name, species, age),
    )
    tags.append(species)
    return tags


def adopt(pet_id):
    """Mark a pet as adopted and increment the adoption count.

    Args:
        pet_id: The database ID of the pet to adopt.
    """
    conn.execute("UPDATE pets SET adopted = 1 WHERE id = ?", (pet_id,))
    ADOPTION_STATE["count"] += 1


def adoption_code():
    """Return a randomly generated adoption code."""
    return f"PET-{secrets.randbelow(9000) + 1000:04d}"


def oldest_available():
    """Return the oldest available pet's name, or None if none is available."""
    try:
        row = conn.execute(
            "SELECT name, age FROM pets WHERE adopted = 0 ORDER BY age DESC"
        ).fetchone()
    except sqlite3.Error:
        return None
    return row[0] if row is not None else None


def clear_unadopted():
    """Delete all pets that have not been adopted."""
    conn.execute("DELETE FROM pets WHERE adopted = 0")


def shelter_status():
    """Return 'active' if an adoption was recorded, otherwise 'quiet'."""
    if ADOPTION_STATE["count"] > 0:
        return "active"
    return "quiet"


def main():
    """Run the sample shelter registration and adoption workflow."""
    register_pet("Bruno", "dog", 7)
    register_pet("Mitzi", "cat", 3)
    register_pet("Kiwi", "parrot", 12)
    adopt(1)
    print(oldest_available(), adoption_code(), shelter_status())
    clear_unadopted()


main()
