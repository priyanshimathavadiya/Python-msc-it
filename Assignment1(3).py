p = input("Enter password: ")

if not any("A" <= c <= "Z" for c in p):
    print("Uppercase missing")

if not any("a" <= c <= "z" for c in p):
    print("Lowercase missing")

if not any("0" <= c <= "9" for c in p):
    print("Digit missing")

if not any(c in "!@#$%^&*" for c in p):
    print("Special character missing")

for i in range(len(p)-1):
    if p[i] == p[i+1]:
        print("Repeated consecutive characters found")
        break
