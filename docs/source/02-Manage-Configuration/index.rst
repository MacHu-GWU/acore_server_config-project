Manage Configuration
==============================================================================

.. note::

    这个项目的配置管理功能由 `config_patterns <https://github.com/MacHu-GWU/config_patterns-project>`_ Python 库提供. 建议你先阅读该项目的文档, 有一个大该的了解既可.


Declare Configuration Schema
------------------------------------------------------------------------------
每个 Environment 下会有多个 Server (environment 和 server 的概念请参考 `这篇文档 <https://acore-server-metadata.readthedocs.io/en/latest/search.html?q=Environment+Name+and+Server+Name&check_keywords=yes&area=default>`_). 一个 Server 的详细配置是在 `acore_server_config/config/define/server.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/acore_server_config/config/define/server.py>`_ 模块中被定义的. :class:`~acore_server_config.config.define.server.Server` 类的实例代表了一个 Server 的配置数据. 下面是该模块的源码:

.. dropdown:: acore_server_config/config/define/server.py

    .. literalinclude:: ../../../acore_server_config/config/define/server.py
       :language: python
       :linenos:


Local Configuration Data
------------------------------------------------------------------------------
配置数据的源头是由管理员在本地编写好数据文件然后部署到 AWS S3 中的. 本地的配置文件分两个, 普通配置数据的 `config/config.json <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/config/config.json>`_, 和敏感配置数据的 ``${HOME}/.projects/acore_server_config/config-secret.json`` 文件 (这是一个本地路径). 普通配置数据文件会被 check in 到 Git 中, 而敏感配置数据不会.

而读取 Configuration Data 会有两种情况:

1. 管理员在本地开发时从本地数据文件中读取数据.
2. 游戏服务器在 EC2 上运行程序并读取数据.

下面我们分情况来介绍.

.. _load-configuration-data-from-local-files:

1. Load Configuration Data From Local Files
------------------------------------------------------------------------------
`acore_server_config/config/init.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/acore_server_config/config/init.py>`_ 模块实现了从本地文件中读取配置数据的功能. 你只要运行 ``from acore_server_config.config.init import config`` 既可获得一个 config 对象. 该模块的源码如下:

.. dropdown:: acore_server_config/config/init.py

    .. literalinclude:: ../../../acore_server_config/config/init.py
       :language: python
       :linenos:


2. Load Configuration Data From AWS S3 on EC2
------------------------------------------------------------------------------
`acore_server_config/config/loader.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/acore_server_config/config/loader.py>`_ 模块实现了从 AWS S3 中读取配置数据的功能. 它有两个关键的类:

1. :class:`~acore_server_config.config.loader.ConfigLoader`: 让管理员从 AWS S3 上读取配置数据. 管理员在部署了配置数据后可以用这个类从 AWS S3 将其读回来. 该操作常用于 Debug.
2. :class:`~acore_server_config.config.loader.Ec2ConfigLoader`: 让运行在 EC2 上的脚本自己发现 (自省) 自己是哪个服务器, 然后到对应的 AWS S3 object 中读取属于自己的配置数据. 游戏服务器启动时的自动化脚本就会用到这个类.

下面是该模块的源码:

.. dropdown:: acore_server_config/config/loader.py

    .. literalinclude:: ../../../acore_server_config/config/loader.py
       :language: python
       :linenos:

.. note::

    TODO: 介绍一下我们的 boostrap 程序是如何用这个库来将配置数据应用到游戏服务器上的.


.. _deploy-configuration-data:

Deploy Configuration Data
------------------------------------------------------------------------------
管理员用 :ref:`load-configuration-data-from-local-files` 中的方法从本地配置文件中读取配置数据后, 就可以将其部署到 AWS S3 上了. `config/deploy_parameters.py <https://github.com/MacHu-GWU/acore_server_config-project/blob/main/config/deploy_parameters.py>`_ 脚本里有示例代码. 我个人也是用这个脚本来部署配置数据的. 该脚本的源码如下:

.. dropdown:: config/deploy_parameters.py

    .. literalinclude:: ../../../config/deploy_parameters.py
       :language: python
       :linenos:

每次部署的时候, 我们不会 overwrite 已经存在的配置数据, 而是自动创建一个新的版本. 在 AWS S3 上的目录结构如下::

    # 配置数据的根目录
    s3://bucket/projects/acore_server_config/config/
    # 这个目录下的配置数据文件是包含了所有环境的配置数据
    s3://bucket/projects/acore_server_config/config/acore_server_config/
    # 这几个目录只包含了属于自己环境的配置数据
    s3://bucket/projects/acore_server_config/config/acore_server_config-sbx/
    s3://bucket/projects/acore_server_config/config/acore_server_config-tst/
    s3://bucket/projects/acore_server_config/config/acore_server_config-prd/
    # 我们就拿 production 为例, 其他几个文件夹下的结构类似
    # 每个环境的配置都会有一个 latest 文件和所有的历史版本文件, latest 中的数据永远和最新的历史版本一样
    s3://bucket/projects/acore_server_config/config/acore_server_config-prd/acore_server_config-prd-latest.json
    s3://bucket/projects/acore_server_config/config/acore_server_config-prd/acore_server_config-prd-000001.json
    s3://bucket/projects/acore_server_config/config/acore_server_config-prd/acore_server_config-prd-000002.json
    s3://bucket/projects/acore_server_config/config/acore_server_config-prd/acore_server_config-prd-000003.json

.. note::

    之所以不用 parameter store 是因为配置数据可能会很大


I Lost My Local Secret Configuration File
------------------------------------------------------------------------------
如果你是管理员, 并且不慎将本地的敏感配置数据文件删除了, 那么你可以到 AWS S3 上去找到 ``s3://bucket/projects/acore_server_config/config/acore_server_config/acore_server_config-latest.json`` 文件将其下载到本地, 然后把 ``secret_data`` key 下面的内容复制到 ``${HOME}/.projects/acore_server_config/config-secret.json`` 文件中既可.


Update Game Server Config By Restarting EC2
------------------------------------------------------------------------------
当你要更改游戏服务器配置时, 你通常需要将游戏服务器临时关闭, 更新配置, 然后重新启动. 由于我们的 EC2 重启时有 bootstrap 程序, 会从 AWS S3 从新读取并应用配置数据. 所以你可以简单的关闭 world server, 然后关闭 EC2, 用 :ref:`deploy-configuration-data` 中的方法更新数据, 然后启动 EC2 既可.


Update Game Server Config Without Restarting EC2
------------------------------------------------------------------------------
这一节介绍了如何在只重启 world server, 但是不重启 EC2 的情况下更新配置数据.

TODO 以后再补充说如何做.
