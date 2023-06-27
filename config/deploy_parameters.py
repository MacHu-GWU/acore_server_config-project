# -*- coding: utf-8 -*-

"""
将所有服务器的配置数据部署到 AWS S3. 在这个项目中, 因为集群上的服务器数量多, 配置的内容复杂,
最终配置数据可能会很大. 只有用 AWS S3 才可以存储任意多, 任意大的数据.
"""

from s3pathlib import S3Path
from acore_server_config.boto_ses import bsm
from acore_server_config.config.init import config

s3folder_config = (
    S3Path(f"s3://{bsm.aws_account_id}-{bsm.aws_region}-artifacts")
    .joinpath(
        "projects",
        "acore_server_config",
        "config",
    )
    .to_dir()
)
config.deploy(bsm=bsm, s3folder_config=s3folder_config)
# config.delete(bsm=bsm, s3folder_config=s3folder_config, include_history=True)
