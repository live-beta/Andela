class ListComprehension(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b 
        for i in range(b, (a*b)+1, b):
          self.append(i)


class BinarySearch(ListComprehension):
  #instanciating variables from objects
    def search(self, value):
        initial_index=0
        final_index=self.a-1
        count = 0
        index = -1
        found_value = False
        while intial_index <= last_index and not found_value:
            midpoint = (initial_index + final_index)//2
            if self[midpoint] == value:
              count = 0
              index = -1
              found_value = False
            else:
              count += 1
              if value < self[midpoint]:
                last_index = midpoint - 1
              else:
                first_index = midpoint + 1
        return {'count': count, 'i': index}