# 08 TCP, Frames, And Payload

`07_tcp_and_frames` reads current TCP pose, default active TCP, default TCP/workpiece coordinate names, and active TCP payload. It does not modify TCP, payload, or workpiece settings.

Payload includes mass, center of mass, and inertia. It affects trajectory planning, dynamics compensation, and force-control behavior.

Tool-relative offsets are converted with:

```text
current TCP homogeneous matrix x tool-frame relative transform
```

`--offset=x,y,z,roll,pitch,yaw` uses meters for position and degrees for RPY input. The example only calculates and prints the target pose.
