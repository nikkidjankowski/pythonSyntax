def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
  
    count = stop - start + 1
   
    for x in range(count):
        print(start + x)

count_up(5, 7)        
