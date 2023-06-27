# -*- coding: utf-8 -*-

import os
import pytest

from acore_server_config.config.loader import Ec2ConfigLoader, ConfigLoader


def test():
    config_loader = ConfigLoader.new(env_name="sbx")
    for server_name, server in config_loader.iter_servers():
        pass


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
