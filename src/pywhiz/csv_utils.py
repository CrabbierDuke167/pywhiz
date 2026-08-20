import csv


def numeric_extraction(f,c):
    """Inner Function"""
    vr=0
    with open(f,'r',encoding='utf-8') as f:
        ro= csv.DictReader(f)
        for i in ro:
            v=i.get(c)
            try:
                vr.append((i,float(v)))
            except(ValueError,TypeError):
                continue
    return (vr) 


def max_csv(file_name,column):
    """max row"""
    data=numeric_extraction(file_name,column)
    return max(data, key=lambda item: item[1])[0] if data else None

def min_csv(file_name,column):
    """min row"""
    data=numeric_extraction(file_name,column)
    return min(data, key=lambda item: item[1])[0] if data else None

def csv_summary(file_path,column):
    """summary"""
    data =numeric_extraction(file_path,column)
    if not data:
        return None

    return {
        "max_row": max(data, key=lambda item: item[1])[0],
        "min_row": min(data, key=lambda item: item[1])[0],
        "total_valid_entries": len(data),}