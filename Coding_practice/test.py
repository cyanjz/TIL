try:
    x = int(input('Enter a number : '))
    y = 10/x
except ValueError as e:
    print(f'error raised : {e}')
except ZeroDivisionError as e:
    print(f'error raised : {e}')
else:
    print(f'result : {y}')
finally:
    print('program end')