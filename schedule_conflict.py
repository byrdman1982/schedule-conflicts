#!/usr/bin/python3
## \author Tom Robinson
## \description This python program will evaluate a schedule in the following format
## \verbatim
## hh:mm - hh:mm
## \endverbatim
## and search for conflicts in the schedule

## A recursive function the will figure out if conflicts occur
## This function descends the list
def find_conflicts(times_list,times_string,conflicts_list,i):
#  Save the i value, but give j the value of i to start
  j = i
#Set up the base time
  hs1 = times_list[i]['h1']
  ms1 = times_list[i]['m1']
  he1 = times_list[i]['h2']
  me1 = times_list[i]['m2']

#convert to floats for comparisons
  fs1=float(hs1+(ms1/60.))
  fe1=float(he1+(me1/60.))

  while j < len(times_list)-1:
    j=j+1
#Set up the time to compare
    hs2 = times_list[j]['h1']
    ms2 = times_list[j]['m1']
    he2 = times_list[j]['h2']
    me2 = times_list[j]['m2']
# Convert to floats for comparisons
    fs2=float(hs2+(ms2/60.))
    fe2=float(he2+(me2/60.))
# Compare to see if there is a conflict
#    print (fe1,fs2,fe1>fs2,fs1,
    if (fe1 > fs2 and fs1 < fe2):
      conflicts_list.append("conflict: "+times_string[i]['t1']+"-"+times_string[i]['t2']+" with "+times_string[j]['t1']+"-"+times_string[j]['t2'])
      print ("conflict: "+times_string[i]['t1']+"-"+times_string[i]['t2']+" with "+times_string[j]['t1']+"-"+times_string[j]['t2'])
## Either recall the function or end the recursion
  if i == 0:
## At the end of the iteration return 0
    return i 
  else:
    return find_conflicts(times_list,times_string,conflicts_list,i-1)

## A function that checks for duplicates
def dups(c,i):
  j = i
  print_flag = 0
# Loop through the part of the list that is before this element
  while j < len(c)-1:
    j = j+1
    if c[i] == c[j]:
      # Switch the flag to not print
      print_flag = 1 
  return print_flag
 
#
###############################################################################################
#
## Open the file 
file_obj = open("schedule.txt","r")
## Parse out the times and store them in an array of dictionaries
times_list=[]
times_string=[]
ntimes = 0
for line in file_obj:
 #split on the -
   times = line.split("-")
 #save the times
   t1_string = times[0]
   t2_string = times[1]
 #create a dictionary the beginning hour h1, beginning minutes m1, ending hour h2 and ending minutes h2
 # \note Strings are converted to integers here
   tdict = {"h1":int(t1_string.split(":")[0].strip()) , "m1":int(t1_string.split(":")[1].strip()) , "h2":int(t2_string.split(":")[0].strip()) , "m2":int(t2_string.split(":")[1].strip())}
   times_list.append(tdict)
   ts={"t1":t1_string.strip(), "t2":t2_string.strip()}
   times_string.append(ts)
   ntimes = ntimes + 1
##
conflicts_list=[]
## Check for conflicts
i=(find_conflicts(times_list,times_string,conflicts_list,len(times_list)-1))
## Check for duplicates and print
k=0
while k < len(conflicts_list):
  if dups(conflicts_list,k) == 0:
    print(conflicts_list[k])
  k=k+1

quit()







