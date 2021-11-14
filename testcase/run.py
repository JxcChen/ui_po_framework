import pytest
from common.path_handle import REPORT_PATH

cmd = "--alluredir={}".format(REPORT_PATH)
pytest.main([cmd])
