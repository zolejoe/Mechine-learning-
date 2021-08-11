# coding_1#计算pi
# from random import random
# from math import sqrt
#
#
# DARTS = 12000
# hits = 0
#
#
# for i in range(1, DARTS):
# 	x, y = random(), random()
# 	dist = sqrt(x**2 + y**2)
# 	if dist <= 1.0:
# 		hits = hits + 1
#
# pi = 4*(hits/DARTS)
# print("pi的值是 %s" %pi)
#

#coding_2 利用函数来减少程序的重复性
# def happy():
# 	print("happy birthday to you")
# 	return
# 	return None
#
# def singmike():
# 	happy()
# 	happy()
# 	print("happy birthday to mike")
# singmike()

# coding_3 函数值返回和调用
def addInterst(balance, rate):
	newbalance = balance * (1 + rate)
	balance = newbalance
	return balance

def main():
	amount = 100
	rate = 0.05
	addInterst(amount, rate)  #没有把形参的计算结果返回给实参
	amount = addInterst(amount, rate) # 把形参的计算结果返回实参，通过值来传递参数（因为python不允许引用，这是python特有的）
	print(amount)
main()

#处理多个账户
def addInterst(balances, rate):
	for i in range(len(balances)):
		balances[i] = balances[i] * (1 + rate)
	return balances

def main():
	amounts = [100,200]
	rate = 0.05
	addInterst(amounts, rate)  #没有把形参的计算结果返回给实参
	amounts = addInterst(amounts, rate) # 把形参的计算结果返回实参，通过值来传递参数（因为python不允许引用，这是python特有的）
	print(amounts)
main()