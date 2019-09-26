import os, re, time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='C:/Users/User/Desktop/Python Lab/PhantomJs/bin/phantomjs.exe')
os.system("cls")

destinos = [
    (24, 60),
    (2, 73), (2, 21839), (2, 74), (2, 75), (2, 76), (2, 38), (2, 21840), (2, 77), (2, 78), (2, 37),
    (21, 79), (21, 22942), (21, 15), (21, 16), (21, 17), (21, 21779), (21, 81),
    (50, 85), (50, 13033),
    (19, 97), (19, 59), (19, 99), (19, 100), (19, 21), (19, 22), (19, 18672), (19, 108), (19, 110), (19, 115), (19, 19583), (19, 19672), (19, 118), (19, 24), (19, 20035), (19, 25), (19, 21892), (19, 26), (19, 128), (19, 27), (19, 132), (19, 21890), (19, 139), (19, 28), (19, 142), (19, 143), (19, 144), (19, 147), (19, 10724), (19, 21428), (19, 29),
    (8, 13007), (8, 158), (8, 159), (8, 21780), (8, 160), (8, 13021), (8, 22949), (8, 21874), (8, 10903), (8, 50), (8, 164), (8, 21807), (8, 165), (8, 21894), (8, 21873), (8, 11063),
    (48, 169),
    (51, 21893), (51, 22943), (51, 21838), (51, 21778),
    (3, 178),
    (47, 14549)
]
urls = []
contents = []
totais = []

for x in destinos:    
    urls.append('https://www.stb.com.br/intercambio/idiomas?tipo=&curso=3&idade=&idioma=[2]&pais=[' + str(x[0]) + ']&cidade=[' + str(x[1]) + ']&guide=&busca=true&continente=&duracao=[semana-4]&cargahoraria=[2]&selo=[]&escolas=[]&page=1')

for url in urls:
    driver.get(url)
    time.sleep(10)
    info = driver.find_element_by_class_name("grid-info-idiomas-horizontal").text
    lines1 = info.splitlines()
    lines2 = []

    for line in lines1:
        if 'R$' in line or 'CURSO "' in line:
            lines2.append(line)
    lines3 = [a + " - " + b for a, b in zip(lines2[::2], lines2[1::2])]
    for line in lines3:
        print(line)

    contents += lines3

print()
for line in contents:
    line = line.replace(".", "")
    x = line.find("-")
    line = line[:(x-1)]
    nums = re.findall('\d+', line)
    tot = int(nums[2]) * int(nums[1]) + int(nums[0])
    print(nums, '->', tot)
    totais.append(tot)

print('\n', min(totais))
v = totais.index(min(totais))
print(contents[v])
driver.close()
os.system("pause")
