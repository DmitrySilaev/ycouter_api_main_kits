import sender_stand_request
import data

# Функция для сохранения исходного словаря


def get_kit_body(kit_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения в поле name
    current_body["name"] = kit_name
    # возвращается новый словарь с нужным значением name
    return current_body


# Функция для позитивной проверки


def positive_assert(kit_name):
    # В переменную kit_name сохраняется обновленное тело запроса
    kit_body = get_kit_body(kit_name)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 201
    assert response.status_code == 201
    # Проверяется, что в ответе есть поле name, и оно совпадает с полем name в запросе
    assert response.json()["name"] == kit_name

# Функции для негативной проверки


def negative_assert_code_400(kit_name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(kit_name)

    # В переменную response сохраняется результат запроса
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверка, что код ответа равен 400
    assert response.status_code == 400

    # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


# Тест 1. Успешное создание набора
# Параметр name состоит из 1 символа


def test_create_name_kit_1_letter_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора
# Параметр name состоит из 511 символа


def test_create_name_kit_511_letter_success_response():
    positive_assert("AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                    + "AbcdeAbcdeA")


# Тест 3. Количество символов меньше допустимого
# Ошибка.Параметр name состоит из нуля символов


def test_create_name_kit_0_letter_error_response():
    negative_assert_code_400("")


# Тест 4. Количество символов больше допустимого
# Ошибка.Параметр name состоит из 512 символа


def test_create_name_kit_512_letter_error_response():
    negative_assert_code_400("AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcdeAbcde"\
                             + "AbcdeAbcdeAb")


# Тест 5. Разрешены английские буквы
# Параметр name состоит из букв английского алфавита


def test_create_name_kit_english_letter_success_response():
    positive_assert("QWErty")


# Тест 6. Разрешены русские буквы
# Параметр name состоит из букв русского алфавита


def test_create_name_kit_russian_letter_success_response():
    positive_assert("Мария")


# Тест 7. Разрешены спецсимволы
# Параметр name состоит из спецсимволов


def test_create_name_kit_special_characters_success_response():
    positive_assert("\"№%@\",")


# Тест 8. Разрешены пробелы
# В параметре name допустимы пробелы


def test_create_name_kit_spaces_success_response():
    positive_assert("Человек и КО")


# Тест 9. Разрешены цифры
# Параметр name состоит из цифр


def test_create_name_kit_numbers_success_response():
    positive_assert("123")


# Тест 10. Ошибка, Параметр не передан в запросе
# В запросе нет параметра name


def test_create_name_no_name_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    # Иначе можно потерять данные из исходного словаря
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    del kit_body["name"]
    # Проверка полученного ответа
    negative_assert_code_400(kit_body)


# Тест 11. Ошибка. Передан другой тип параметра
# Тип параметра name: число


def test_create_name_number_type_name_error_response():
    negative_assert_code_400(123)
