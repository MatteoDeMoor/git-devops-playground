def validate_age(age):
    if age < 0:
        return False
    return True


def validate_name(name):
    if not name:
        return False
    return True


if __name__ == "__main__":
    print(validate_age(25))
    print(validate_age(-5))
    print(validate_name("Matteo"))
    print(validate_name(""))
