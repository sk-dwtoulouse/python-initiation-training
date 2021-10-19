"""
Simple demo application to showcase Peewee.

Simple script with model definition to showcase the
use of ORMs and Peewee for beginners in database usage.

"""
import peewee as pw  # pip install peewee
from models import Person


if __name__ == "__main__":  # Only True if current script is executed manually.
    # Initialize a Peewee database for SQLite
    db = pw.SqliteDatabase("database/demo-file.sqlite3")
    # Make the Person model use the database.
    Person.bind(db)
    # Query the `person` table.
    query = Person.select().where(Person.age > 50)

    # Display the results with a friendly formatting.
    print(f"List of people older than 50 years old:\n{'–' * 80}")
    for person in query:  # type: Person
        print(f"{person.id:02d}. {person.get_full_name():<30}: {person.age} years old.")

    # Exemple pour créer un nouvel objet Person dans ma table
    # nouvelle_personne = Person(first_name="Bob", last_name="Bob", age=90)
    # nouvelle_personne.save()
