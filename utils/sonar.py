def measureIncreasingDepth(readings,measurementLength):
    output = 0
    for readingIndex in range(len(readings)-1):
        first_measurement = readings[readingIndex+1:readingIndex+1+measurementLength]
        second_measurement = readings[readingIndex:readingIndex+measurementLength]
        output += sum(first_measurement)>sum(second_measurement)
    return output

