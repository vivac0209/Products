# 建立記帳程式專案
# 存取二維清單

# 使用者輸入商品名稱跟價錢
# 建立一個大清單 把小清單加進去
# 會跑出[[ 奶茶, 10 ] , [ 拿鐵 , 50 ] ]
# products=[]
# while True:
# 	name = input('請輸入商品名稱: ')
# 	if name == 'q':
# 		break
# 	price = input('請入商品價格: ')
# 	p = []
# 	p.append(name)
# 	p.append(price)
# 	products.append(p)

# print(products)

# 第一個[0] 是大清單中第0個位置
# 第二個[0] 是抓到大清單的位置後 裡面小清單中第0個位置	
# products[0][0]

# 簡潔寫法1
# p = []
# p.append(name)
# p.append(price)
# 把上面三行改成 p = [name. proce]
# products=[]
# while True:
# 	name = input('請輸入商品名稱: ')
# 	if name == 'q':
# 		break
# 	price = input('請入商品價格: ')
# 	p = [name , proce]
# 	products.append(p)

# print(products)

# 簡潔寫法2
# p = []
# p.append(name)
# p.append(price)
# 直接把p拿掉 在大清單那邊新增時 改成products.append( [name , proce] ) 直接加進去

products=[]
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請入商品價格: ') 			#這邊寫入 是字串喔 不是int
	products.append( [name , price] )

print(products)

# 用for loop 印出清單

for p in products:
	print(p)
	print(p[0])						#抓出清單中所有[0]位置的資料出來
	print(p[0] , '的價格是' , p[1])	#抓出清單中所有[0] [1]位置的資料出來
									#因為for loop是從頭開始跑 所以從第一個資料跑完 才會跑第二個

# 練習寫入檔案 把上面的商品資料寫入檔案中
# 如果一開始沒有txt檔 做寫入的動作時 系統會自動新增txt檔 如果本身已有這檔案 那這動作會覆蓋
# W是指寫入  f是當作這個txt檔 簡稱而已 當作打開的txt檔
# \n 是換行
# with是系統自動幫忙close 檔案

# with open('products.txt' , 'w') as f:			# 打開檔案
# 	for p in products:
# 		f.write(p[0] + ',' + p[1] + '\n')		# 寫入檔案

# txt檔改存成csv檔 資料裡面會有不同屬性 csv也可以用excel打開
# csv檔 通常用逗點做區隔 如果沒有逗點做分隔的話 資料會全在同一格

# 使用utf-8 是因為編碼 要告訴程式用這個編碼 沒有寫的話 新增商品 價格的文字會變成亂碼

with open('products.csv' , 'w' , encoding='utf-8') as f:			# 打開檔案
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')		# 寫入檔案 這邊都是字串


