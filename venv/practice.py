# # def read_file(filename):
# #     with open(filename, 'r') as file:
# #         for item in file:
# #             yield item
# #
# #
# # s = read_file('students.txt')
# # print(next(s))
# # print(next(s))
#
# # list_nums = (num * num for num in [1, 2, 5, 19, 22])
# #
# # print(next(list_nums))
# #
# # print(list(list_nums))
#
#
# import datetime
#
# # tday = datetime.date.today()
# # bday = datetime.date(2024, 12, 22)
# #
# # till_bday = bday - tday
# #
# # print(till_bday)
# # # 57 days
#
# t = datetime.datetime(1999,10,30, 10, 33, 12, 44)
#
# tdelta = datetime.timedelta(days=8)
# cdate = t + tdelta
# print(cdate)
# # Outcome 1999-11-07 10:33:12.000044


# understanding different merging structures


list_nums = (num * num for num in [1, 2, 5, 19, 22])

print(next(list_nums))
print(next(list_nums))