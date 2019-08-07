class Blacknight:
    def __init__(self):
        self.members = ['one arm','another arm','a leg', 'another leg']

        self.phrases = ['1','2','3','4']

    @property
    def member(self):
        print('next member is:')
        return self.members[0]

    @member.deleter
    def member(self):
        text = 'black knight (loses {})\n--{}'
        print(text.format(self.members.pop(0),self.phrases.pop(0)))


knight =Blacknight()
print(knight.member)

    