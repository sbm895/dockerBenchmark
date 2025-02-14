import time as t 


def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

array = [5, 5, 27, 34, 59, 97, 79, 23, 60, 87, 46, 90, 50, 57, 12, 85, 18, 63, 7, 44, 8, 47, 22,
          73, 62, 66, 100, 86, 50, 81, 6, 39, 81, 28, 46, 75, 70, 2, 31, 54, 41, 91, 1, 51, 58, 3, 97, 
          50, 70, 87, 39, 43, 9, 5, 51, 100, 72, 42, 67, 98, 4, 40, 53, 1, 58, 69, 24, 96, 34, 20, 24, 56,
            98, 92, 2, 50, 49, 20, 22, 70, 53, 71, 31, 2, 56, 42, 51, 82, 3, 85, 78, 51, 42, 70, 62, 4, 74, 36,
              65, 94, 64, 66, 2, 54, 25, 53, 41, 88, 85, 61, 53, 93, 61, 6, 60, 15, 33, 55, 93, 93, 25, 78, 79, 
              19, 82, 82, 63, 23, 88, 82, 88, 69, 35, 80, 93, 19, 89, 24, 5, 82, 30, 99, 68, 34, 16, 92, 16, 80, 
              46, 53, 22, 39, 52, 8, 27, 36, 82, 50, 69, 39, 78, 70, 68, 1, 26, 40, 6, 1, 75, 48, 66, 51, 61, 80,
              50, 31, 90, 78, 93, 67, 76, 57, 26, 7, 94, 40, 9, 63, 28, 20, 71, 60, 75, 62, 63, 70, 36, 61, 77,
              63, 24, 25, 43, 26, 49, 80, 80, 31, 28, 37, 4, 75, 2, 73, 90, 33, 98, 97, 23, 82, 90, 42, 37, 58,
                    87, 8, 51, 62, 45, 23, 44, 55, 95, 71, 56, 44, 37, 15, 28, 98, 93, 21, 50, 16, 48, 30, 30, 94,
                      46, 100, 48, 58, 51, 9, 85, 22, 48, 50, 74, 98, 26, 86, 64, 66, 32, 39, 83, 94, 47, 90, 42, 
                      5, 45, 19, 62, 72, 84, 44, 93, 24, 93, 12, 26, 60, 71, 27, 14, 84, 17, 37, 58, 30, 95, 94, 85,
                        1, 13, 5, 12, 13, 8, 32, 84, 53, 86, 97, 62, 79, 78, 93, 72, 23, 25, 98, 64, 87, 49, 90, 80,
                          16, 39, 89, 63, 47, 70, 52, 52, 46, 90, 74, 24, 23, 30, 39, 49, 61, 77, 4, 75, 86, 92, 30, 
                          96, 27, 48, 95, 39, 56, 14, 97, 63, 27, 41, 92, 31, 26, 39, 20, 25, 27, 52, 68, 90, 7, 44, 
                          63, 67, 6, 33, 59, 22, 39, 73, 95, 21, 96, 70, 93, 5, 91, 41, 12, 63, 74, 58, 35, 29, 74, 
                          21, 45, 63, 66, 73, 98, 9, 19, 86, 31, 6, 52, 18, 20, 69, 29, 24, 92, 16, 79, 93, 92, 100,
                            3, 18, 58, 22, 1, 60, 13, 58, 19, 35, 19, 13, 20, 96, 15, 8, 95, 9, 8, 39, 33, 20, 78, 
                            14, 92, 96, 54, 24, 92, 31, 31, 42, 15, 35, 89, 68, 25, 62, 36, 13, 70, 98, 81, 92, 7, 
                            88, 89, 32, 66, 53, 21, 95, 54, 81, 62, 96, 90, 77, 57, 99, 27, 78, 87, 33, 18, 90, 20,
                              71, 29, 71, 24, 8, 58, 81, 22, 39, 52, 28, 12, 61, 22, 6, 64, 73, 27, 79, 35, 29, 7, 
                              84, 44, 96, 44, 24, 26, 92, 72, 24, 51, 37, 59, 92, 26, 75, 98, 10, 25, 64, 65, 12, 
                              28, 56, 77, 15, 57, 28, 19, 12, 36, 2, 2, 24, 86, 93, 14, 64, 99, 8, 100, 82, 90, 66,
                                99, 76, 91, 23, 12, 70, 39, 6, 14, 23, 82, 30, 13, 70, 2, 2, 98, 20, 1, 55, 82, 15,
                                  38, 89, 43, 59, 71, 43, 67, 64, 42, 70, 93, 17, 81, 40, 99, 78, 83, 1, 84, 74, 87,
                                    95, 35, 94, 82, 97, 18, 3, 56, 65, 61, 38, 1, 5, 34, 16, 8, 26, 27, 26, 30, 40, 
                                    33, 98, 77, 69, 74, 5, 42, 48, 25, 95, 16, 73, 95, 35, 66, 67, 48, 13, 98, 1, 75,
                                      99, 99, 56, 68, 86, 15, 9, 93, 90, 91, 80, 40, 92, 69, 1, 2, 95, 64, 45, 89, 79, 
                                      96, 51, 41, 97, 35, 61, 59, 24, 71, 31, 88, 40, 31, 97, 61, 67, 84, 7, 93, 7, 25,
                                        40, 64, 16, 29, 69, 7, 51, 62, 2, 28, 13, 77, 1, 47, 31, 27, 78, 91, 53, 88, 75,
                                          90, 16, 31, 7, 71, 13, 85, 67, 15, 69, 35, 42, 29, 1, 17, 55, 26, 79, 81, 21, 
                                          81, 60, 7, 1, 84, 82, 22, 67, 45, 34, 100, 46, 31, 9, 17, 58, 24, 16, 79, 88, 
                                          81, 58, 46, 82, 69, 28, 88, 1, 71, 56, 50, 93, 52, 58, 94, 55, 83, 99, 45, 81, 
                                          28, 19, 64, 54, 9, 99, 91, 86, 88, 51, 40, 75, 74, 70, 25, 9, 51, 92, 31, 61, 
                                          40, 13, 4, 55, 30, 75, 64, 31, 84, 80, 71, 23, 96, 81, 14, 5, 3, 17, 40, 71, 
                                          73, 86, 61, 24, 13, 84, 78, 7, 69, 98, 49, 66, 99, 100, 21, 97, 96, 32, 58, 
                                          56, 18, 7, 8, 16, 77, 62, 76, 25, 79, 19, 3, 93, 24, 46, 34, 48, 57, 84, 31, 
                                          83, 97, 35, 24, 38, 83, 100, 44, 5, 86, 67, 23, 62, 75, 51, 51, 79, 97, 53, 
                                          51, 54, 13, 99, 20, 85, 46, 10, 95, 19, 19, 83, 61, 7, 5, 51, 47, 42, 4, 31,
                                            29, 83, 37, 67, 24, 9, 85, 14, 60, 63, 90, 93, 98, 50, 38, 51, 14, 45, 13,
                                              24, 18, 53, 58, 69, 11, 89, 57, 42, 59, 45, 4, 3, 67, 32, 94, 16, 71, 86,
                                                13, 45, 50, 79, 12, 55, 16, 54, 34, 16, 98, 23, 17, 65, 76, 100, 28, 56,
                                                  67, 36, 36, 71, 96, 68, 86, 61, 83, 38, 87, 35, 43, 95, 33, 6, 57, 78, 
                                                  79, 11, 67, 50, 29, 89, 30, 60, 45, 14, 53, 33, 99, 97, 25, 15, 14, 50,
                                                    3, 94, 15, 1, 76, 30, 46, 88, 80, 25, 21, 58, 30, 93, 83, 85, 70, 34, 
                                                    70, 29, 47, 75, 55, 25, 53, 22, 94, 8, 75, 34, 56, 95, 43, 8, 94, 17, 
                                                    64, 33, 57, 66, 83, 88, 25, 81, 1, 15, 40, 77, 23, 68, 25, 82, 98, 25, 98,
                                                      9, 92, 21, 14, 58, 61, 52, 11, 46, 49, 95, 70, 68, 74, 30, 3, 51, 38, 2, 
                                                      42, 70, 62, 15, 57, 64, 61, 49, 79, 71, 24, 5, 67, 10, 15, 98, 66, 50, 84,
                                                        90, 68, 15, 8, 76, 30, 68, 83, 64, 40, 52, 87, 59, 13, 2, 11, 56, 44, 54, 
                                                        49, 85, 79, 65, 79, 34, 28, 46, 78, 95, 24, 20, 71, 84, 93, 88, 36, 16, 71,
                                                          30, 74, 40, 36, 64, 76, 5, 77, 80, 61, 73, 84, 17, 88, 31, 3, 34, 55, 6, 
                                                          22, 58, 28, 66, 30, 3, 12, 58, 62, 44, 9, 40, 84, 81, 29, 35, 83, 64, 93, 
                                                          48, 36, 35, 15, 95, 72, 24, 9, 76, 23, 14, 1, 23, 61, 31, 4, 49, 70, 6, 17, 
                                                          31, 67, 93, 13, 15, 88, 16, 31, 90, 50, 87, 18, 96, 45, 41, 64, 27, 61, 3, 35,
                                                            25, 94, 50, 47, 90, 59, 39, 78, 75, 58, 48, 89, 13, 8, 50, 40, 16, 86, 36, 78,
                                                              86, 90, 52, 41, 44, 57, 3, 29, 4, 45, 46, 81, 77, 95, 98, 37, 7, 36, 42, 45,
                                                                20, 4, 31, 72, 12, 47, 57, 20, 41, 37, 69, 53, 47, 9, 28, 58, 65, 21, 30, 
                                                                61, 86, 52, 93, 57, 41, 33, 15, 7, 37, 67, 84, 71, 16, 74, 94, 16, 73, 96,
                                                                  66, 42, 9, 43, 54, 42, 93, 69, 83, 60, 97, 64, 78, 50, 42, 30, 6, 27, 68,
                                                                  95, 78, 10, 87, 89, 7, 53, 80, 38, 75, 47, 5, 85, 53, 57, 43, 56, 55, 32, 
                                                                  4, 81, 56, 33, 58, 70, 78, 49, 29, 68, 11, 22, 13, 57, 45, 64, 100, 99, 38, 
                                                                  71, 18, 8, 46, 86, 86, 21, 3, 32, 83, 12, 63, 88, 32, 100, 78, 63, 97, 17, 
                                                                  48, 47, 79, 97, 64, 5, 26, 20, 71, 14, 83, 85, 26, 70, 60, 94, 50, 76, 79, 
                                                                  59, 24, 13, 94, 65, 1, 70, 11, 44, 7, 57, 91, 40, 64, 94, 69, 76, 41, 42, 
                                                                  76, 15, 19, 9, 16, 27, 91, 40, 5, 74, 88, 27, 31, 69, 22, 94, 80, 91, 1, 64,
                                                                    85, 79, 48, 9, 87, 49, 3, 34, 74, 44, 4, 63, 89, 21, 76, 29, 55, 63, 97, 99,
                                                                      99, 39, 40, 16, 56, 47, 92, 49, 70, 18, 62, 98, 51, 25, 83, 49, 93, 70, 48]


start = t.time()
selection_sort(array)
end = t.time()
print('Python runtime = ', (end-start),' seconds')

with open('solved.txt', 'w') as file:
    file.write(str(array))
