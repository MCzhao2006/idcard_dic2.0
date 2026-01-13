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
check18list = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
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
                    result = 0
                    for i in range(0, len(check18list)):
                        result += (int(before17[i]) * int(check18list[i]))
                    result = result % 11
                    check = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]
                    if gender % 2 == divisor:   # 条件更改除数分流男女
                        for last in range(0, 11):  # 词条组合,并写入文件
                            if last != check[result]:
                                continue
                            if last == 10:  # 最后一位为10替换X
                                last = "X"
                            f.write(f"{begin}{birth}{x}{y}{gender}{last}\n")
elif bl == 2:
    with open(output_file, 'w') as f:
        if not len(last) == 4:
            last = str(input('请输入身份证后四位:'))
        start = int(input("请输入生日起始年份:"))
        end = int(input("请输入生日结束年份:"))
        for year in range(start, end + 1):
            year1 = f"{year}"
            for month in range(1, 13):
                if month < 10:
                    month1 = f"0{month}"
                else:
                    month1 = f"{month}"
                for date in range(1, 32):
                    if date < 10:
                        date1 = f"0{date}"
                    else:
                        date1 = f"{date}"
                    f.write(f"{begin}{year1}{month1}{date1}{last}\n")