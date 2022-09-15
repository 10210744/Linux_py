"""Read the documentation of the string methods at
https://docs.python.org/3.5/library/stdtypes.html#string-methods
 You might want to experiment with some of them to make sure you they
 work . strip and replace are particularly useful .
 The documentation uses a syntax that might be confusing . For example , in find ( sub [, start [, end ]]), the brackets indicate optional arguments . So sub is required , but start is optional , and if you include start , then end is optional .
"""
print("please input 7 number")
lst=[]
str=raw_input("请输入数值并用逗号隔开")
lst1=str.split(" ")
i=0
while i<=len(lst1)+1:
	lst1.append(int(lst1.pop()))
	i+=1
def sum(list):
	s=0
	for x in list:
		s+=x
	return s
def average(list):
	avg=0
	avg=sum(list)/(len(list)*1.0)
	return avg
mi=min(lst1)
ma=max(lst1)
print("min="+mi)
print("max="+ma)
print("avg="+avg)