# tqwebhelper2

天勤量化 Web UI 增强版。通过 monkey-patch 替换 tqsdk 默认的 Web 界面，无需修改官方 SDK。

## Preview
实盘

![实盘](https://raw.githubusercontent.com/pseudocodes/tqwebhelper2/main/img/rl.png)

回测

![回测](https://raw.githubusercontent.com/pseudocodes/tqwebhelper2/main/img/bt.png)


## 安装

```bash
pip install tqwebhelper2
```

## 使用

```python
import tqwebhelper2
tqwebhelper2.patch()  # 必须在 TqApi 之前调用

from tqsdk import TqApi, TqAuth
api = TqApi(auth=TqAuth("user", "pass"), web_gui=True)
```

浏览器打开控制台输出的地址即可看到新版 Web 界面。

## 原理

- 继承原版 `TqWebHelper`，只替换 `_web_dir` 指向本包内的编译产物
- 通过 `patch()` 同时替换 `tqsdk.tqwebhelper` 和 `tqsdk.api` 中的引用
- WebSocket 数据通道、路由逻辑完全复用原版，零侵入
- `unpatch()` 可恢复原版


