# from unittest.mock import patch

# def get_cpu_usage():
#     return 50

# def is_overloaded():
#     return get_cpu_usage() > 80

# @patch("test_file2.get_cpu_usage")
# def test_cpu_usage(mock_cpu):
#     mock_cpu.return_value = 90
#     assert is_overloaded() is True

# @patch("test_file2.get_cpu_usage")
# def test_get_cpu_usage(mock_cpu):
#     mock_cpu.return_value = 40
#     assert is_overloaded() is False

