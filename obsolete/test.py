file = open("good_log.txt", "r")
new = open("better_good_log.txt", "a")

for line in file:
    if "<awaitable>" not in line:
        new.write(line)

file.close()
new.close()
