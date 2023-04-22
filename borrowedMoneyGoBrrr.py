#this script helps me make borrowing decisions on "investments"

contribution = float(input('how much are you putting in?\n'))
months = int(input('how many months?\n'))
annual_interest = float(input('What is the annual interest in decimal percentage, example: 10 percent is .10\n'))
monthly_interest = (annual_interest/12)
sum_of_tot = 0
print('\n')

for i in range(months):
    that_month = contribution * monthly_interest
    contribution = contribution + that_month
    sum_of_tot = that_month + sum_of_tot
    print(f'month {i+1} = {that_month:.2f} If cash out this month, value needs to be higher than {contribution:.2f}')

print(f'total interest after {months} months = {sum_of_tot:.2f}')
