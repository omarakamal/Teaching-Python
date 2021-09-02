#try and accept (error handling)
# it tries whats in try and if it doesnt work it does whats in the except
text = input('Usernme: ')
try:
    number = int(text)
    print(number)
except:
    print('invlid username')
