from api.my_module import add, user_info


def test_add():
    result = add(2, 3)
    assert result == 5


def test_user_info():
    result = user_info("Kim")
    assert result == {"Hello": "Kim"}
