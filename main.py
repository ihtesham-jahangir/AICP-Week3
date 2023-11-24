def costSlab1(matrix):
    slab1_cost = sum(matrix[0]) * 10  # Rs.10 per unit in slab 1
    return slab1_cost

def costSlab2(matrix):
    slab2_cost = sum(matrix[1]) * 15  # Rs.15 per unit in slab 2
    return slab2_cost

def costSlab3(matrix):
    slab3_cost = sum(matrix[2]) * 20  # Rs.20 per unit in slab 3
    return slab3_cost

def display_menu(student_id, matrix):
    print(f"Student ID: {student_id}")
    while True:
        choice = input("Press 1 for Slab 1 and 2\nPress 2 for Slab 3 \nPress any other key to exit:\n")
        if choice == '1':
            print(f"Total Bill for Slab 1: Rs.{costSlab1(matrix)}")
            print(f"Total Bill for Slab 2: Rs.{costSlab2(matrix)}")
        elif choice == '2':
            print(f"Total Bill for Slab 3: Rs.{costSlab3(matrix)}")
        else:
            print("Program terminated.")
            break


sample_matrix = [
    [55, 65, 75],  # Slab 1 data
    [120, 150, 170],  # Slab 2 data
    [210, 230, 240]   # Slab 3 data
]


student_id = "XY12345678"


display_menu(student_id, sample_matrix)
