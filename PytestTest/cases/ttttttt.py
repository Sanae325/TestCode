# import pytest

# users = [
#   {"name":"jack","password":"Iloverose"},
#   {"name":"rose","password":"Ilovejack"},
#   {"name":"tom","password":"password123"},
#   {"name":"mike","password":"password"},
#   {"name":"james","password":"AGoodPasswordWordShouldBeLongEnough"}
# ]


# class TestUserPasswordWithParam(object):
#     @pytest.fixture(params=users)
#     def user(self, request):
#         return request.params

#     def test_user_password(self, user):
#         passwd = user['password']
#         assert len(passwd) >= 6
#         msg = "user %s has a weak password" %(user['name'])
#         assert passwd != 'password', msg
#         assert passwd != 'password123', msg


# import pytest
# @pytest.mark.parametrize("test_input,expected", [
#     ("3+5", 8),
#     ("2+4", 6),
#     ("6*9", 42),
# ])
# def test_eval(test_input, expected):