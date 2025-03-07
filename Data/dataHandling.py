import re
import csv


# The raw data (replace `raw_data` with the actual string you provided)
raw_data = """
Data
Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
1:0    0.00    0.00    0.00
1:1    0.00    0.00    0.00
1:2    0.00    0.00    0.00
1:3    0.00    0.00    0.00
1:4    0.00    0.00    0.00
1:5    0.00    0.00    0.00
1:6    0.00    0.00    0.00
I'm just a chill guy looking around
Hunger level: 1
Tendency to lay eggs: 1


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
2:0    0.00    0.00    0.00
2:1    0.00    0.00    0.00
2:2    0.00    0.00    0.00
2:3    0.00    0.00    0.00
2:4    0.00    0.00    0.00
2:5    0.00    0.00    0.00
2:6    0.00    0.00    0.00
I'm just a chill guy looking around
Hunger level: 2
Tendency to lay eggs: 2


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
3:0    0.00    0.00    0.00
3:1    0.00    0.00    0.00
3:2    0.00    0.00    0.00
3:3    0.00    0.00    0.00
3:4    0.00    0.00    0.00
3:5    0.00    0.00    0.00
3:6    0.00    0.00    0.00
I'm just a chill guy looking around
Hunger level: 3
Tendency to lay eggs: 3


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
4:0    0.00    0.00    0.00
4:1    0.00    0.00    0.00
4:2    0.00    0.00    0.00
4:3    0.00    0.00    0.00
4:4    0.00    0.00    0.00
4:5    0.00    0.00    0.00
4:6    0.00    0.00    0.00
I'm just a chill guy looking around
Hunger level: 4
Tendency to lay eggs: 4

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
5:0    0.00    0.00    0.00
5:1    0.00    0.00    0.00
5:2    0.00    0.00    0.00
5:3    0.00    0.00    0.00
5:4    0.00    0.00    0.00
5:5    0.00    0.00    0.00
5:6    0.00    0.00    0.00
I'm just a chill guy looking around
Hunger level: 5
Tendency to lay eggs: 5

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
6:0    0.00    0.00    5.00
6:1    0.00    0.00    0.00
6:2    0.00    0.00    0.00
6:3    0.00    0.00    0.00
6:4    0.00    0.00    0.00
6:5    0.00    0.00    0.00
6:6    0.00    0.00    0.00
I'm just a chill guy looking around
Ready to lay eggs!
Hunger level: 6
Tendency to lay eggs: 6

Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
7:0    0.00    0.00    5.00
7:1    0.00    0.00    0.00
7:2    0.00    0.00    0.00
7:3    0.00    0.00    0.00
7:4    0.00    0.00    0.00
7:5    0.00    -5.00    0.00
7:6    0.00    0.00    0.00
I'm just a chill guy looking around
Hunger level: 7
Tendency to lay eggs: 7

Reward:  -10 , Next State:  6
TState Q(left) Q(right) Q(forward)
8:0    0.00    0.00    5.00
8:1    0.00    0.00    0.00
8:2    0.00    0.00    0.00
8:3    0.00    -5.00    0.00
8:4    0.00    0.00    0.00
8:5    0.00    -5.00    0.00
8:6    0.00    0.00    0.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 8
Tendency to lay eggs: 8

Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
9:0    0.00    0.00    5.00
9:1    0.00    0.00    0.00
9:2    0.00    0.00    0.00
9:3    0.00    -5.00    0.00
9:4    0.00    0.00    0.00
9:5    0.00    -5.00    0.00
9:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 9
Tendency to lay eggs: 9

Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
10:0    0.00    0.00    5.00
10:1    0.00    0.00    0.00
10:2    0.00    0.00    0.00
10:3    0.00    -5.00    5.00
10:4    0.00    0.00    0.00
10:5    0.00    -5.00    0.00
10:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 10
Tendency to lay eggs: 10

Reward:  20 , Next State:  1
TState Q(left) Q(right) Q(forward)
11:0    0.00    0.00    5.00
11:1    0.00    0.00    0.00
11:2    0.00    0.00    10.00
11:3    0.00    -5.00    5.00
11:4    0.00    0.00    0.00
11:5    0.00    -5.00    0.00
11:6    0.00    0.00    -5.00
I am eating
Hunger level: 0
Tendency to lay eggs: 10

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
12:0    0.00    0.00    5.00
12:1    0.00    0.00    2.47
12:2    0.00    0.00    10.00
12:3    0.00    -5.00    5.00
12:4    0.00    0.00    0.00
12:5    0.00    -5.00    0.00
12:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 1
Tendency to lay eggs: 11

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
13:0    0.00    0.00    7.50
13:1    0.00    0.00    2.47
13:2    0.00    0.00    10.00
13:3    0.00    -5.00    5.00
13:4    0.00    0.00    0.00
13:5    0.00    -5.00    0.00
13:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 2
Tendency to lay eggs: 12

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
14:0    0.00    0.00    7.50
14:1    0.00    0.00    2.47
14:2    0.00    0.00    10.00
14:3    0.00    -5.00    5.00
14:4    0.00    0.00    0.00
14:5    0.00    -5.00    5.00
14:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 3
Tendency to lay eggs: 13

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
15:0    0.00    0.00    7.50
15:1    0.00    0.00    2.47
15:2    0.00    0.00    10.00
15:3    0.00    -5.00    5.00
15:4    0.00    0.00    0.00
15:5    0.00    -5.00    9.98
15:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 4
Tendency to lay eggs: 14

Reward:  20 , Next State:  4
TState Q(left) Q(right) Q(forward)
16:0    0.00    0.00    7.50
16:1    0.00    0.00    2.47
16:2    0.00    0.00    10.00
16:3    0.00    -5.00    5.00
16:4    0.00    0.00    0.00
16:5    0.00    -5.00    14.99
16:6    0.00    0.00    -5.00
I am laying eggs
Hunger level: 4
Tendency to lay eggs: 0


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
17:0    0.00    0.00    7.50
17:1    0.00    0.00    2.47
17:2    0.00    0.00    10.00
17:3    0.00    -5.00    5.00
17:4    0.00    3.71    0.00
17:5    0.00    -5.00    14.99
17:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 5
Tendency to lay eggs: 1

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
18:0    0.00    0.00    7.46
18:1    0.00    0.00    2.47
18:2    0.00    0.00    10.00
18:3    0.00    -5.00    5.00
18:4    0.00    3.71    0.00
18:5    0.00    -5.00    14.99
18:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 6
Tendency to lay eggs: 2

Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
19:0    0.00    0.00    1.21
19:1    0.00    0.00    2.47
19:2    0.00    0.00    10.00
19:3    0.00    -5.00    5.00
19:4    0.00    3.71    0.00
19:5    0.00    -5.00    14.99
19:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 7
Tendency to lay eggs: 3

Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
20:0    0.00    0.00    1.21
20:1    0.00    0.00    2.47
20:2    0.00    0.00    10.00
20:3    0.00    -5.00    -0.03
20:4    0.00    3.71    0.00
20:5    0.00    -5.00    14.99
20:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 8
Tendency to lay eggs: 4



Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
21:0    0.00    0.00    1.21
21:1    0.00    0.00    2.47
21:2    0.00    0.00    10.00
21:3    0.00    -5.00    -5.01
21:4    0.00    3.71    0.00
21:5    0.00    -5.00    14.99
21:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 9
Tendency to lay eggs: 5

Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
22:0    0.00    0.00    1.21
22:1    0.00    0.00    2.47
22:2    0.00    0.00    10.00
22:3    0.00    -5.00    7.44
22:4    0.00    3.71    0.00
22:5    0.00    -5.00    14.99
22:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 10
Tendency to lay eggs: 6

Reward:  20 , Next State:  1
TState Q(left) Q(right) Q(forward)
23:0    0.00    0.00    1.21
23:1    0.00    0.00    2.47
23:2    0.00    0.00    16.23
23:3    0.00    -5.00    7.44
23:4    0.00    3.71    0.00
23:5    0.00    -5.00    14.99
23:6    0.00    0.00    -5.00
I am eating
Hunger level: 0
Tendency to lay eggs: 6

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
24:0    0.00    0.00    1.21
24:1    0.60    0.00    2.47
24:2    0.00    0.00    16.23
24:3    0.00    -5.00    7.44
24:4    0.00    3.71    0.00
24:5    0.00    -5.00    14.99
24:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 1
Tendency to lay eggs: 7

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
25:0    0.00    0.00    13.02
25:1    0.60    0.00    2.47
25:2    0.00    0.00    16.23
25:3    0.00    -5.00    7.44
25:4    0.00    3.71    0.00
25:5    0.00    -5.00    14.99
25:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 2
Tendency to lay eggs: 8

Reward:  20 , Next State:  4
TState Q(left) Q(right) Q(forward)
26:0    0.00    0.00    13.02
26:1    0.60    0.00    2.47
26:2    0.00    0.00    16.23
26:3    0.00    -5.00    7.44
26:4    0.00    3.71    0.00
26:5    0.00    -5.00    19.33
26:6    0.00    0.00    -5.00
I am laying eggs
Hunger level: 2
Tendency to lay eggs: 0

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
27:0    0.00    0.00    13.02
27:1    0.60    0.00    2.47
27:2    0.00    0.00    16.23
27:3    0.00    -5.00    7.44
27:4    6.45    3.71    0.00
27:5    0.00    -5.00    19.33
27:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 3
Tendency to lay eggs: 1

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
28:0    0.00    0.00    12.96
28:1    0.60    0.00    2.47
28:2    0.00    0.00    16.23
28:3    0.00    -5.00    7.44
28:4    6.45    3.71    0.00
28:5    0.00    -5.00    19.33
28:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 4
Tendency to lay eggs: 2

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
29:0    0.00    0.00    12.89
29:1    0.60    0.00    2.47
29:2    0.00    0.00    16.23
29:3    0.00    -5.00    7.44
29:4    6.45    3.71    0.00
29:5    0.00    -5.00    19.33
29:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 5
Tendency to lay eggs: 3

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
30:0    0.00    6.38    12.89
30:1    0.60    0.00    2.47
30:2    0.00    0.00    16.23
30:3    0.00    -5.00    7.44
30:4    6.45    3.71    0.00
30:5    0.00    -5.00    19.33
30:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 6
Tendency to lay eggs: 4

Reward:  20 , Next State:  1
TState Q(left) Q(right) Q(forward)
31:0    0.00    6.38    17.67
31:1    0.60    0.00    2.47
31:2    0.00    0.00    16.23
31:3    0.00    -5.00    7.44
31:4    6.45    3.71    0.00
31:5    0.00    -5.00    19.33
31:6    0.00    0.00    -5.00
I am eating
Hunger level: 0
Tendency to lay eggs: 4

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
32:0    0.00    6.38    17.67
32:1    0.60    0.00    9.98
32:2    0.00    0.00    16.23
32:3    0.00    -5.00    7.44
32:4    6.45    3.71    0.00
32:5    0.00    -5.00    19.33
32:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 1
Tendency to lay eggs: 5

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
33:0    0.00    6.38    17.58
33:1    0.60    0.00    9.98
33:2    0.00    0.00    16.23
33:3    0.00    -5.00    7.44
33:4    6.45    3.71    0.00
33:5    0.00    -5.00    19.33
33:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 2
Tendency to lay eggs: 6

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
34:0    0.00    6.38    17.49
34:1    0.60    0.00    9.98
34:2    0.00    0.00    16.23
34:3    0.00    -5.00    7.44
34:4    6.45    3.71    0.00
34:5    0.00    -5.00    19.33
34:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 3
Tendency to lay eggs: 7

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
35:0    0.00    6.38    17.41
35:1    0.60    0.00    9.98
35:2    0.00    0.00    16.23
35:3    0.00    -5.00    7.44
35:4    6.45    3.71    0.00
35:5    0.00    -5.00    19.33
35:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 4
Tendency to lay eggs: 8

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
36:0    0.00    6.38    17.32
36:1    0.60    0.00    9.98
36:2    0.00    0.00    16.23
36:3    0.00    -5.00    7.44
36:4    6.45    3.71    0.00
36:5    0.00    -5.00    19.33
36:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 5
Tendency to lay eggs: 9

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
37:0    0.00    6.38    17.23
37:1    0.60    0.00    9.98
37:2    0.00    0.00    16.23
37:3    0.00    -5.00    7.44
37:4    6.45    3.71    0.00
37:5    0.00    -5.00    19.33
37:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 6
Tendency to lay eggs: 10

Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
38:0    0.00    6.38    21.65
38:1    0.60    0.00    9.98
38:2    0.00    0.00    16.23
38:3    0.00    -5.00    7.44
38:4    6.45    3.71    0.00
38:5    0.00    -5.00    19.33
38:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Hunger level: 7
Tendency to lay eggs: 11

Reward:  -10 , Next State:  6
TState Q(left) Q(right) Q(forward)
39:0    0.00    6.38    21.65
39:1    0.60    0.00    9.98
39:2    -5.00    0.00    16.23
39:3    0.00    -5.00    7.44
39:4    6.45    3.71    0.00
39:5    0.00    -5.00    19.33
39:6    0.00    0.00    -5.00
I'm just a chill guy looking around
Ready to lay eggs!
Hunger level: 8
Tendency to lay eggs: 12

Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
40:0    0.00    6.38    21.65
40:1    0.60    0.00    9.98
40:2    -5.00    0.00    16.23
40:3    0.00    -5.00    7.44
40:4    6.45    3.71    0.00
40:5    0.00    -5.00    19.33
40:6    0.00    -1.32    -5.00
I'm just a chill guy looking around
Ready to lay eggs!
Hunger level: 9
Tendency to lay eggs: 13

Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
41:0    0.00    6.38    21.65
41:1    0.60    0.00    9.98
41:2    -5.00    0.00    16.23
41:3    0.00    -5.00    2.41
41:4    6.45    3.71    0.00
41:5    0.00    -5.00    19.33
41:6    0.00    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 10
Tendency to lay eggs: 14

Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
42:0    0.00    6.38    21.65
42:1    0.60    0.00    9.98
42:2    -5.00    0.00    16.23
42:3    0.00    -5.00    -2.61
42:4    6.45    3.71    0.00
42:5    0.00    -5.00    19.33
42:6    0.00    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 11
Tendency to lay eggs: 15

Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
43:0    0.00    6.38    21.65
43:1    0.60    0.00    9.98
43:2    -5.00    0.00    16.23
43:3    -5.00    -5.00    -2.61
43:4    6.45    3.71    0.00
43:5    0.00    -5.00    19.33
43:6    0.00    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 12
Tendency to lay eggs: 16

Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
44:0    0.00    6.38    21.65
44:1    0.60    0.00    9.98
44:2    -5.00    0.00    16.23
44:3    -5.00    -5.00    11.73
44:4    6.45    3.71    0.00
44:5    0.00    -5.00    19.33
44:6    0.00    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 13
Tendency to lay eggs: 17

Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
45:0    0.00    6.38    21.65
45:1    0.60    0.00    9.98
45:2    -5.00    0.00    21.14
45:3    -5.00    -5.00    11.73
45:4    6.45    3.71    0.00
45:5    0.00    -5.00    19.33
45:6    0.00    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 14
Tendency to lay eggs: 18

Reward:  -10 , Next State:  6
TState Q(left) Q(right) Q(forward)
46:0    0.00    6.38    21.65
46:1    0.60    0.00    9.98
46:2    -5.00    0.00    5.57
46:3    -5.00    -5.00    11.73
46:4    6.45    3.71    0.00
46:5    0.00    -5.00    19.33
46:6    0.00    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 15
Tendency to lay eggs: 19

Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
47:0    0.00    6.38    21.65
47:1    0.60    0.00    9.98
47:2    -5.00    0.00    5.57
47:3    -5.00    -5.00    11.73
47:4    6.45    3.71    0.00
47:5    0.00    -5.00    19.33
47:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 16
Tendency to lay eggs: 20

Reward:  20 , Next State:  1
TState Q(left) Q(right) Q(forward)
48:0    0.00    6.38    21.65
48:1    0.60    0.00    9.98
48:2    -5.00    0.00    17.73
48:3    -5.00    -5.00    11.73
48:4    6.45    3.71    0.00
48:5    0.00    -5.00    19.33
48:6    7.76    -1.32    -5.00
I am eating
Hunger level: 0
Tendency to lay eggs: 20

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
49:0    0.00    6.38    21.65
49:1    0.60    0.00    15.71
49:2    -5.00    0.00    17.73
49:3    -5.00    -5.00    11.73
49:4    6.45    3.71    0.00
49:5    0.00    -5.00    19.33
49:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 1
Tendency to lay eggs: 21

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
50:0    0.00    6.38    21.54
50:1    0.60    0.00    15.71
50:2    -5.00    0.00    17.73
50:3    -5.00    -5.00    11.73
50:4    6.45    3.71    0.00
50:5    0.00    -5.00    19.33
50:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 2
Tendency to lay eggs: 22

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
51:0    0.00    6.38    21.43
51:1    0.60    0.00    15.71
51:2    -5.00    0.00    17.73
51:3    -5.00    -5.00    11.73
51:4    6.45    3.71    0.00
51:5    0.00    -5.00    19.33
51:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 3
Tendency to lay eggs: 23
Whoops! I'm going back to my habitat!

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
52:0    0.00    6.38    25.29
52:1    0.60    0.00    15.71
52:2    -5.00    0.00    17.73
52:3    -5.00    -5.00    11.73
52:4    6.45    3.71    0.00
52:5    0.00    -5.00    19.33
52:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 4
Tendency to lay eggs: 24

Reward:  20 , Next State:  4
TState Q(left) Q(right) Q(forward)
53:0    0.00    6.38    25.29
53:1    0.60    0.00    15.71
53:2    -5.00    0.00    17.73
53:3    -5.00    -5.00    11.73
53:4    6.45    3.71    0.00
53:5    0.00    -5.00    22.86
53:6    7.76    -1.32    -5.00
I am laying eggs
Hunger level: 4
Tendency to lay eggs: 0

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
54:0    0.00    6.38    25.29
54:1    0.60    0.00    15.71
54:2    -5.00    0.00    17.73
54:3    -5.00    -5.00    11.73
54:4    15.74    3.71    0.00
54:5    0.00    -5.00    22.86
54:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 5
Tendency to lay eggs: 1

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
55:0    0.00    6.38    25.16
55:1    0.60    0.00    15.71
55:2    -5.00    0.00    17.73
55:3    -5.00    -5.00    11.73
55:4    15.74    3.71    0.00
55:5    0.00    -5.00    22.86
55:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 6
Tendency to lay eggs: 2

Reward:  20 , Next State:  1
TState Q(left) Q(right) Q(forward)
56:0    0.00    6.38    30.36
56:1    0.60    0.00    15.71
56:2    -5.00    0.00    17.73
56:3    -5.00    -5.00    11.73
56:4    15.74    3.71    0.00
56:5    0.00    -5.00    22.86
56:6    7.76    -1.32    -5.00
I am eating
Hunger level: 0
Tendency to lay eggs: 2

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
57:0    0.00    6.38    30.36
57:1    0.60    0.00    22.88
57:2    -5.00    0.00    17.73
57:3    -5.00    -5.00    11.73
57:4    15.74    3.71    0.00
57:5    0.00    -5.00    22.86
57:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 1
Tendency to lay eggs: 3

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
58:0    0.00    6.38    30.20
58:1    0.60    0.00    22.88
58:2    -5.00    0.00    17.73
58:3    -5.00    -5.00    11.73
58:4    15.74    3.71    0.00
58:5    0.00    -5.00    22.86
58:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 2
Tendency to lay eggs: 4

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
59:0    0.00    6.38    31.42
59:1    0.60    0.00    22.88
59:2    -5.00    0.00    17.73
59:3    -5.00    -5.00    11.73
59:4    15.74    3.71    0.00
59:5    0.00    -5.00    22.86
59:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 3
Tendency to lay eggs: 5

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
60:0    0.00    6.38    31.42
60:1    0.60    0.00    22.88
60:2    -5.00    0.00    17.73
60:3    -5.00    -5.00    11.73
60:4    15.74    3.71    0.00
60:5    0.00    -5.00    27.74
60:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 4
Tendency to lay eggs: 6

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
61:0    0.00    6.38    31.42
61:1    0.60    0.00    22.88
61:2    -5.00    0.00    17.73
61:3    -5.00    -5.00    11.73
61:4    15.74    3.71    0.00
61:5    0.00    -5.00    32.60
61:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 5
Tendency to lay eggs: 7

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
62:0    0.00    6.38    31.42
62:1    0.60    0.00    22.88
62:2    -5.00    0.00    17.73
62:3    -5.00    -5.00    11.73
62:4    15.74    3.71    0.00
62:5    0.00    -5.00    31.85
62:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 6
Tendency to lay eggs: 8

Reward:  20 , Next State:  1
TState Q(left) Q(right) Q(forward)
63:0    0.00    6.38    37.03
63:1    0.60    0.00    22.88
63:2    -5.00    0.00    17.73
63:3    -5.00    -5.00    11.73
63:4    15.74    3.71    0.00
63:5    0.00    -5.00    31.85
63:6    7.76    -1.32    -5.00
I am eating
Hunger level: 0
Tendency to lay eggs: 8

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
64:0    0.00    6.38    37.03
64:1    0.60    0.00    29.77
64:2    -5.00    0.00    17.73
64:3    -5.00    -5.00    11.73
64:4    15.74    3.71    0.00
64:5    0.00    -5.00    31.85
64:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 1
Tendency to lay eggs: 9

Reward:  10 , Next State:  5
TState Q(left) Q(right) Q(forward)
65:0    0.00    6.38    39.28
65:1    0.60    0.00    29.77
65:2    -5.00    0.00    17.73
65:3    -5.00    -5.00    11.73
65:4    15.74    3.71    0.00
65:5    0.00    -5.00    31.85
65:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Ready to lay eggs!
Hunger level: 2
Tendency to lay eggs: 10

Reward:  20 , Next State:  4
TState Q(left) Q(right) Q(forward)
66:0    0.00    6.38    39.28
66:1    0.60    0.00    29.77
66:2    -5.00    0.00    17.73
66:3    -5.00    -5.00    11.73
66:4    15.74    3.71    0.00
66:5    0.00    -5.00    33.72
66:6    7.76    -1.32    -5.00
I am laying eggs
Hunger level: 2
Tendency to lay eggs: 0

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
67:0    0.00    6.38    39.28
67:1    0.60    0.00    29.77
67:2    -5.00    0.00    17.73
67:3    -5.00    -5.00    11.73
67:4    27.31    3.71    0.00
67:5    0.00    -5.00    33.72
67:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 3
Tendency to lay eggs: 1

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
68:0    0.00    6.38    39.09
68:1    0.60    0.00    29.77
68:2    -5.00    0.00    17.73
68:3    -5.00    -5.00    11.73
68:4    27.31    3.71    0.00
68:5    0.00    -5.00    33.72
68:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 4
Tendency to lay eggs: 2

Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
69:0    0.00    6.38    38.89
69:1    0.60    0.00    29.77
69:2    -5.00    0.00    17.73
69:3    -5.00    -5.00    11.73
69:4    27.31    3.71    0.00
69:5    0.00    -5.00    33.72
69:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 5
Tendency to lay eggs: 3


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
70:0    0.00    6.38    38.70
70:1    0.60    0.00    29.77
70:2    -5.00    0.00    17.73
70:3    -5.00    -5.00    11.73
70:4    27.31    3.71    0.00
70:5    0.00    -5.00    33.72
70:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 6
Tendency to lay eggs: 4


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
71:0    0.00    6.38    20.15
71:1    0.60    0.00    29.77
71:2    -5.00    0.00    17.73
71:3    -5.00    -5.00    11.73
71:4    27.31    3.71    0.00
71:5    0.00    -5.00    33.72
71:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 7
Tendency to lay eggs: 5


Reward:  -10 , Next State:  6
TState Q(left) Q(right) Q(forward)
72:0    0.00    6.38    20.15
72:1    0.60    0.00    29.77
72:2    -5.00    0.00    17.73
72:3    -5.00    -5.00    4.70
72:4    27.31    3.71    0.00
72:5    0.00    -5.00    33.72
72:6    7.76    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 8
Tendency to lay eggs: 6


Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
73:0    0.00    6.38    20.15
73:1    0.60    0.00    29.77
73:2    -5.00    0.00    17.73
73:3    -5.00    -5.00    4.70
73:4    27.31    3.71    0.00
73:5    0.00    -5.00    33.72
73:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 9
Tendency to lay eggs: 7


Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
74:0    0.00    6.38    20.15
74:1    0.60    0.00    29.77
74:2    -5.00    0.00    22.64
74:3    -5.00    -5.00    4.70
74:4    27.31    3.71    0.00
74:5    0.00    -5.00    33.72
74:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 10
Tendency to lay eggs: 8


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
75:0    0.00    6.38    20.15
75:1    0.60    0.00    29.77
75:2    -5.00    0.00    8.65
75:3    -5.00    -5.00    4.70
75:4    27.31    3.71    0.00
75:5    0.00    -5.00    33.72
75:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Ready to lay eggs!
Hunger level: 11
Tendency to lay eggs: 9


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
76:0    0.00    6.38    20.15
76:1    0.60    0.00    29.77
76:2    -5.00    0.00    8.65
76:3    -5.17    -5.00    4.70
76:4    27.31    3.71    0.00
76:5    0.00    -5.00    33.72
76:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 12
Tendency to lay eggs: 10


Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
77:0    0.00    6.38    20.15
77:1    0.60    0.00    29.77
77:2    -5.00    0.00    8.65
77:3    -5.17    -5.00    11.63
77:4    27.31    3.71    0.00
77:5    0.00    -5.00    33.72
77:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 13
Tendency to lay eggs: 11


Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
78:0    0.00    6.38    20.15
78:1    0.60    0.00    29.77
78:2    -5.00    0.00    13.61
78:3    -5.17    -5.00    11.63
78:4    27.31    3.71    0.00
78:5    0.00    -5.00    33.72
78:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 14
Tendency to lay eggs: 12


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
79:0    0.00    6.38    20.15
79:1    0.60    0.00    29.77
79:2    -5.00    0.00    7.56
79:3    -5.17    -5.00    11.63
79:4    27.31    3.71    0.00
79:5    0.00    -5.00    33.72
79:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 15
Tendency to lay eggs: 13


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
80:0    0.00    6.38    20.15
80:1    0.60    0.00    29.77
80:2    -5.00    0.00    7.56
80:3    -5.17    -5.00    6.58
80:4    27.31    3.71    0.00
80:5    0.00    -5.00    33.72
80:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 16
Tendency to lay eggs: 14


Reward:  -10 , Next State:  6
TState Q(left) Q(right) Q(forward)
81:0    0.00    6.38    20.15
81:1    0.60    0.00    29.77
81:2    -5.00    0.00    7.56
81:3    -5.17    -5.00    7.03
81:4    27.31    3.71    0.00
81:5    0.00    -5.00    33.72
81:6    17.65    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 17
Tendency to lay eggs: 15
Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
82:0    0.00    6.38    20.15
82:1    0.60    0.00    29.77
82:2    -5.00    0.00    7.56
82:3    -5.17    -5.00    7.03
82:4    27.31    3.71    0.00
82:5    0.00    -5.00    33.72
82:6    7.31    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 18
Tendency to lay eggs: 16


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
83:0    0.00    6.38    20.15
83:1    0.60    0.00    29.77
83:2    -5.00    0.00    7.56
83:3    -4.11    -5.00    7.03
83:4    27.31    3.71    0.00
83:5    0.00    -5.00    33.72
83:6    7.31    -1.32    -5.00
I'm just a chill guy looking around
Ready to lay eggs!
Hunger level: 19
Tendency to lay eggs: 17


Reward:  -10 , Next State:  6
TState Q(left) Q(right) Q(forward)
84:0    0.00    6.38    20.15
84:1    0.60    0.00    29.77
84:2    -5.00    0.00    7.56
84:3    -4.11    -5.00    2.13
84:4    27.31    3.71    0.00
84:5    0.00    -5.00    33.72
84:6    7.31    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 20
Tendency to lay eggs: 18


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
85:0    0.00    6.38    20.15
85:1    0.60    0.00    29.77
85:2    -5.00    0.00    7.56
85:3    -4.11    -5.00    2.13
85:4    27.31    3.71    0.00
85:5    0.00    -5.00    33.72
85:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Ready to lay eggs!
Hunger level: 21
Tendency to lay eggs: 19


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
86:0    0.00    6.38    20.15
86:1    0.60    0.00    29.77
86:2    -5.00    0.00    7.56
86:3    -4.11    -5.00    -2.88
86:4    27.31    3.71    0.00
86:5    0.00    -5.00    33.72
86:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 22
Tendency to lay eggs: 20


Reward:  10 , Next State:  2
TState Q(left) Q(right) Q(forward)
87:0    0.00    6.38    20.15
87:1    0.60    0.00    29.77
87:2    -5.00    0.00    7.56
87:3    -4.11    6.24    -2.88
87:4    27.31    3.71    0.00
87:5    0.00    -5.00    33.72
87:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 23
Tendency to lay eggs: 21


Reward:  20 , Next State:  1
TState Q(left) Q(right) Q(forward)
88:0    0.00    6.38    20.15
88:1    0.60    0.00    29.77
88:2    -5.00    0.00    28.52
88:3    -4.11    6.24    -2.88
88:4    27.31    3.71    0.00
88:5    0.00    -5.00    33.72
88:6    -0.29    -1.32    -5.00
I am eating
Hunger level: 0
Tendency to lay eggs: 21


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
89:0    0.00    6.38    20.15
89:1    0.60    0.00    24.86
89:2    -5.00    0.00    28.52
89:3    -4.11    6.24    -2.88
89:4    27.31    3.71    0.00
89:5    0.00    -5.00    33.72
89:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 1
Tendency to lay eggs: 22


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
90:0    0.00    6.38    20.05
90:1    0.60    0.00    24.86
90:2    -5.00    0.00    28.52
90:3    -4.11    6.24    -2.88
90:4    27.31    3.71    0.00
90:5    0.00    -5.00    33.72
90:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 2
Tendency to lay eggs: 23


Reward:  20 , Next State:  4
TState Q(left) Q(right) Q(forward)
91:0    0.00    6.38    33.55
91:1    0.60    0.00    24.86
91:2    -5.00    0.00    28.52
91:3    -4.11    6.24    -2.88
91:4    27.31    3.71    0.00
91:5    0.00    -5.00    33.72
91:6    -0.29    -1.32    -5.00
I am laying eggs
Hunger level: 2
Tendency to lay eggs: 0


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
92:0    0.00    6.38    33.55
92:1    0.60    0.00    24.86
92:2    -5.00    0.00    28.52
92:3    -4.11    6.24    -2.88
92:4    30.26    3.71    0.00
92:5    0.00    -5.00    33.72
92:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 3
Tendency to lay eggs: 1


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
93:0    0.00    6.38    33.38
93:1    0.60    0.00    24.86
93:2    -5.00    0.00    28.52
93:3    -4.11    6.24    -2.88
93:4    30.26    3.71    0.00
93:5    0.00    -5.00    33.72
93:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 4
Tendency to lay eggs: 2


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
94:0    0.00    6.38    33.21
94:1    0.60    0.00    24.86
94:2    -5.00    0.00    28.52
94:3    -4.11    6.24    -2.88
94:4    30.26    3.71    0.00
94:5    0.00    -5.00    33.72
94:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 5
Tendency to lay eggs: 3


Reward:  0 , Next State:  0
TState Q(left) Q(right) Q(forward)
95:0    0.00    6.38    33.05
95:1    0.60    0.00    24.86
95:2    -5.00    0.00    28.52
95:3    -4.11    6.24    -2.88
95:4    30.26    3.71    0.00
95:5    0.00    -5.00    33.72
95:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 6
Tendency to lay eggs: 4


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
96:0    0.00    6.38    14.61
96:1    0.60    0.00    24.86
96:2    -5.00    0.00    28.52
96:3    -4.11    6.24    -2.88
96:4    30.26    3.71    0.00
96:5    0.00    -5.00    33.72
96:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 7
Tendency to lay eggs: 5


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
97:0    0.00    6.38    14.61
97:1    0.60    0.00    24.86
97:2    -5.00    0.00    28.52
97:3    -4.11    1.21    -2.88
97:4    30.26    3.71    0.00
97:5    0.00    -5.00    33.72
97:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 8
Tendency to lay eggs: 6


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
98:0    0.00    6.38    14.61
98:1    0.60    0.00    24.86
98:2    -5.00    0.00    28.52
98:3    -4.11    1.21    -5.84
98:4    30.26    3.71    0.00
98:5    0.00    -5.00    33.72
98:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 9
Tendency to lay eggs: 7


Reward:  -10 , Next State:  6
TState Q(left) Q(right) Q(forward)
99:0    0.00    6.38    14.61
99:1    0.60    0.00    24.86
99:2    -5.00    0.00    28.52
99:3    -4.11    -4.54    -5.84
99:4    30.26    3.71    0.00
99:5    0.00    -5.00    33.72
99:6    -0.29    -1.32    -5.00
I'm just a chill guy looking around
Whoops! I'm going back to my habitat!
Hunger level: 10
Tendency to lay eggs: 8
Whoops! I'm going back to my habitat!


Reward:  -10 , Next State:  3
TState Q(left) Q(right) Q(forward)
100:0    0.00    6.38    14.61
100:1    0.60    0.00    24.86
100:2    -5.00    0.00    28.52
100:3    -4.11    -4.54    -5.84
100:4    30.26    3.71    0.00
100:5    0.00    -5.00    33.72
100:6    -7.18    -1.32    -5.00
I'm just a chill guy looking around
Hunger level: 11
Tendency to lay eggs: 9

"""

# Initialize lists to store extracted data
data = []

# Split the data into lines for processing
lines = raw_data.strip().split("\n")

# Regex patterns for matching
state_pattern = re.compile(r"(\d+):(\d+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)")
reward_pattern = re.compile(r"Reward:\s+([-]?\d+)")
hunger_pattern = re.compile(r"Hunger level: (\d+)")
tendency_pattern = re.compile(r"Tendency to lay eggs: (\d+)")

# Variables to hold temporary values
current_trial = None
reward = None
hunger_level = None
tendency = None

# Iterate through each line
for line in lines:
    if "TState" in line:
        # New trial detected, reset trial-specific data
        current_trial = len(data) + 1
        reward = None
        hunger_level = None
        tendency = None
    elif reward_match := reward_pattern.search(line):
        # Extract the reward value
        reward = int(reward_match.group(1))
    elif hunger_match := hunger_pattern.search(line):
        # Extract the hunger level
        hunger_level = int(hunger_match.group(1))
    elif tendency_match := tendency_pattern.search(line):
        # Extract the tendency to lay eggs
        tendency = int(tendency_match.group(1))
    elif state_match := state_pattern.match(line):
        # Extract state and Q values
        state, action_left, action_right, action_forward = (
            int(state_match.group(2)),
            float(state_match.group(3)),
            float(state_match.group(4)),
            float(state_match.group(5)),
        )
        # Append the extracted data as a row
        data.append([
            current_trial,
            state,
            reward,
            hunger_level,
            tendency,
            action_left,
            action_right,
            action_forward,
        ])

# Verify data consistency
assert all(len(row) == 8 for row in data), "Mismatch in extracted data columns"

# Write into a new CSV file
with open("parsed_final_data.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    csvwriter.writerow(["Trial", "State", "Reward", "Hunger Level", "Tendency to Lay Eggs", "Q(left)", "Q(right)", "Q(forward)"])
    # Write the rows
    csvwriter.writerows(data)

print("Data has been successfully parsed and written to 'parsed_lab5_data.csv'")