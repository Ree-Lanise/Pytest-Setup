import pytest
from lib.password_checker import *

def test_if_password_length_is_valid():
    password_checker = PasswordChecker()
    password_checker.check("2827yehdsgd")
    result = password_checker.check("2827yehdsgd")
    assert result == True

def test_if_password_length_is_invalid():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("yhsghk")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."





# class PasswordChecker:
#     def check(self, password):
#         if len(password) >= 8:
#             return True
#         else:
#             raise Exception("Invalid password, must be 8+ characters.")
