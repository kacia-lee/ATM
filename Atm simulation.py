int_amt=4000
while True:
    initial=int(input('What would you like to do? 1. Check balance 2. Deposit 3. Withdraw 4. Exit \n'))
    if initial==1:
        print(f'The current balance is {int_amt}')
    elif initial==2:
        deposit=int(input('How much would you like to deposit? '))
        if deposit==0:
            print(f'No amount was deposited. The current value is still {int_amt}')
        elif deposit<0:
            print('Invalid amount. Please enter a positive integer value')
        else:
            int_amt=int_amt+deposit
            print(f'The current balance is now {int_amt}')
    elif initial==3:
        withdraw=int(input('How much would you like to withdraw? '))
        if withdraw==0:
            print(f'No amount was withdrawn. The current balance is still {int_amt}')
        elif withdraw<0:
            print('Invaild amount. Please enter a positive integer.')
        elif withdraw>int_amt:
            print('Insufficient balance.')
        else:
            int_amt=int_amt-withdraw
            print(f'The current balance is now {int_amt}')
    elif initial==4:
        print('Exiting the application...')
        break
    else :
        print('Please choose a valid option')
