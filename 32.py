#Write a Python program to find the common elements between two lists.

firstList = ["apple","banana","grapes","purple"]
secondList = ["ant","bat","cow","purple"]
common = set(firstList) & set(secondList)
print(common)