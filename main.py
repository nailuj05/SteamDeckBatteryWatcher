import logging
import psutil


class Plugin:
    async def GetCharge1(self) -> str:
        logging.debug("reached pythn")
        b = psutil.sensors_battery()
        logging.debug(str(b))
        logging.debug(str(b.percent))
        return str(b.percent)

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        pass
