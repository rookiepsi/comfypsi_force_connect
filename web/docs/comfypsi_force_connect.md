# Force Connect

A custom node for ComfyUI that forces a connection between any input and output.

## Usage

This node acts as a universal adapter. Its primary purpose is to override ComfyUI's strict type-checking system, allowing you to connect two sockets (e.g., a `STRING` output to a `COMBO` input) that would normally be incompatible.

## Input

| Name     | Type  | Description                                      |
| -------- | ----- | ------------------------------------------------ |
| `source` | `ANY` | The input data of any type to be passed through. |

## Output

| Name | Type  | Description                                                      |
| ---- | ----- | ---------------------------------------------------------------- |
| `*`  | `ANY` | The original `source` data, passed through without modification. |
