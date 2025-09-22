a=["apple","mango","apple","banana","Orange","Pineapple","Pineapple"]
freq={}
for i in a:
    freq[i]=freq.get(i,0)+1
    
print("The Number of Occurances in the list is :\n",freq)