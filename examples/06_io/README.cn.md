# 06 IO

[English](README.md) | [中文](README.cn.md)

演示 `readDI`、`readDO`、`readAI`、`readAO`、总线电流/电压读取，以及可选 `writeDO` 和 `writeAO`。IO API 本身与 Diana/Thor 型号无关，但仍支持 `--model` 做连接后的轴数校验。

```bash
python3 examples/06_io/main.py --model diana7 --ip 192.168.10.75
python3 examples/06_io/main.py --model thor12 --ip 192.168.10.75
```

写 `board/do0`：

```bash
python3 examples/06_io/main.py --model thor12 --ip 192.168.10.75 --set-do=1
```

写模拟输出 `board/ao0`：

```bash
python3 examples/06_io/main.py --model thor12 --ip 192.168.10.75 --set-ao=0:0.0
```

`--set-ao` 格式为 `<mode>:<value>`；务必先确认示教器中的 AO 配置、接线和允许输出范围。

相关教程：[`docs/07_io.cn.md`](../../docs/07_io.cn.md)。
