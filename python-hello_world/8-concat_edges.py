#!/usr/bin/python3
str = "Python is an object-oriented programming language that lets you work quickly and integrate systems more effectively"
print(str[str.find("object"):str.find("language")] + str[:6])
