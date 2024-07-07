from unittest import mock
from src.test_module import test_incrementer
func = test_incrementer
# to get module and qualname relative to where you run your function:
print(f"Module: {func.__module__}")
print(f"Qualname: {func.__qualname__}")

def call_incrementer(num: int) -> int:
    result = test_incrementer(num)
    return result

def test_call_incrementer():
    with mock.patch('logging.Logger.info', return_value=None) as mock_logger:
        assert call_incrementer(1) == 2
        assert mock_logger.call_args_list[0][0][0] == "Incrementing 1"

test_call_incrementer()