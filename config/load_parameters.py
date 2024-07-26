# -*- coding: utf-8 -*-

"""
用这个脚本来测试是否你能读取部署的 config 数据.
"""

from acore_server_config.config.loader import ConfigLoader

config_loader = ConfigLoader.new(env_name="sbx")
print(config_loader.get_server("blue"))
