a = int(input('Enter a no.'))
b = int(input('Enter a no.'))
try:
    f = open('abc.txt', 'r')
    c = a / b
    print(c)
except ZeroDivisionError:
    print("divisor can't be zero, enter a valid no.")
except NameError:
    print('variable not defined')
except FileNotFoundError:
    print("the file named doesn't exist, check the name again")
except:
    print('something went wrong')
finally:  # closes all the files that have been opened irrespective of any errors
    f.close()
    print("finally all closed")