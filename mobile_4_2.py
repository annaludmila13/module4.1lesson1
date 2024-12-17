def test_function():
    # Создаем внутреннюю функцию
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызываем внутреннюю функцию внутри внешней функции
    inner_function()


# Вызываем внешнюю функцию
test_function()

# Попробуем вызвать внутреннюю функцию снаружи
try:
    inner_function()  # Это вызовет ошибку, так как inner_function не доступна за пределами test_function
except NameError as e:
    print(f"Произошла ошибка при попытке вызвать inner_function снаружи: {e}")