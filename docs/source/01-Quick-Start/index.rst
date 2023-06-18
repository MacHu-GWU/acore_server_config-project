Quick Start 快速上手
==============================================================================


批量部署服务器配置数据
------------------------------------------------------------------------------
1. 修改配置数据的 Schema: 修改 `acore_server_config/config/define/server.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/acore_server_config/config/define/server.py>`_ 模块即可.
2. 根据配置数据的 Schema, 填入配置数据:
    - 对于非敏感数据, 可以填入 `config/config.json <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/config/config.json>`_ 中
    - 对于敏感数据, 可以填入 ``${HOME}/.projects/acore_server_config/config-secret.json`` 中. 本项目中各种账号密码, 服务配置都属于敏感数据.
3. 部署配置数据: 运行 `python config/deploy_parameter.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/config/deploy_parameters.py>`_ 脚本即可将配置部署到 AWS Parameter Store, 专用的配置数据管理服务中.


在服务器上读取对应的配置数据
------------------------------------------------------------------------------
你可以在 EC2 服务器上的自动化脚本中插入以下代码来读取配置数据:

.. code-block:: python

    >>> from acore_server_config.api import get_server
    >>> server = get_server()
    >>> server
    Server(id='sbx-blue', db_admin_password='sbx*dummy4test', db_username='myuser', db_password='sbx*dummy4test', ...)

如果你不想使用默认的 boto session (默认使用 EC2 的 IAM Instance Profile), 或想要更改 ``s3folder_config`` 或 ``parameter_name_prefix``, 你可以这样:

.. code-block:: python

    >>> from boto_session_manager import BotoSesManager
    >>> bsm = BotoSesManager(
    ...     profile_name=...,
    ...     region_name=...,
    ...     aws_access_key_id=...,
    ...     aws_secret_access_key=...,
    ... )
    # 这样
    >>> server = get_server(bsm, s3folder_config="s3://mybucket/myfolder/config/")
    # 或这样
    >>> server = get_server(bsm, parameter_name_prefix="your_own_prefix")
