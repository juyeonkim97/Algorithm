card=list(range(21))
for _ in range(10):
    ai,bi=map(int,input().split())
    for i in range((bi-ai+1)//2):
        card[ai+i],card[bi-i]=card[bi-i],card[ai+i]
card.pop(0)
for i in card:
    print(i,end=" ")
