from utils import *
from zipfile import ZipFile
import os


def test_files_should_be_zipped():
    # Создать каталог tmp, если он еще не создан
    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH)

    # Заархивировать все файлы из каталога resources в /tmp/resources.zip
    with ZipFile(f'{TMP_PATH}/resources.zip', 'x') as myzip:
        # Рекурсивно проходимся по всем файлам и подкаталогам в каталоге resources
        for root, dirs, files in os.walk(RESOURCES_PATH):
            # Формируем полный путь к текущему файлу
            for file in files:
                file_path = os.path.join(root, file)
                # Определяем относительный путь файла внутри архива
                relative_path = os.path.relpath(file_path, RESOURCES_PATH)
                # Добавляем файл в архив с его относительным путем
                myzip.write(file_path, relative_path)

    # Записать в files_in_archive список файлов из архива /tmp/resources.zip
    with (ZipFile(f'{TMP_PATH}/resources.zip') as myzip):
        files_in_archive = myzip.namelist()

    # Удалить архив /tmp/resources.zip
    os.remove(f'{TMP_PATH}/resources.zip')

    # Проверить, что файл с именем "Python Testing with Pytest (Brian Okken).pdf" помещен в архив
    assert 'Python Testing with Pytest (Brian Okken).pdf' in files_in_archive, \
            f"Файл 'Python Testing wi2th Pytest (Brian Okken).pdf' не найден в архиве"

    # Проверить, что файл с именем "file_example_XLSX_50.xlsx" помещен в архив
    assert 'file_example_XLSX_50.xlsx' in files_in_archive, f"Файл 'file_example_XLSX_50.xlsx' не найден в архиве"

    # Проверить, что файл с именем "file_example_XLS_10.xls" помещен в архив
    assert 'file_example_XLS_10.xls' in files_in_archive, f"file_example_XLS_10.xls' не найден в архиве"

    # Проверить, что файл с именем "hello.zip" помещен в архив
    assert 'hello.zip' in files_in_archive, f"hello.zip' не найден в архиве"
