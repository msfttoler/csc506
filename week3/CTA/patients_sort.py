# patients_sort.py
"""
This program implements two sorting algorithms (Bubble Sort and Merge Sort)
to sort hospital patient records by last name. Patient records are represented
as dictionaries stored within a list. Although the dataset is modest in this
example, the algorithmic principles apply directly to larger, real-world data
in hospital information systems.
"""

# Sample patient records data
patient_records = [
    {"id": 1001, "first_name": "Alice", "last_name": "Smith", "admission_date": "2025-03-01"},
    {"id": 1002, "first_name": "Bob", "last_name": "Jones", "admission_date": "2025-02-20"},
    {"id": 1003, "first_name": "Carol", "last_name": "Brown", "admission_date": "2025-03-05"},
    {"id": 1004, "first_name": "David", "last_name": "Davis", "admission_date": "2025-01-15"},
    {"id": 1005, "first_name": "Eva", "last_name": "Miller", "admission_date": "2025-03-10"}
]

def bubble_sort(records, key):
    n = len(records)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if records[j][key] > records[j + 1][key]:
                records[j], records[j + 1] = records[j + 1], records[j]
                swapped = True
        if not swapped:
            break
    return records

def merge_sort(records, key):
    if len(records) <= 1:
        return records
    mid = len(records) // 2
    left = merge_sort(records[:mid], key)
    right = merge_sort(records[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

if __name__ == "__main__":
    print("Original Patient Records:")
    for record in patient_records:
        print(record)
    
    print("\nBubble Sorted Patient Records (by last_name):")
    sorted_bubble = bubble_sort(patient_records.copy(), "last_name")
    for record in sorted_bubble:
        print(record)
    
    print("\nMerge Sorted Patient Records (by last_name):")
    sorted_merge = merge_sort(patient_records.copy(), "last_name")
    for record in sorted_merge:
        print(record)