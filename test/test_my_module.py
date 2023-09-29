from api.my_module import add, user_info

# def add(a, b):
#     return a + b
# def user_info(name):
#     return {"Hello": name}
def test_add():
    result = add(2, 3)
    assert result == 5

def test_user_info():    
    result = user_info("Kim1")
    assert result == {"Hello": "Kim1"}