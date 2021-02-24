# 建立記帳程式專案
# 存取二維清單

# 使用者輸入商品名稱跟價錢
# 建立一個大清單 把小清單加進去
# 會跑出[[ 奶茶, 10 ] , [ 拿鐵 , 50 ] ]
products=[]
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)

print(products)

# 第一個[0] 是大清單中第0個位置
# 第二個[0] 是抓到大清單的位置後 裡面小清單中第0個位置	
products[0][0]

# 簡潔寫法1
# p = []
# p.append(name)
# p.append(price)
# 把上面三行改成 p = [name. proce]
products=[]
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請入商品價格: ')
	p = [name. proce]
	products.append(p)

print(products)

# 簡潔寫法2
# p = []
# p.append(name)
# p.append(price)
# 直接把p拿掉 在大清單那邊新增時 改成products.append( [name. proce] ) 直接加進去

products=[]
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請入商品價格: ')
	products.append( [name. proce] )

print(products)