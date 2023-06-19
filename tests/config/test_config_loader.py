# -*- coding: utf-8 -*-

import moto
from acore_server_config.config.loader import (
    Env,
    EnvEnum,
    Config,
    Ec2ConfigLoader,
    ConfigLoader,
    _get_default_s3folder_config,
)
from acore_server_config.tests.mock_aws import BaseMockTest
from acore_server_config.tests.dummy_config import config


class TestConfigLoader(BaseMockTest):
    mock_list = [
        moto.mock_s3,
        moto.mock_sts,
    ]

    @classmethod
    def setup_class_post_hook(cls):
        bucket = f"{cls.bsm.aws_account_id}-{cls.bsm.aws_region}-artifacts"
        cls.bsm.s3_client.create_bucket(Bucket=bucket)
        s3folder_config = _get_default_s3folder_config(bsm=cls.bsm)
        config.deploy(bsm=cls.bsm, s3folder_config=s3folder_config, verbose=False)

    def _test_ec2_config_loader(self):
        server = Ec2ConfigLoader.load(bsm=self.bsm, server_id="sbx-blue")
        assert server.id == "sbx-blue"

    def _test_config_loader(self):
        config_loader = ConfigLoader.new(
            bsm=self.bsm,
            env_name="sbx",
            parameter_name_prefix="acore_server_config",
        )
        config_loader.iter_servers()
        server = config_loader.get_server(server_name="blue")
        assert server == config_loader._env.server_blue
        assert server.id == "sbx-blue"

    def test(self):
        self._test_ec2_config_loader()
        self._test_config_loader()


if __name__ == "__main__":
    from acore_server_config.tests import run_cov_test

    run_cov_test(__file__, "acore_server_config.config.loader", preview=False)
