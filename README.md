# schedule-conflicts

THis program is written in python because I find python to be quite easy and straightforward to 
handle and parse strings.  Because the input is formatted, the design is very simple:
1. Open the file
2. Parse each line for the time numbers
3. Convert the number strings to values
4. Save the number strings for possible printing
5. Compare the times

After [opening the file](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L62),
I [parsed it line by line](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L67),
[cut out the -s](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L69),
and 
[pulled out the hour and minute values](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L75).
I created a 
[list of dictionaries](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L75) 
because I find handlng lists to be easy and I thought a dictionary would be the best way to store the data. I also
saved the
[times as strings in a dictionary](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L78)
to make printing easier later.  I ended up doing this after I wrote the code for the comparisons realizing I needed
to do this printing.

I started by trying to compare the hours and then the minutes, but the logic was very very confusing,
so after a few minutes of thought. I decided to 
[convert the times into floating point values](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L21).
This made the 
[comparison quite simple](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L36).
I used local variables to make the coding easier to read, After I figured out how to compare the values, 
I decided to (learn how to in python) 
[create a recursive function](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L44) 
to deal with the comparisons. I've done this is Fortran, but never in python, so I was familiar with the
concept, just not the syntax in python.  It was very easy though.  The function gets an index for the list, and then
[iterates through the rest of the list through all of the times with a higher index than its 
own](https://github.com/byrdman1982/schedule-conflicts/blob/main/schedule_conflict.py#L24)
This prevents duplication of effort.  After `times_list[len(times_list)-1]` is done and `times_list[len(times_list)-2]` 
is being evaluated, it will not compare to `time_list[len(times_list[0]]` again.  I decided to start at the end because 
starting a `0` always throws me off because I am most comfortable with Fortran, <rant> and if you ask someone to count to 10,
they do not start with 0, they start with 1.</rant>

I also saved the conflicts, as this "will be used operationally", but it was never discussed how it would be used.  If it is
going to be part of a large program, the conflicts are recorded for the future use.  

I made a typo in the if statement that compares the times, and I thought I would have to go 
through the list a second time in the opposite direction, then I had to check for duplicates. The code 
was a giant mess until I realized there was a typo.  The I deleted the mess and it worked.
