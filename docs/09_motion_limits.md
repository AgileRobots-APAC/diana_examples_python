# 09 Motion Limits

`08_motion_limits` reads active joint and Cartesian limits from the controller. Use these values as upper bounds before sending motion commands, and keep a safety margin.

The example is read-only and does not call any limit-setting API.
