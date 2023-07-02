def find_common_person(person_a, person_b):
    common_person = sorted(set(person_a).intersection(set(person_b)))
    return common_person

n, m = map(int, input().split())
person_a = []
person_b = []
for _ in range(n):
    friend = str(input())
    person_a.append(friend)
    
for _ in range(m):
    friend = str(input())
    person_b.append(friend)
    
result = find_common_person(person_a, person_b)
if result:
    for person in result:
        print(person)
else:
    print(-1)
        
print(person_a, person_b, result)