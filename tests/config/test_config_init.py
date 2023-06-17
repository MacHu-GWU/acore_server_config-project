# -*- coding: utf-8 -*-

from acore_server_config.config.init import config


def test():
    # main.py
    _ = config
    _ = config.env

    # server.py
    _ = config.env.servers
    for name, server in config.env.servers.items():
        _ = server.id
        _ = server.db_admin_password
        _ = server.db_username
        _ = server.db_password

    _ = config.env.server_blue
    _ = config.env.server_green


if __name__ == "__main__":
    from acore_server_config.tests import run_cov_test

    run_cov_test(__file__, "acore_server_config.config", preview=False)
