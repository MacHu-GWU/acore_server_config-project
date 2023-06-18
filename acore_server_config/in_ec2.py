# -*- coding: utf-8 -*-

"""
该模块用于在 EC2 实例中被调用, 并 "自省" 发现自己的服务器 ID 并在 AWS Parameter Store
找到对应的配置数据并读取.
"""


import typing as T

from simple_aws_ec2.api import Ec2Instance
from acore_server_metadata.api import settings

from .boto_ses import bsm
from .config.define import EnvEnum, Env, Config, Server

if T.TYPE_CHECKING:
    from boto_session_manager import BotoSesManager


def get_server(
    bsm: BotoSesManager = bsm,
    parameter_name_prefix: str = "acore_server_config-",
) -> Server:
    ec2_inst = Ec2Instance.from_ec2_inside(bsm.ec2_client)
    server_id = ec2_inst.tags[settings.ID_TAG_KEY]

    env_name, server_name = server_id.split("-", 1)
    parameter_name = f"{parameter_name_prefix}-{env_name}"

    config = Config.read(
        env_class=Env,
        env_enum_class=EnvEnum,
        bsm=bsm,
        parameter_name=parameter_name,
        parameter_with_encryption=True,
    )
    env = config.get_env(env_name=env_name)
    server = env.servers[server_id]
    return server
