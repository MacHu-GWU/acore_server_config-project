Solution 解决方案详述
==============================================================================
**首先**, 我们沿用了 `Multi Environment Config Management - S3 Backend <https://github.com/MacHu-GWU/config_patterns-project/blob/main/example/multi_env_json/multi_environment_config_with_s3_backend.ipynb>`_ 文档中的最佳实践, 将每个 environment 的 config 部署到了 AWS S3 中. 每次更新数据, 重新部署的流程为:

1. 修改位于本地的 `/path/to/acore_server_config-project/config/config.json <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/config/config.json>`_ 和 ``${HOME}/.projects/acore_server_config/config-secret.json`` 配置文件, 更新数据.
2. (optional) 更新 :mod:`acore_server_config.config.define.server` 的配置数据结构代码.
3. 运行 `/path/to/acore_server_config-project/tests/config/test_config_init.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/tests/config/test_config_init.py>`_ 单元测试, 确保配置文件的数据结构和配置数据本身相互匹配没有问题.
4. 运行 `/path/to/acore_server_config-project/config/deploy_parameters.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/config/deploy_parameters.py>`_ 脚本呢, 将配置文件部署到 AWS S3 中.

**对于 EC2**, 我们有 :class:`acore_server_config.api.Ec2ConfigLoader <acore_server_config.config.loader.Ec2ConfigLoader>`, 可以用自省的方式自动获取自己的配置数据.

**对于外部项目**, 我们有 :class:`acore_server_config.api.ConfigLoader <acore_server_config.config.loader.ConfigLoader>`, 可以从 backend 读取配置数据.
