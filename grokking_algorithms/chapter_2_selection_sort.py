# Big O notation: O(n^2)

influencers_by_followers = {
    "alice": 1500,
    "bob": 3000,
    "charlie": 1200,
    "dave": 2500,
    "eve": 4000,
}

def selection_sort(influencers: dict[str, int]) -> list[tuple[str, int]]:
    items = list(influencers.items())
    n = len(items)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if items[j][1] < items[min_index][1]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]

    return items


print(selection_sort(influencers_by_followers))
