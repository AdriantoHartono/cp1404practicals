# Adrianto Hartono
# 14347930

"""
Programming Languages

Expect: 20 min
Actually: 15 min
"""

class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.title() == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}."