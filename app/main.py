def get_human_age(cat_age: int, dog_age: int) -> list:

    cat = 0
    dog = 0
    if cat_age >= 28:
        cat = 2 + (cat_age - 24) // 4
    elif cat_age >= 24:
        cat = 2
    elif cat_age >= 15:
        cat = 1

    if dog_age >= 29:
        dog = 2 + (dog_age - 24) // 5
    elif dog_age >= 24:
        dog = 2
    elif dog_age >= 15:
        dog = 1

    return [cat, dog]
