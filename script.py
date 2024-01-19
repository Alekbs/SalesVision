# Укажите путь к вашему файлу
file_path = 'file.txt'

try:
    # Открываем файл на чтение
    with open(file_path, 'r', encoding='utf-8') as file:
        # Читаем содержимое файла
        content = file.read()

    # Удаляем все переносы строк
    content_without_newlines = content.replace('TINYINT(1)', 'INT')

    # Открываем файл на запись
    with open(file_path, 'w', encoding='utf-8') as file:
        # Записываем измененное содержимое файла
        file.write(content_without_newlines)

    print(f"Переносы строк удалены в файле: {file_path}")

except FileNotFoundError:
    print(f"Файл не найден по пути: {file_path}")

except Exception as e:
    print(f"Произошла ошибка: {e}")
