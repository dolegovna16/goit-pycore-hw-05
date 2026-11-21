def input_error(func):
    """Декоратор: перехоплює помилки введення й повертає повідомлення."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            # Не вистачає (або забагато) аргументів: add Bob
            return "Enter the argument for the command"
        except IndexError:
            # Аргументів немає зовсім: phone
            return "Enter the argument for the command"
        except KeyError:
            # Контакту немає в словнику
            return "Contact not found."

    return inner


def parse_input(user_input):
    # Ріжемо рядок на слова по пробілах: "add John 123" -> ["add", "John", "123"]
    parts = user_input.split()

    # Якщо користувач нічого не ввів (просто Enter), повертаємо порожню команду
    if not parts:
        return "", []

    # Перше слово це команда, решта це аргументи
    cmd, *args = parts

    # Робимо команду маленькими літерами, щоб HELLO і hello були однаковими
    cmd = cmd.strip().lower()

    # Повертаємо команду і список аргументів
    return cmd, args


@input_error
def add_contact(args, contacts):
    # Якщо аргументів не 2, розпакування кине ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    # Якщо аргументів не 2, розпакування кине ValueError
    name, phone = args
    # Звернення до ключа кине KeyError, якщо контакту немає
    contacts[name]
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    # Якщо аргументів немає, args[0] кине IndexError
    name = args[0]
    # Якщо контакту немає, contacts[name] кине KeyError
    return contacts[name]


@input_error
def show_all(contacts):
    # Якщо словник порожній, так і кажемо
    if not contacts:
        return "No contacts saved."

    # Робимо з кожної пари рядок "ім'я: номер"
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    # Словник для контактів, живе поки працює бот
    contacts = {}

    print("Welcome to the assistant bot!")

    # Нескінченний цикл: бот постійно чекає команди
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # Вихід з програми
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # Кожна команда викликає свою функцію, а main друкує результат
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


# Запускаємо main() тільки якщо файл запустили напряму
if __name__ == "__main__":
    main()