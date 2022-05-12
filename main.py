import os
import psutil


class Plugin:
    async def GetCharge(self) -> str:
        b = psutil.sensors_battery()
        return str(b.percent)

    async def GetCharge2(self) -> int:
        return int(read_from_sys("/sys/class/hwmon/hwmon2/device/charge_now", amount=-1).strip())

    async def GetCharge3(self) -> int:
        return int(read_from_sys("/sys/class/power_supply/BAT0/capacity").strip())

    async def GetCharge4(self) -> int:
        charge = os.system("cat /sys/class/power_supply/BAT0/capacity")
        return int(charge)

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        pass


def read_from_sys(path, amount=1):
    with open(path, mode="r") as f:
        return f.read(amount)
