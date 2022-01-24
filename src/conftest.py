def pytest_addoption(parser):
    parser.addoption("--url", action='store_true', default='https://ya.ru')
    parser.addoption('--status_code', action='store_true', default=200)
