result = 3
prev_result = 0
i = 2
while True:
        result += (4.0/(i*(i+1.0)*(i+2.0)))-(4.0/((i+2.0)*(i+3.0)*(i+4.0)))
        if prev_result == result:
                break
        prev_result = result
        i += 4
print result