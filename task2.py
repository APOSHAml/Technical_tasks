class Animal:
    def __init__(self, name: str, color: str, voice: str):
        self.name = name
        self.color = color
        self.voice = voice

    def print_it_says_voice(self):

        print(f"It says {self.voice}.", end=" ")

        return self

    def print_name_is_color(self):

        print(f"{self.name} is {self.color}.")

        return self


cow = Animal("Besee", "White", "Muuu")

cat = Animal("Barsik", "Black", "Myau")

dog = Animal("Sharik", "Grey", "Gaf")


cow.print_it_says_voice()
print()
cat.print_it_says_voice()
print()
dog.print_it_says_voice()
print()

cow.print_it_says_voice().print_name_is_color()

cat.print_it_says_voice().print_name_is_color()

dog.print_it_says_voice().print_name_is_color()
