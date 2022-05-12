import os
import psutil


class Plugin:
    async def GetCharge(self) -> str:
        b = psutil.sensors_battery()
        return str(b.percent)
    # A normal method. It can be called from JavaScript using call_plugin_function("method_2", argument1, argument2)

    async def GetCharge2(self) -> float:
        b = psutil.sensors_battery()
        return float(b.percent)

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        pass


def read_from_sys(path, amount=1):
    with open(path, mode="r") as f:
        return f.read(amount)
