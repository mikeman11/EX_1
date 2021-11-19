from numpy import size

import call
import building
import call
from  call import calls
from Superalgo import supuer_algo
from building import elvator_list

import sys

if __name__ == '__main__':
   #buildingFile = sys.argv[1]
   #callsFile = sys.argv[2]
   #print(buildingFile + " , " + callsFile)


   time = 1
   i = 0
   num_of_calls = size(calls)

   while(time < int(float(calls[num_of_calls-1].time))):


      if (time >= int(float(calls[i].time)) ):
         supuer_algo(time, i, calls , elvator_list)
         for x in range(len(elvator_list)):
            elvator_list[x].coolDown = elvator_list[x].coolDown - 1

         i=i+1
         time = time  + 1


      else:
         time = time + 1







