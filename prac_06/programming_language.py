class ProgrammingLanguage:
    """Represents Programming Language object"""
    def __init__(self, name, typing, reflection, year):
        """Initialise a language instance
        name: string, name of language
        typing: string, type
        reflection: Boolean
        year: int, year released"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string of programming language object"""
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if dynamic"""
        return self.typing == 'Dynamic'

