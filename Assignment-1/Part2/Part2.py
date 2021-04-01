from collections import Counter

def isStringPermutation(s1: str, s2: str) -> bool:
    counter = {}
    counter1 = {}

    for i in s1:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    for j in s2:
        if j in counter1:
            counter1[j] += 1
        else:
            counter1[j] = 1

    return counter == counter1

def isStringPermutationAlternative(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)


def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    hashmap = {}
    pairs = []
    for i in range(len(inputArray)):
        if inputArray[i] in hashmap:
            pairs.append((hashmap[inputArray[i]], i+1))
        else:
            hashmap[targetSum-inputArray[i]] = inputArray[i]

    return pairs

print("String Permuation Check: ")
print(isStringPermutation("asdf", "fsda"))
print(isStringPermutation("asdf", "fsa"))
print(isStringPermutation("asdf", "fsax"))

# print(isStringPermutationAlternative("asdf", "fsda"))
# print(isStringPermutationAlternative("asdf", "fsa"))
# print(isStringPermutationAlternative("asdf", "fsax"))

print("\nPairs that equal sum:")
print(pairsThatEqualSum([1,2,3,4,5], 5))
print(pairsThatEqualSum([1,2,3,4,5], 1))
print(pairsThatEqualSum([1,2,3,4,5], 7))