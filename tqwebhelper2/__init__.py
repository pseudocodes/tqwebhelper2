"""
tqwebhelper2 — 天勤量化 Web UI 增强版

用法：
    import tqwebhelper2
    tqwebhelper2.patch()  # 在 TqApi() 之前调用

    from tqsdk import TqApi, TqAuth
    api = TqApi(auth=TqAuth("user", "pass"), web_gui=True)
"""

__all__ = ['patch', 'unpatch']
__version__ = '0.1.0'


def patch():
    """替换 tqsdk 的 TqWebHelper 为 tqwebhelper2 版本。"""
    from tqwebhelper2.patch import patch as _patch
    _patch()


def unpatch():
    """恢复原版 TqWebHelper。"""
    from tqwebhelper2.patch import unpatch as _unpatch
    _unpatch()
