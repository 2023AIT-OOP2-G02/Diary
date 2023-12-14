from diaries.DiarySample import DiarySample
from diaries.k22036_diary import k22036_diary
from diaries.k22138_diary import k22138_diary
from diaries.k22028_diary import k22028_diary


# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           k22036_diary(), 
           k22138_diary()]

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), k22036_diary(), k22028_diary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()