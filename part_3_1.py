from timer import Timer

ITEMS = list(range(30000))

with Timer("Calculating sum of normalized items"):
    norm_items = []
    max_item = max(ITEMS)
    for i in ITEMS:
        norm_item = i / max_item
        norm_items.append(norm_item)
    sum_norm = sum(norm_items)

print("The sum of norm items is", sum_norm)
