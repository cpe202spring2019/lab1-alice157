def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   if not int_list:
      return None

   max = int_list[0]
   for n in int_list[1:]:
      if n > max:
         max = n
   return max

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   if not int_list:
      return []

   return reverse_rec(int_list[1:]) + [int_list[0]]

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   midpoint = (low + high) // 2
   if int_list is None:
      raise ValueError

   if int_list[midpoint] == target:
      return midpoint
   # If the search comes down to 2 elements, check the upper one too.
   elif high - low == 1 and int_list[high] == target:
      return high

   if (low + 1) >= high:
      return None

   if int_list[midpoint] < target:
      return bin_search(target, midpoint, high, int_list)
   else:
      return bin_search(target, low, midpoint, int_list)
