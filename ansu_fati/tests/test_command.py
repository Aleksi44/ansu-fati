from ansu_fati.command import execute_from_command_line


def test_command_data_log():
    execute_from_command_line(['logs/data.log'])


def test_command_empty_log():
    execute_from_command_line(['logs/empty.log'])


def test_command_random_log():
    execute_from_command_line(['logs/random.log'])
