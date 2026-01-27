import time

print("\n用途:生成中国大陆身份证字典,请勿用于非法用途,本作者概不负责\n")
output_file = str(input("请输入生成路径与文件名(如C:/Users/ASUS/Desktop/savefile.txt):"))
ran = int(time.time())    # 使用时间戳,防止重名文件覆盖
if not output_file:
    print(f'未检测到输出文件名,已使用默认文件名"4aVef1le{ran}.txt"')
    output_file = f'4aVef1le{ran}.txt'

bl = int(input("是否知道生日,1知道,2不知道:"))
begin = ""          # 设定空变量，为while做好准备
birth = ""
genderstr = ""
divisor = ""
last = ""
start = 0
end = 0
check18list = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
check = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]
def returnresult():
    result = 0
    for i in range(0, len(check18list)):
        result += (int(before17[i]) * int(check18list[i]))
    result = result % 11
    return result

while not len(begin) == 6:
    begin = str(input("请输入前六位省市区号(如320211):"))
if bl == 1:
    with open(output_file, 'w') as f:
        while not len(birth) == 8:
            birth = str(input("请输入八位生日(如19980405):"))
        while not len(genderstr) == 1:
            genderstr = str(input("请输入性别(如男):"))
        for x in range(0, 10):
            for y in range(0, 10):
                if genderstr == "男":       # 男性余数
                    divisor = 1
                elif genderstr == "女":     # 女性余数
                    divisor = 0
                for gender in range(0, 10):
                    before17 = list(f"{begin}{birth}{x}{y}{gender}")
                    result = returnresult()
                    if gender % 2 == divisor:   # 条件更改除数分流男女
                        for last in range(0, 11):  # 词条组合,并写入文件
                            if last != check[result]:
                                continue
                            if last == 10:  # 最后一位为10替换X
                                last = "X"
                            before17 = ''.join(before17)
                            f.write(f"{before17}{last}\n")
elif bl == 2:
    with open(output_file, 'w') as f:
        while not len(last) == 4:
            last = input('请输入身份证后四位:')
        while start < 1910:
            start = int(input("请输入生日起始年份:"))
        while end < 1910:
            end = int(input("请输入生日结束年份:"))

        for year in range(start, end + 1):
            for month in range(1, 13):
                if month < 10:
                    month = f"0{month}"
                for date in range(1, 32):
                    if date < 10:
                        date = f"0{date}"
                    if month == 2 and date > 29:
                        break
                    birth = str(year)+str(month)+str(date)
                    before17 = list(f"{begin}{birth}{last[0]}{last[1]}{last[2]}")
                    result = returnresult()
                    if last[3] == 'X' or last[3] == 'x':
                        lastint = 10
                    if lastint != check[result]:
                        continue
                    before17 = ''.join(before17)
                    f.write(f"{before17}{last[3]}\n")