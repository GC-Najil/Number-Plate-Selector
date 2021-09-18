import random

print("Car number plate selection")

numbers = '1234567890'
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

location = input('Choose location (eg : malappuram): ')

if location == 'trivandrum':
    plate = print(f'KL 01 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'kollam':
    plate = print(f'KL 02 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'alappuzha':
    plate = print(f'KL 03 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'pathanamthitta':
    plate = print(f'KL 04 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'kottayam':
    plate = print(f'KL 05 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'idukki':
    plate = print(f'KL 06 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'kochi':
    plate = print(f'KL 07 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'thrissur':
    plate = print(f'KL 08 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'palakkad':
    plate = print(f'KL 09 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'malappuram':
    plate = print(f'KL 10 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'kozhikode':
    plate = print(f'KL 11 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'wayanadu':
    plate = print(f'KL 12 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'kannur':
    plate = print(f'KL 13 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')

if location == 'kasargode':
    plate = print(f'KL 14 {random.choice(chars)}{random.choice(chars)} {random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}')
if location == '':
    print(f'Blank')    
