# -*- coding: utf-8 -*-

from acore_server_config.in_ec2 import get_server


def test():
    server = get_server()
    print(server)


if __name__ == "__main__":
    from acore_server_config.tests import run_cov_test

    run_cov_test(__file__, "acore_server_config.in_ec2", preview=False)
