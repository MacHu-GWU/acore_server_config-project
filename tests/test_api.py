# -*- coding: utf-8 -*-

from acore_server_config import api


def test():
    _ = api


if __name__ == "__main__":
    from acore_server_config.tests import run_cov_test

    run_cov_test(__file__, "acore_server_config.api", preview=False)
