from single_point import parse


def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """
    final_x_matrix = list()
    final_y_vector = list()
    missing_vectors_x = list()
    missing_vectors_y = list()
    avg = [0]*14
    count = 0

    f = open(data_file_full_path, "r")
    for line in f:
        if line.startswith('|'):
            continue

        is_missed = line.find("?") > 0
        splited_line = line.split(', ')

        x, y = parse(splited_line)

        # handling missed data: put feature average on missed feature
        count += 1
        for col in range(0, len(x)):
            if int(x[col]) > -1:
                avg[col] += int(x[col])

        if not is_missed:
            final_x_matrix.append(x)
            final_y_vector.append(y)
        else:
            missing_vectors_x.append(x)
            missing_vectors_y.append(y)

    # calculate average of each feature and replace missing values
    for i in range(0, len(avg)):
        avg[i] = avg[i]/count

    for i in range(0, len(missing_vectors_x)):
        for j in range(0, len(missing_vectors_x[i])):
            if missing_vectors_x[i][j] < 0:
                missing_vectors_x[i][j] = avg[j]

    final_x_matrix += missing_vectors_x
    final_y_vector += missing_vectors_y
    f.close()

    return final_x_matrix, final_y_vector
