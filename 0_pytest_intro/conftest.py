import pytest


@pytest.fixture
def function_fixture(request):
    print("Выполнение обычной фикстуры из конфтест")

    def fin():
        print(f"\n Конец первой фикстуры - {request.scope} ")

    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def class_fixture(request):
    print(f"\n Начало выполнения фикстуры {request.scope} !!")

    def fin():
        print(f"\n Конец выполнения фикстуры {request.scope} !!")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\n Начало выполнения {request.scope} фикстуры")

    def fin():
        print(f"\n окончание выполнения {request.scope} фикстуры")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n Начало выполенения {request.scope} фикстуры!!")

    def fin():
        print(f"\n Конец выполнения {request.scope} фикстуры!")

    request.addfinalizer(fin)


@pytest.fixture(autouse=True)
def always_used_fixture():
    print(f"\n Hello, I'm fixture with autouse and funcction scope used always!")