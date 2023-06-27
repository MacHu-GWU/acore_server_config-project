# -*- coding: utf-8 -*-

import os
import pytest
from acore_server_config.in_ec2 import get_server


def test():
    server = get_server(server_id="sbx-blue")
    print(server)


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
