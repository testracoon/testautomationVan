import time

import pytest
import sys

class MyPlugin:
    def pytest_sessionfinish(self):
        print("\n*** test run reporting finishing")


if __name__ == "__main__":
    print("Test Started")
    retcode = pytest.main(["-s", "-v", "--capture=sys", "--html=./results/towels_report.html"], plugins=[MyPlugin()])
    print("Test Ended")