# -*- coding: utf-8 -*-

from acore_server_config.boto_ses import bsm
from acore_server_config.config.init import config

config.deploy(bsm=bsm, parameter_with_encryption=True)
# config.delete(bsm=bsm, use_parameter_store=True)
