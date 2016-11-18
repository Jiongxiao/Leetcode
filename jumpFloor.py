# 题目描述

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。




# -*- coding:utf-8 -*-
class Solution:
    def a(self,x):
        res=1
        for i in range(1,x+1):
            res*=i
        return res
    
        
    def jumpFloor(self, number):
        # write code here
        # i denotes 1; j denotes 2;
        j=0
        c=0
        while(j<=number/2):
            i=number-2*j
            if j>0 and i>0:
                c=c+self.a(i+j)/self.a(i)/self.a(j)
            else: c+=1
            j=j+1
        return c