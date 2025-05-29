class gmail:
    def email(self):
        self.str1=str(input("Enter The Value To see if it is a gmail:"))
        self.isTrue=False
        if '@'and '.' and 'com' in self.str1:
            self.isTrue = True
            pass
        if self.isTrue:
            return True
ca=gmail()
print(ca.email())
