def bit_critera_func(input, pos):

    data = input

    if pos == 12:
        pos = 0

    if len(data) == 1:
        return data[0]

    else:
        count_0 = 0
        count_1 = 0

        for num in data:
            if num[pos] == '0':
                count_0 = count_0 + 1
            elif num[pos] == '1':
                count_1 = count_1 + 1

        if count_1 >= count_0:
            for num in data:
                if num[pos] == '0':
                    data.remove(num)

        else:
            for num in data:
                if num[pos] == '1':
                    data.remove(num)

        bit_critera_func(data, pos+1)
