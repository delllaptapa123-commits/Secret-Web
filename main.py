class Computer:
    number = 0
    def __init__(self, os, officesuite):
        self.os = os
        self.officesuite = officesuite
        Computer.number += 1
        self.num = Computer.number
    def __str__(self):
        return """
    ~PC {} Information~
OS           : {}
Office suite : {}
        """.format(self.num, self.os, self.officesuite)
    @property
    def OS():
        pass
    @OS.setter
    def OS(self, newOS):
        self.os = newOS
    @OS.getter
    def os(self):
        return self.os

Computer1 = Computer("Windows 10", "WPS Office")
Computer2 = Computer("Windows 7", "WPS Office")

print(Computer1)
print(Computer2)

Computer1.OS = "Windows 11"

print(Computer1)
print(Computer2)

input()