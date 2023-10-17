def my_fun(person=None, fruit=None, custom_message=None):
    """Display information about a person and a fruit."""
    if person:
        print("\nI know a person named " + person + ".")
    if fruit:
        print("They like to eat " + fruit + ".")
    if custom_message:
        print(custom_message)
my_fun(person='Aliza', fruit='apples')
my_fun(person='Kinza', fruit='bananas')
my_fun(person='Maria', fruit='cherries')
my_fun(person='Parwaz', fruit='dates', custom_message='Let\'s go fruit picking!')
