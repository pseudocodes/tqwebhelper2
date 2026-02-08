"""
TqWebHelper2 — 继承原版 TqWebHelper，仅替换 web 静态文件目录。

设计原则：
  - 继承而非重写，最大限度复用原版逻辑（WebSocket、数据处理、路由等）
  - 只覆盖 web 目录指向，让 tqsdk 加载我们编译好的 tqsdk-web3 前端
  - 如果未来需要自定义路由或数据处理，可以在此类中 override 对应方法
"""

import os
from tqsdk.tqwebhelper import TqWebHelper


# tqwebhelper2/web/ 目录（编译好的 tqsdk-web3 输出）
WEB_DIR = os.path.join(os.path.dirname(__file__), 'web')


class TqWebHelper2(TqWebHelper):

    async def _run(self, api_send_chan, api_recv_chan, web_send_chan, web_recv_chan):
        """覆盖 _run，在启动前替换 web 目录指向。"""
        # 原版在 _run 中设置 self._web_dir = os.path.join(os.path.dirname(__file__), 'web')
        # 我们在 super()._run() 之前不能直接改，因为 _web_dir 是在 _run 内部赋值的。
        # 所以用更可靠的方式：覆盖 _run，让 _web_dir 指向我们的目录。
        if self._api._web_gui:
            self._web_dir = WEB_DIR
        await super()._run(api_send_chan, api_recv_chan, web_send_chan, web_recv_chan)

    async def link_httpserver(self):
        """确保 httpserver 使用我们的 web 目录。"""
        self._web_dir = WEB_DIR
        await super().link_httpserver()
