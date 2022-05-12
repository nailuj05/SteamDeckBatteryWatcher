import psutil


class Plugin:
    async def test(self):
        battery = psutil.sensors_battery()
        return battery.percent

    # A normal method. It can be called from JavaScript using call_plugin_function("method_2", argument1, argument2)
    async def test2(self):
        return "A string from python"

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        pass
