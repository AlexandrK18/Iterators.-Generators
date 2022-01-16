def flat_generator(lists):

    for items in lists:

        for item in items:

            yield item


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

for item in flat_generator(nested_list):
	print(item)