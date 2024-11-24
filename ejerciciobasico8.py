s = int(input('Escribe una cantidad de segundos: '))
h = s // 3600
restoh = s % 3600
m = restoh // 60
mresto = restoh % 60
print(f'{s} segundos son {h} horas, {m} minutos y {mresto} segundos.')
