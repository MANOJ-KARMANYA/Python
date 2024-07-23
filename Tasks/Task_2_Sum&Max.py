def sum_function(nums):
    total_sum = 0
    for num in nums:
        total_sum += num
    return total_sum

def max_function(nums):
    if not nums:
        return None  # Handle case where list is empty
    
    max_value = nums[0]
    for num in nums[1:]:
        if num > max_value:
            max_value = num
    return max_value

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Calling sum function")
    print(sum_function(numbers))
    
    print("Calling max function")
    print(max_function(numbers))

if __name__ == "__main__":
    main()
