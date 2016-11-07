#coding=utf-8
import math
from toolkits import calobjvalue,calfitvalue,best,selection,crossover,mutation

def b2d(b): #将二进制转化为十进制 x∈[0,10]
    t = 0
    for j in range(len(b)):
        t += b[j] * (math.pow(2, j))
    t = t * 10 / 1023
    return t

popsize = 50 #种群的大小
#用遗传算法求函数最大值：
#f(x)=10*sin(5x)+7*cos(4x) x∈[0,10]

chromlength = 10 #基因片段的长度
pc = 0.6 #两个个体交叉的概率
pm = 0.001; #基因突变的概率
results = []
bestindividual = []
bestfit = 0
fitvalue = []
tempop = [[]]
pop = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  for i in range(popsize)]
for i in range(1000): #繁殖100代
    objvalue = calobjvalue(pop) #计算目标函数值
    fitvalue = calfitvalue(objvalue); #计算个体的适应值
    [bestindividual, bestfit] = best(pop, fitvalue) #选出最好的个体和最好的函数值
    results.append([bestfit,b2d(bestindividual)]) #每次繁殖，将最好的结果记录下来
    selection(pop, fitvalue) #自然选择，淘汰掉一部分适应性低的个体
    crossover(pop, pc) #交叉繁殖
    mutation(pop, pc) #基因突变
    

results.sort(key=lambda x:x[0]) 
for ele in results:
    print ele   
#print(results) #打印函数最大值和对应的