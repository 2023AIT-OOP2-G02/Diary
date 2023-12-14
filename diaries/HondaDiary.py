from diaries.AbstractDiary import AbstractDiary


class HondaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return "グループワークが始まった。"

    def get_author(self):
        return "Honda"
