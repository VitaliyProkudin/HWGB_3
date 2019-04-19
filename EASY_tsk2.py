#Дан шестизначный номер билета. Определить, является ли билет счастливым.
#Решение реализовать в виде функции.
#Билет считается счастливым, если сумма его первых и последних цифр равны.
#!!!P.S.: функция не должна НИЧЕГО print'ить

User_Ticket= input("Enter nuber  ticket: ")

def luckTicket(User_Ticket)

    a = sum(map(int,User_Ticket[:3]))
    b = sum(map(int,User_Ticket[-3:]))

    if a == b:
         return 'Lucky'
    else:
         return 'UnLucky'
    
print(luckTicket(User_Ticket))


