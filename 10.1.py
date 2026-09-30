def first_word(text):
    """Поиск первого слова"""

    word = ""

    for char in text:
        # Пропускаем точки, запятые и пробелы в начале
        if not word and char in " .,":
            continue

        # Если нашли разделитель после начала слова
        if word and char in " .,":
            break

        # Добавляем символ к слову
        word += char

    return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')
