#Functional Prompt

# Implement a function that will flatten and sort an array of integers in ascending order, and which adhere to a functional programming paradigm.

array = [[3, 5], [7, 3, 9], [1, 12]]

def flatten_and_sort(array):
	arr = []
	for item in array:
		for i in item:
			arr.append(i)

	return sorted(arr)

print(flatten_and_sort(array))

# Make sure to answer the following questions about your coding process:

# How does this solution ensure data immutability?
#Answer: Functional programming use immutable data  means that variables can't change their value once you have defined them, and the only way to create additional values is by defining new variables.So, this example not seen any add additional values that refers to ensure data immutability.

# Is this solution a pure function? Why or why not?
#Answer: Yes, this soultion is pure function, because it does not contain any side effects because it does not alter the array item.

# Is this solution a higher order function? Why or why not?
#Answer: Yes, this solution is higher order function, because it accepts one function as an argument and returns a function.

# Would it have been easier to solve this problem using a different programming style?
list = [8, 4, 14, 9, 12, 5, 7, 1, 10, 2, 3]
list.sort()  # Sorting the list declaratively using the sorting algorithm provided by the Python langauge
print(list)

# Why in particular is functional programming a helpful paradigm when solving this problem?
# Answer: Functional programming is a programming paradigm in which we try to bind everything in pure mathematical functions style. It is a declarative type of programming style.Its main focus is on "what to solve" in contrast to an imperative style where the main focus is "how to solve".

