import pytest


@pytest.fixture()
def my_fixture():
    print("\n11111")
    yield
    print("\n22222")


def test_my_test(my_fixture):
    print("第一条测试用例")


if __name__ == "__main__":
    pytest.main(['-vs'])
