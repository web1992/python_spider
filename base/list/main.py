#!/usr/bin/env python
# -*- coding:utf-8 -*-


l1 = [2,2]

l2 =   l1*2

# aaaa
print 'aa'*2
# [2,2,2,2]
print l2

#Ture
print '_' in 'abcd_deda'
#False
print '_' in 'dateA'



a1 = ['1','2','3','4']
#1-2-3-4
print '-'.join(a1)

#['H', 'e', 'l', 'l', 'o']
print list('Hello')

print True

print False

# change list
testList = list('test')
testList[0]=2
#[2, 'e', 's', 't']
print testList

del testList[1]
#[2, 's', 't']
print testList

# the method of list

#append
appendList = list('append')
appendList.append('0')
#['a', 'p', 'p', 'e', 'n', 'd', '0']
print appendList

#count
countList = list('listlist')
#2
print countList.count('l')

#extend
extendList = list('extend')
numList = list('123')
extendList.extend(numList)
#['e', 'x', 't', 'e', 'n', 'd', '1', '2', '3']
print extendList

#index

indexList = list('index')
#4
print indexList.index('x')

#insert
insertList = list('insert')
insertList.insert(2,'2')
print insertList
