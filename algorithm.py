def check_rent(P, H, R):
    earnings = P * H
    if earnings > R:
        print("YES")
    elif earnings == R:
        print("BARELY")
    else:
        print("NO")

# Reading input
P = int(input())  # Pay per hour
H = int(input())  # Hours worked
R = int(input())  # Rent

check_rent(P, H, R)
# The function check_rent calculates the earnings based on the pay per hour and hours worked,
# and compares it with the rent to determine if the earnings are sufficient to cover the rent.