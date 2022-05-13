import os
import psutil


class Plugin:
    async def GetCharge1(self) -> str:
        b = psutil.sensors_battery()
        return str(b.percent)

    async def GetCharge2(self) -> int:
        return int(read_from_sys("/sys/class/hwmon/hwmon2/device/charge_now", amount=-1).strip())

    async def GetCharge3(self) -> str:
        b = psutil.sensors_battery()
        return str(convertTime(b.secsleft))

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        pass


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def read_from_sys(path, amount=1):
    with open(path, mode="r") as f:
        return f.read(amount)
