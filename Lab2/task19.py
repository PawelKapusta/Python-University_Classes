List =[1,3,7,9,22,36,37,58,89,123,456,788]
for i in range(len(List)):
    List[i] = str(List[i]).zfill(3)
print("Given word is:",''.join(map(str,List)))