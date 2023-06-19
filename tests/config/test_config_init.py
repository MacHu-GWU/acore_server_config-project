# -*- coding: utf-8 -*-

from acore_server_config.tests.dummy_config import config


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
        _ = server.authserver_conf
        _ = server.worldserver_conf
        _ = server.mod_lua_engine_conf

    _ = config.env.server_blue
    _ = config.env.server_green


if __name__ == "__main__":
    from acore_server_config.tests import run_cov_test

    run_cov_test(__file__, "acore_server_config.config.define", preview=False)
