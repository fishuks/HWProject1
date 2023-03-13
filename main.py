import ru_local as ru
import datetime

print(ru.NOMBER)
n = int(input())

data = datetime.date(2009, 9, 25)
data_n = data + datetime.timedelta(n)

DIST = 16637000000                          # миль
SPEED_HOUR = 38241                          # скорость в милях в час

speed_day = SPEED_HOUR * 24                 # скорость в милях в день
distance_ml = DIST + (n * speed_day)        # расстрояние в милях через n дней
distance_km = distance_ml * 1.6934          # расстояние  в километрах через n дней
distance_au = distance_ml / 92955781.16     # расстояние в астрономических единицах через n дней

SPD_OF_RWS = 299792458                      # скорость радиоволны в метрах в секунду
SPD_OF_RWH = SPD_OF_RWS * 3.6               # скорость радиоволны в километрах в час
delay = distance_km / SPD_OF_RWH            # задержка спустя n дней

print(data_n.strftime('%Y-%m-%d'), ru.DISTANCEml, distance_ml)
print(data_n.strftime('%Y-%m-%d'), ru.DISTANCEkm, distance_km)
print(data_n.strftime('%Y-%m-%d'), ru.DISTANCEau, distance_au)
print(n, ru.DELAY, round(delay, 3), ru.HOURS)
