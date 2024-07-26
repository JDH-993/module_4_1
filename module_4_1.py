from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(int(input()), int(input()))
result2 = fake_divide(int(input()), int(input()))
result3 = true_divide(int(input()), int(input()))
result4 = true_divide(int(input()), int(input()))
print(result1)
print(result2)
print(result3)
print(result4)
