# -*- coding:utf-8 -*-
x = "There are %d types of people." %10
bingry = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(bingry,do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious  # 两个变量相连

w = "This is the left side of..."
e = "a string with aright side."

print w + e # 两个字符串想连