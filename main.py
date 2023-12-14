from diaries.DiarySample import DiarySample
from diaries.k22036_diary import k22036_diary


# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), k22036_diary()]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()