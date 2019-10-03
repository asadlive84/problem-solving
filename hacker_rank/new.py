

my_dict = dict()

for _ in range(int(input())):
    name = input()
    score = float(input())

    my_dict[name]=score

scores = list(set(my_dict.values()))
scores.remove(min(scores))

names = [k for k,v in my_dict.items() if v == min(scores)]
print(str(names))



print(scores)

