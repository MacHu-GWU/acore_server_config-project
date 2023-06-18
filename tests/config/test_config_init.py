# -*- coding: utf-8 -*-

from acore_server_config.config.define import Env, EnvEnum, Config
from acore_server_config.paths import dir_unit_test, path_config_json

path_config_secret_json = dir_unit_test.joinpath("config", "config-secret.json")


def test():
    config = Config.read(
        env_class=Env,
        env_enum_class=EnvEnum,
        path_config=path_config_json,
        path_secret_config=path_config_secret_json,
    )

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

    run_cov_test(__file__, "acore_server_config.config", preview=False)
