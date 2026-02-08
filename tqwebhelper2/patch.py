"""
Monkey-patch tqsdk，用 TqWebHelper2 替换原版 TqWebHelper。

核心原理：
  tqsdk/api.py 中通过 `from tqsdk.tqwebhelper import TqWebHelper` 导入，
  然后在 `_setup_connection` 中实例化 `TqWebHelper(self)`。
  
  `from X import Y` 会把 Y 绑定到导入方模块的命名空间，
  所以需要同时 patch tqsdk.tqwebhelper 和 tqsdk.api 两个模块的引用。
"""

_original_class = None
_patched = False


def patch():
    """
    替换 tqsdk 的 TqWebHelper 为 tqwebhelper2 版本。
    必须在 TqApi() 实例化之前调用。
    """
    global _original_class, _patched
    if _patched:
        return

    import tqsdk.tqwebhelper
    import tqsdk.api
    from tqwebhelper2.helper import TqWebHelper2

    # 保存原始类，供 unpatch 恢复
    _original_class = tqsdk.tqwebhelper.TqWebHelper

    # patch 模块属性
    tqsdk.tqwebhelper.TqWebHelper = TqWebHelper2
    # patch 使用方的引用（from import 绑定到 api 模块的局部名称）
    tqsdk.api.TqWebHelper = TqWebHelper2

    _patched = True


def unpatch():
    """恢复原版 TqWebHelper。"""
    global _original_class, _patched
    if not _patched or _original_class is None:
        return

    import tqsdk.tqwebhelper
    import tqsdk.api

    tqsdk.tqwebhelper.TqWebHelper = _original_class
    tqsdk.api.TqWebHelper = _original_class

    _patched = False
    _original_class = None
