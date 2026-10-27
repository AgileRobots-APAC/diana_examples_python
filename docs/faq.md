# FAQ

## 1. Python Cannot Find DianaApi

Initialize the SDK submodule and add the wrapper directory to `PYTHONPATH`:

```bash
git submodule update --init --recursive
export PYTHONPATH="$PWD/third_party/diana_sdk_python/lib:$PYTHONPATH"
```

## 2. `libDianaApi.so` Cannot Be Found

Make sure the native runtime library is in the SDK `lib/` directory and set:

```bash
export LD_LIBRARY_PATH="$PWD/third_party/diana_sdk_python/lib:$LD_LIBRARY_PATH"
```

## 3. The Robot Cannot Be Pinged

Fix network adapter, IP address, netmask, and routing first. Do not start by debugging API code.

## 4. Are `rx ry rz` RPY?

No by default. Diana poses usually use axis-angle vectors. Use `axis2RPY` and `rpy2Axis` when RPY conversion is needed.

## 5. Why Does A Motion Example Not Move?

For safety, motion examples are dry-run by default. Use:

```bash
--model <name> --run
```

to send motion commands.

## 6. How Do Diana And Thor Joint Counts Differ?

Examples call `getJointCount()` after connection and validate the result with the selected profile in `robots/`.
