# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

a = 75832644 # Впишіть ділене
b = 35 # Впишіть дільник

num = a
div = b

print (" ")
print ("Д І Л И М О   В   С Т О В П Ч И К")
print (" ")
print ("Дана програма ділить в стовпчик до цілого числа .")
print (" ")
print ("Далі діє як звичайний калькулятор .")
print (" ")

digits = list(map(int, str(num)))

print(f"  {num} │ {div}")
print("-", " "*len(digits), "├─" + "─"*max(len(str(div)), len(str(num / div))))
print(" "*len(digits), "  │", num / div )

rem = offset = 0
while digits:
    rem = rem*10 + digits.pop(0)
    if rem > div:
        if offset:
            print(f"{'':<{offset}}  {rem}")
            print(f"{'':<{offset}}-")
        l = len(str(rem))
        res, rem = divmod(rem, div)
        print(f"{'':<{offset}}  {res*div:>{l}}")
        print(f"{'':<{offset}}──", "─"*l, sep="")
        offset += l - len(str(rem)) + (0 if rem else 1)
print(f"{'':<{offset}}  {rem}")
