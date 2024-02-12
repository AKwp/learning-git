shopping_list = {"piekarnia": ["chleb" , "pączek", "bułki"], "warzywniak": ["marchew", "seler", "rukola" ]}
capi = {x.capitalize():[y.capitalize() for y in v] for x,v in shopping_list.items()}
for p,r in capi.items():
    print(f"Idę do {p}, kupuję tu następujące rzeczy: {r}.")
    
count = 0
for i in capi:
    if isinstance(capi[i], list):
        count += len(capi[i])
print(f"W sumie kupuję {count} produktów.")

i = 0
divide_list = []
for i in range (0,101,1):
    if i % 5 == 0 and i != 0:
        divide_list.append(i)
print(divide_list)
sq = [(element * element * element) for element in divide_list  ]
print(sq)
print("Prawie ok")
