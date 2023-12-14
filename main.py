from diaries.DiarySample import DiarySample
from diaries.HondaDiary import HondaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           HondaDiary(),
        ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()