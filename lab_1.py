#номер 1
name = input("Имя: ").strip()
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")

#
# #номер 2
# a = input("a: ").replace(",", ".")
# b = input("b: ").replace(",", ".")
# a, b = float(a), float(b)
# s = a + b
# avg = s / 2
# print(f"sum={s:.2f}; avg={avg:.2f}")
#
# #номер 3
# price = float(input("Цена: "))
# discount = float(input("Скидка (%): "))
# vat = float(input("НДС (%): "))
# base = price * (1 - discount / 100)
# vat_amount = base * (vat / 100)
# total = base + vat_amount
# print(f"База после скидки: {base:.2f} ₽")
#
# print(f"НДС:               {vat_amount:.2f} ₽")
#
# print(f"Итого к оплате:    {total:.2f} ₽")
#
# #номер 4
# m = int(input("Минуты: "))
# hours = m // 60
# minutes = m % 60
# print(f"{hours}:{minutes:02d}")
#
# #номер 5
# fio = input("ФИО: ")
# fio_stripped = fio.strip()
# parts = fio_stripped.split()
# initials = "".join([p[0].upper() for p in parts]) + "."
# print(f"Инициалы: {initials}")
# print(f"Длина (символов): {len(fio_stripped.replace(' ', ''))}")
#
# #номер 6
# n = int(input())
# onsite = 0
# remote = 0
# for _ in range(n):
#     surname, name, age, form = input().split()
#     if form == "True":
#         onsite += 1
#     else:
#         remote += 1
# print(onsite, remote)
#
# #номер 7
# s = input().strip()
# start = next(i for i, ch in enumerate(s) if ch.isupper())
# digit_index = next(i for i, ch in enumerate(s) if ch.isdigit() and i + 1 < len(s))
# step = (digit_index + 1) - start
# decoded = ""
# for i in range(start, len(s), step):
#     decoded += s[i]
#     if s[i] == ".":
#         break
# print(decoded)