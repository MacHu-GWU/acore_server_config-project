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
        _ = server.ec2_ami_id
        _ = server.ec2_instance_type
        _ = server.ec2_subnet_id
        _ = server.ec2_key_name
        _ = server.ec2_eip_allocation_id
        _ = server.acore_soap_app_version
        _ = server.acore_db_app_version
        _ = server.acore_server_bootstrap_version
        _ = server.db_snapshot_id
        _ = server.db_instance_class
        _ = server.db_admin_password
        _ = server.db_username
        _ = server.db_password
        _ = server.lifecycle
        _ = server.authserver_conf
        _ = server.worldserver_conf
        _ = server.mod_lua_engine_conf

    _ = config.env.server_blue
    _ = config.env.server_green


if __name__ == "__main__":
    from acore_server_config.tests import run_cov_test

    run_cov_test(__file__, "acore_server_config.config.define", preview=False)
