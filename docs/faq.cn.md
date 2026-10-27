# FAQ

## 1. Python 找不到 DianaApi 模块

确认 SDK 子模块已初始化，并把 wrapper 目录加入 `PYTHONPATH`：

```bash
git submodule update --init --recursive
export PYTHONPATH="$PWD/third_party/diana_sdk_python/lib:$PYTHONPATH"
```

如果临时使用外部 SDK，可改用：

```bash
export PYTHONPATH=/your/path/to/diana_sdk_python/lib:$PYTHONPATH
```

## 2. 运行找不到 libDianaApi.so

确认原生动态库位于 SDK 的 `lib/` 目录，并设置：

```bash
export LD_LIBRARY_PATH="$PWD/third_party/diana_sdk_python/lib:$LD_LIBRARY_PATH"
```

如果使用外部 SDK：

```bash
export LD_LIBRARY_PATH=/your/path/to/diana_sdk_python/lib:$LD_LIBRARY_PATH
```

## 3. ping 不通机器人

先解决网卡、IP、掩码和路由问题；不要先从 API 代码排查。

## 4. `rx ry rz` 是 RPY 吗？

默认不是。Diana API 常用旋转参数为轴角向量。需要 RPY 时使用 `axis2RPY / rpy2Axis` 转换。

## 5. 为什么运动例程不动？

为了避免客户下载后直接发生机器人运动。显式加：

```bash
--model <name> --run
```

才会发送运动命令。

## 6. Diana 和 Thor 关节数不同怎么办？

示例连接后调用 `getJointCount()` 获取真实轴数，并用 `robots/` 中的型号 profile 校验 Diana 7 轴 / Thor 6 轴。
