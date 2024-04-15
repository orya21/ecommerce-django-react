
import os
import pytest

def set_django_settings_module():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

def run_tests():
    # Set the DJANGO_SETTINGS_MODULE environment variable
    set_django_settings_module()
    
    # Run the tests using pytest
    pytest.main(['--html=unit_test_report.html', 'tests'])

if __name__ == "__main__":
    run_tests()
