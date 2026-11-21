import sys  # потрібен для аргументів командного рядка (sys.argv)


def parse_log_line(line: str) -> dict:
    """Розбиває рядок логу на дату, час, рівень і повідомлення."""
    # maxsplit=3 дає 4 частини, повідомлення з пробілами лишається цілим
    parts = line.strip().split(maxsplit=3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3],
    }


def load_logs(file_path: str) -> list:
    """Читає лог-файл і повертає список розібраних записів.

    Якщо файл не знайдено або виникла помилка читання,
    виводить повідомлення й повертає порожній список.
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            logs = []
            for line in file:
                # Пропускаємо порожні рядки
                if not line.strip():
                    continue
                try:
                    logs.append(parse_log_line(line))
                except IndexError:
                    # Рядок має менше 4 частин: невірний формат
                    print(f"Пропущено некоректний рядок: {line.strip()}")
        return logs
    except FileNotFoundError:
        # Файлу за вказаним шляхом не існує
        print(f"Файл {file_path} не знайдено")
        return []
    except Exception as e:
        # Будь-яка інша помилка читання (права доступу, кодування тощо)
        print(f"Помилка читання файлу {e}")
        return []


def filter_logs_by_level(logs: list, level: str) -> list:
    """Повертає лише записи вказаного рівня (регістр не важливий)."""
    # Функціональне програмування: filter + lambda.
    # .upper() потрібен, бо користувач пише error, а в логах ERROR
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    """Рахує кількість записів для кожного рівня логування."""
    counts = {}
    for log in logs:
        level = log["level"]
        # .get(level, 0) повертає 0, якщо рівень зустрівся вперше
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict) -> None:
    """Виводить таблицю з кількістю записів за рівнями логування."""
    # Заголовок і роздільна лінія таблиці
    print("Рівень логування | Кількість")
    print("-" * 17 + "|" + "-" * 10)
    # {level:<16} вирівнює рівень по лівому краю в полі шириною 16
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    """Обробляє аргументи командного рядка й запускає аналіз логів."""
    # sys.argv[0] - назва скрипта, [1] - шлях до файлу, [2] - рівень
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень]")
        return
    logs = load_logs(sys.argv[1])
    # Якщо файл не прочитано або він порожній, таблицю не виводимо
    if not logs:
        return

    display_log_counts(count_logs_by_level(logs))

    # Необов'язковий другий аргумент: вивести всі записи цього рівня
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filter_logs_by_level(logs, level):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()