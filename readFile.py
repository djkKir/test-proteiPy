def getCsvData(csvPath):
    rows = []
    csvData = open(csvPath)
    for row in csvData:
        list = row.strip().split(";")
        rows.append(list)

    csvData.close()
    return rows