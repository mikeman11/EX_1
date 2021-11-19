from numpy import size
import building
import csv
from  call import calls
from building import elvator_list



def travaltime(elvator_list, calls,x,i):
    cycle_time = elvator_list[x]._stopTime + elvator_list[x]._openTime + elvator_list[x]._startTime + elvator_list[x]._stopTime
    traval_to_src = abs(int(elvator_list[x].Pos) - int(calls[i].src))
    traval_to_dst = abs(int(calls[i].src) - int(calls[i].dst))
    traval_to_0 = abs(int(calls[i].dst))
    total_traval = ((traval_to_src +  traval_to_dst + traval_to_0 ) / elvator_list[x]._speed ) + cycle_time
    return total_traval

def csvwriter(time, i, calls , elvator_list ,x):
    with open('out.csv', "a", newline='') as o:
      thewriter = csv.writer(o)
      thewriter.writerow(["Elevator call" , calls[i].src ,calls[i].dst, "3", elvator_list[x]._id, "Done", "dt" ,elvator_list[x].coolDown] )





def supuer_algo(time, i, calls , elvator_list):
   if (size(elvator_list) > 1):
       for x in range(len(elvator_list)):


           if (elvator_list[x].onJob == 0):
               total_traval = travaltime(elvator_list,calls,x,i)
               elvator_list[x].onJob = 1
               elvator_list[x].pos = 0
               #elvator_list[x].pos = calls[i].dst
               elvator_list[x].coolDown = total_traval
               csvwriter(time, i, calls , elvator_list,x)







#travaltime(elvator_list,calls)
#csvwriter(time, i, calls , elvator_list )