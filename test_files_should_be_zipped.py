from utils import RESOURCES_PATH, TMP_PATH
from zipfile import ZipFile

import os
import shutil


def test_files_should_be_zipped():
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

    # Записать в files_in_resources список файлов из каталога /resources
    files_in_resources = os.listdir(RESOURCES_PATH)

    # Записать в files_in_archive список файлов из архива /tmp/resources.zip
    with (ZipFile(f'{TMP_PATH}/resources.zip') as myzip):
        files_in_archive = myzip.namelist()

    # Проитерировать список и вернуть словарь с ключами тип файла
    resources = {}
    for file_name in files_in_resources:
        if '.xlsx' in file_name:
            resources['xlsx'] = f'{file_name}'
        elif '.xls' in file_name:
            resources['xls'] = f'{file_name}'
        elif '.zip' in file_name:
            resources['zip'] = f'{file_name}'
        elif '.pdf' in file_name:
            resources['pdf'] = f'{file_name}'

    # Удалить архив /tmp/resources.zip
    os.remove(f'{TMP_PATH}/resources.zip')

    # Проверить, что файл с именем "Python Testing with Pytest (Brian Okken).pdf" помещен в архив
    assert resources['pdf'] in files_in_archive, \
        f"Файл {resources['pdf']} не найден в архиве"

    # Проверить, что файл с именем "file_example_XLSX_50.xlsx" помещен в архив
    assert resources['xlsx'] in files_in_archive, \
        f"Файл {resources['xlsx']} не найден в архиве"

    # Проверить, что файл с именем "file_example_XLS_10.xls" помещен в архив
    assert resources['xls'] in files_in_archive, \
        f"Файл {resources['xls']} не найден в архиве"

    # Проверить, что файл с именем "hello.zip" помещен в архив
    assert resources['zip'] in files_in_archive, \
        f"Файл {resources['zip']} не найден в архиве"

    shutil.rmtree('tmp')
