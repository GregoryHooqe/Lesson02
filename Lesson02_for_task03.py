school_scores = [
                {'school_class': '1a', 'scores': [3,4,4,5,2]},
                {'school_class': '2a', 'scores': [1,5,5,5,4]},
                {'school_class': '3a', 'scores': [2,2,2,1,4]},
                {'school_class': '4a', 'scores': [5,5,5,5,5]},
                {'school_class': '5a', 'scores': [4,4,4,4,1]},
                {'school_class': '6a', 'scores': [3,3,3,3,3]},
                {'school_class': '7a', 'scores': [2,2,2,2,2]}
                ]

total_average = 0
count = 0

for i in school_scores:

    for d in i['scores']:
        total_average += d
        count += 1
    print('Class: {}, Average score: {}'. format(i['school_class'], total_average/count))

print('School average score: {}'.format(total_average/count))
