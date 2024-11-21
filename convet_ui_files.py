import os


def convert(path):
    ui_files = os.listdir(path)
    print(ui_files)
    # Папка, куда будут сохраняться сгенерированные файлы .py
    output_folder = "layouts"

    # Проверка, что папка для выходных файлов существует
    os.makedirs(output_folder, exist_ok=True)

    for ui_file in ui_files:
        # Извлечение имени файла без расширения
        file_name = os.path.basename(ui_file).replace(".ui", "")
        output_file = os.path.join(output_folder, f"{file_name}.py")

        # Формирование команды
        command = f"pyside6-uic {path + ui_file} -o {output_file}"

        # Вывод команды в консоль
        print(command)

        # Выполнение команды
        os.system(command)


if __name__ == '__main__':
    convert('data/etc/')
    convert('data/dialogs/')
