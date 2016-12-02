from single_point import parse

def parse_data(data_file_full_path):
    """ This method parses the data into the final matrix [M x N] - called X matrix.
        and Nx1 vector of classifier results - Y vector.
    """

    final_x_matrix = list()
    final_y_vector = list()
    missing_vectors = list()
    count = 0
    #print data_file_full_path
    f = open(data_file_full_path, "r")
    for line in f:
        count = count+1
        if line.startswith('|'):
            continue

        if line.find("?") > 0:
            missing_vectors.append(line)
            continue
        splitedLine = line.split(', ')

        x, y = parse(splitedLine)
        final_x_matrix.append(x)
        final_y_vector.append(y)

    print "total final x: ", len(final_x_matrix)
    print "total missed: ", len(missing_vectors)
    #print final_x_matrix
    f.close()

    #TODO: handle missed values

    return final_x_matrix, final_y_vector
