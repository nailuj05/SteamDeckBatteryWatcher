import logging
import psutil


class Plugin:
    async def getChargeRaw(self) -> int:
        return int(read_from_sys("/sys/class/hwmon/hwmon2/device/charge_now", amount=-1).strip())

    async def test(self) -> str:
        return "Hello World"

    def getCharge(self):
        chargeNow = read_from_sys(
            "/sys/class/hwmon/hwmon2/device/charge_now", amount=-1)
        chargeNow = (7.7 * chargeNow / 1000000)
        return chargeNow

    def getCharge2(self):
        battery = psutil.sensors_battery()
        return battery.percent

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        logging.basicConfig(filename="log.log")
        logging.debug("---MAIN---")
        logging.debug(f"Charge (method 1): {self.getCharge()}")
        logging.debug(f"Charge (method 2): {self.getCharge2()}")
        pass


def read_from_sys(path, amount=1):
    with open(path, mode="r") as f:
        return f.read(amount)
