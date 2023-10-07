import pytest
import shutil

from utils import *


@pytest.fixture(scope="function")
def create_and_delete_tmp():
    # Создать каталог tmp, если он еще не создан
    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH)

    yield

    shutil.rmtree('../tmp')
