# The link to the problem:
# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&h_r=next-challenge&h_v=zen

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score       
        
    def comparator(a, b):
        if a.score != b.score:
            return b.score - a.score
        return (a.name>b.name)-(a.name<b.name)

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)