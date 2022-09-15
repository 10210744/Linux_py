total = 0
count = 0
average = 0
input_num=[]
while True:
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        inp = float(num)
    except:
        print("Innalid input")
        continue
    total = total + inp
    count = count + 1
    average = total / count
print( total, count, average)

