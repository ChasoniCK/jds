import json

# Загрузка данных из файла JSON (в данном случае, предполагается, что файл называется data.json)
with open('mainFiles/settings.json', 'r') as file:
    data = json.load(file)

# Получение значения переменной isRoot
is_root_value = data.get('isDebug', None)

# Проверка значения и вывод соответствующего сообщения
if is_root_value is not None:
    if is_root_value:
        print("root - true")
    else:
        print("root - false")
else:
    print("Переменная isRoot отсутствует в файле JSON.")
