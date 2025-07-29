# Reversing a string using slicing
text = "PowerBI"
reversed_text = text[::-1]
print("Reversed String:", reversed_text)



# This is the second code

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))  # True


nums = [12, 5, 89, 22, 65]
max_num = max(nums)
print("Largest Number ever:", max_num)
