import psutil


def GetCharge1() -> str:
    b = psutil.sensors_battery()
    return str(b.percent)


def GetCharge2() -> int:
    return int(read_from_sys("/sys/class/hwmon/hwmon2/device/charge_now", amount=-1).strip())


def GetCharge3() -> str:
    b = psutil.sensors_battery()
    return str(convertTime(b.secsleft))


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def read_from_sys(path, amount=1):
    with open(path, mode="r") as f:
        return f.read(amount)


print(GetCharge1())
print(GetCharge2())
print(GetCharge3())
