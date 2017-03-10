log = open('log.txt', 'w')

l = [0]*10

for i in range(len(l)+1):
    try:
        if l[i] == 0:
            z = 1/l[i]

    except Exception as e:
        #log.write('Error: '+str(e))
        print(e)


log.close()