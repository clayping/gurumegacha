from config import Restaurant


def welcome_screen():
    with open("welcome_message.txt") as f:
        print(f.read())


def show():
    for restaurant in Restaurant.select():
        display_user_info(restaurant)


def find():
    name = input("Restaurant name > ")
    restaurant = find_or_none(name)
    if restaurant is not None:
        display_user_info(restaurant)
    else:
        print(f"Sorry, {name} is not found")


def add():
    name = input("New restaurant name > ")
    age = input("New restaurant age > ")

    if input_check(name, age):
        return

    restaurant = Restaurant.create(name=name, age=age)

    print(f"Add new restaurant: {restaurant.name}")


def edit():
    name = input("Restaurant name > ")
    restaurant = find_or_none(name)

    if restaurant is None:
        print(f"Not found restaurant name {name}")
        return

    new_name = input(f"New restaurant name({restaurant.name}) > ")
    new_age = input(f"New restaurant age({restaurant.age}) > ")

    if input_check(new_name, new_age):
        return

    restaurant.name = new_name
    restaurant.age = new_age
    restaurant.save()

    print(f"Update restaurant: {restaurant.name}")


def delete():
    name = input("Restaurant name > ")

    restaurant = find_or_none(name)
    if restaurant is None:
        print(f"Sorry, {name} is not found")
        return
    else:
        restaurant.delete_instance()
        print(f"Restaurant {name} is deleted")


def input_check(name, age):
    if name == "":
        print("Restaurant name can't be blank")
        return True

    if age == "":
        print("age can't be blank")
        return True

    if 20 < len(name):
        print("Restaurant name is too long(maximum is 20 characters")
        return True
    
    try:
        int(age)
    except:
        print("Age is not positive integer")
        return True

    if type(age) is int and 120 < int(age):
        print("Age is grater than 120")
        return True

    if find_or_none(name) is not None:
        print(f"Duplicated restaurant name {name}")
        return True

    return False


def display_user_info(restaurant):
    print(f"Name: {restaurant.name} Age: {restaurant.age}")


def find_or_none(name):
    try:
        restaurant = Restaurant.get(Restaurant.name == name)
    except:
        return None
    else:
        return restaurant


if __name__ == "__main__":
    welcome_screen()
    while True:
        input_str = input("Your command > ")
        command = input_str.upper()
        match command:
            case "S":
                show()
            case "F":
                find()
            case "A":
                add()
            case "E":
                edit()
            case "D":
                delete()
            case "Q":
                print("Bye!")
                break
            case _:
                print(f"{command}: command not found")
