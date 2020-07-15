# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:40:14 2020

@author: jfarm
"""

name = "Jake"
favoriteFood = "Spaghetti"

strConcat = name + "'s favorite food is " + favoriteFood + "!"
print(strConcat)

strFormat = "{}\'s favorite food is {}!".format(name,favoriteFood)
print(strFormat)

strFstr = f"{name}'s favorite food is {favoriteFood}!"
print(strFstr)