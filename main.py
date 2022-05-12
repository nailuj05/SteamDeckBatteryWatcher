import os


class Plugin:
    async def GetCharge(self) -> int:
        return int(read_from_sys("/sys/class/hwmon/hwmon2/device/charge_now", amount=-1).strip())

    # A normal method. It can be called from JavaScript using call_plugin_function("method_2", argument1, argument2)
    async def PythonTest(self) -> str:
        return "A string from python"

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        pass


def read_from_sys(path, amount=1):
    with open(path, mode="r") as f:
        return f.read(amount)
