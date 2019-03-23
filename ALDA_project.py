import json
import numpy as np
#JSON data of 11000 GIFs
json_data = '[{"id": "1000eGIbYHercI","link": "http://webarchive.loc.gov/all/20150318155641/http://media.giphy.com/media/1000eGIbYHercI/giphy.gif","title": "slipper GIF","score": 2},{"id": "1000fHsBSKSL6w","link": "http://webarchive.loc.gov/all/20150318155641/http://media.giphy.com/media/1000fHsBSKSL6w/giphy.gif","title": "swag hustling GIF","score": 0.5}]'
python_obj = json.loads(json_data)    ##changing JSON data to Python Object
gif_IDs = ["1000eGIbYHercI","1000fHsBSKSL6w"]    ##The array of GIFs given by NLP
temp = []
for i in python_obj:
    if i["id"] in gif_IDs:
        temp.append(i)             ##Find the entire tuple of all the GIFs in gif_IDs (it will be better for time complexity if the NLP step gives tuples rather than just IDs)
#HyperParameters set by us, not yet sure on the values yet
T = 0.49
alpha = 0.01
beta = 0.0005

#Paramater taken from user, for how many option he/she wants
n = 10  #Assuming he picks 10
r = round(n/10)  #Keeping 1/10th of randomness in the algorithm, reason explained in PDF
#Quick sort to arrange GIFs in descending order of Scores
def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]["score"]
    for j in range(low , high):
        if   arr[j]["score"] >= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

quickSort(temp,0,1)   #Calling QuickSort

output = []     #All gifs that will be displayed to user
outputs = []    #Keep a track of their index values
for g in range(len(temp)):      #Clearing Threshold
    if temp[g]["score"]<T or g>n-r:
        break
    elif g<(n-r) and temp[g]["score"]>T:
        output.append(temp[g])
        outputs.append(g)
count = 0
executed = 0  #to ensure it doesn't enter an infite loop
while count<r and executed<100:    #Creating random GIFs to display (Reason in pdf)
    executed+=1
    c=int(np.random.uniform(0,len(temp)))
    if c not in outputs:
        output.append(temp[c])
        outputs.append(c)
        count+=1
print(output)    #Final result
for g in output:
    if g["id"]==selected:
    #Change score positively
    #Add tokens of the input to the metadata of the GIF
    else:
    #Change score negatively

##END
