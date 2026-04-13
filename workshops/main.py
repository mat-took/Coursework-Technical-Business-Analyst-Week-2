"""

AI code:

- Hallucinates
- Over-complicates
- Misses edge cases
- Tends towards verbosity
- Makes you look unprepared

You are still responsible for your code, so you should review and test it carefully before using it in production.

Prompt - Assess - Apply
-> prompt should be the function definition and docstring

"""


def get_name_from_email(email):
    """Extract the name from an email address."""
    name = email.split('@')[0]
    remove_numbers_from_name(name)
    return name.replace('.', ' ').title()


def remove_numbers_from_name(name):
    """Remove numbers from a name."""
    return ''.join([char for char in name if not char.isdigit()])


def get_sigmalabs_email_from_name(name):
    """Generate a Sigmalabs email address from a name."""
    email = name.lower().replace(' ', '.') + '@sigmalabs.co.uk'
    return email


if __name__ == "__main__":
    email = input("Enter your email address: ")
    name = get_name_from_email(email)
    print(f"Hello, {name}!")

    name_input = input("Enter your name: ")
    sigmalabs_email = get_sigmalabs_email_from_name(name_input)
    print(f"Your Sigmalabs email address is: {sigmalabs_email}")
