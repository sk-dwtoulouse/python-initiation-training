import peewee as pw


class Person(pw.Model):
    """
    Model class for the Person table.

    Simple representation as a class of the Person
    table columns. Each object of a Person can be persisted or
    retrieved from the database.

    Attributes:
        Person.id: identifier column. Primary key.
        Person.last_name: N/A
        Person.first_name: N/A
        Person.age: Age of the person in years.

    """
    id = pw.BigAutoField(primary_key=True)
    last_name = pw.CharField(column_name="nom", max_length=30, null=False)
    first_name = pw.CharField(column_name="prenom", max_length=20, null=False)
    age = pw.IntegerField(null=False)

    class Meta:
        indexes = (
            # Make a UNIQUE index with the two following columns
            (("last_name", "first_name"), True),
        )

    def get_full_name(self) -> str:
        """Get the full name of the person."""
        return f"{self.first_name} {self.last_name}"
