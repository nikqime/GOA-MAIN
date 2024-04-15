#შექმენი ლისტი თამაშებით სადაც იტყვი რა თამაში რამდენჯერ არის ლისტში
games=["pubg","fortnite","fortnite","brawl stars","roblox","pubg"]

print(games.count("pubg"))
print(games.count("fortnite"))
print(games.count("brawl stars"))
print(games.count("roblox"))

#count 

#შექმენი რაღაც გარკვეული ლისტი სადაც იქნება რაღაც საჭმენები და ჩაამატე ლეისის ჩიფსი

food=["burger","cracks","sprite"]
food.append("lays")
print(food)

#append

#შექმენი რაღაც ლისტი სადაც იქნება შეყვანილი რაღაც სასამელი და ჯერ დააამატე ერთი რამე მერე კი ბევრი

drink=["sprite","cola", "fanta"]
drink.append("GOA_Drink-Water")
i="fanta","coca","kola"
drink.extend(i)
print(drink)

#extend 

#შექმენი რაღაც ლისტი და შემდეგ ამოშალე იქიდან ყველაფერი

list=["pubg","fortnite","fortnite","brawl stars","roblox","pubg"]
list.clear()
print(list)

#clear

#შექმენი რაღაც ტანსაცმლის ლისტი და ჩაამატე რაღაცა ტანსაცმელი ხან ბოლოში ხან შუაში და შემდეგ ამოშალე 3 მათგანი სხვადასხვა ადგილიდან
clothes=["T-shirt", "pants", "maika", "hoody"]
clothes.insert(2,"naski") # მეორეში ჯდება naski და მაიკა გადადის მესამეზე
clothes.append("GOA")# ამატებს ბოლოში GOA-ს
clothes.pop(0)#შლის მენულე ელემენტს ანუ T-shirt-ს
clothes.remove("maika")#ამოშლის მაიკას
print(clothes)

#   pop    insert     append     remove






#tast 1 შექმენით საყვარელის ხილის სია და ამოიღეთ ამ სიიდან 1 ხილი შემდეგ ჩაამატეთ 1 ხილი და გაზომეთ სიგრძე სიის
fruits=["apple","pineapple","lemon","peach"]
fruits.append("Strawberry")
fruits.insert(2,"apple")
fruits.pop(-1)
print(fruits)

#test 2 შექმენი რაღაც ლისტი სადაც იქნება შეტანილი რობლოქსის თამაშები და აქედან უნდა ამოვშალო ის თამაშები რაც გამეორდება 2-ჯერ ან მეტჯერ 
list=["kat", "kat", "jail break", "cs", "pls donate", "car", "jail break"]

for i in list:
    if list.


print(list)