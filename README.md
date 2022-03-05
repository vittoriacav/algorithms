# algorithms

:books: "Algorithms and Data Structures for Biology" assignments (Genomics, UniBo)

## Assignment 1 ##

Suppose you are the employee of a pharmaceutical company, which has to buy as much of a certain type of chemical substance as possible in a short amount of time. Suppose you have access to offers from n suppliers, which for convenience we indicate with s1; : : : ; sn. The supplier si can offer your company an amount of the chemical substance (within the given period) equal to wi grams. However, there is a problem: for reasons related to the nature of the products purchased and to your company's policy, the product supplied by certain suppliers is incompatible with that supplied by some of the other suppliers. In other words, the company has, for each supplier si, a list Li of the other suppliers sj with which si is incompatible (so Li is of length at most n - 1). Your task, as an employee of the company, is to determine the purchase plan, i.e. the suppliers to be selected, which allows the company to maximize the amount of chemical substance to be purchased.

This assignment asks you to:
- Model the problem described above as a combinatorial optimization problem, abstracting away from unessential details.
- Give an exhaustive search algorithm solving the combinatorial problem from the previous point; the key idea here consists in finding an appropriate way to define the search space, in such a way that exploring it turns out to be easy.
- Analyse the algorithm's complexity: give a relevant upper bound to the worst-case compu tation time, in big O notation, in function of n (the total number of suppliers).
- Implement the algorithm you designed in Python. Please do not use external modules.
- Design and implement a Python testing routine which tests your algorithm on randomly generated inputs in which

## Assignment 2 ##

Suppose you are a researcher who needs to move all her equipment to a new workplace on the other side of the world, where she just got a new job. Her research equipment consists of n objects, the i-th object having a weight equal to wi kilograms. The way the researcher is supposed to send her equipment is by way of containers. Each container has enough space capacity to contain an arbitrary amount of objects, in principle all the n objects. There is however a constraint: each container is, for structural reasons, able to carry at most C kilograms, where C is typically smaller than summation(wi, from i=1 to n), but higher than each of the wi. In other words, the researcher needs more than one container, each of them costing a fixed amount p to be sent. The problem the researcher faces, then, is allocating the objects to as few containers as possible, this way minimizing the cost of shipping all the n objects to their final destination.
This assignment asks you to:
1. Model the problem described above as a combinatorial optimization problem (actually one we have encountered at some point in our course).
2. Give an exhaustive search algorithm solving the combinatorial problem from the previous point, and analyse the algorithm's complexity: give an upper bound to the worst-case computation time, in big O notation, in function of n.
3. Give a greedy algorithm that solves the same combinatorial problem from point 1 (or more precisely, that gives an approximate solution), and analyse the algorithm's complexity. Again, the bound should be a function on n. Give an upper bound to the approximation ratio of this algorithm (that is to say, the ratio of the cost of the solution it proposes to the cost of the optimal solution).
4. Make up two instances of the problem, one with n = 4;C = 2, the other with n = 6;C = 2:5, and both with the wi between 0 and 1. Then,
- solve them by hand (i.e. find the optimal solutions),
- apply by hand your greedy algorithm on each of them (you may obtain sub-optimal solutions).
In your report, you do not need to give the details of your calculations: just describe both instances and give both sets of solutions.
5. Implement the two algorithms you designed as two Python functions. The two functions should have the same interface (i.e. they should have the same arguments and return their results in the same format). Please do not use external modules.
6. Write an automated testing routine that runs each function on each instance from point 4 and checks that they give the appropriate results.
7. Write a benchmarking routine that takes as argument either of the two functions (which is why they need to have the same interface) and runs it on randomly generated inputs in which
- n is, successively, 4; 6; 8; 10; 12; 14; 16; 18; 20,
- the weights wi are drawn uniformly and independently between 0 and 1.
- the capacity C of each container is chosen as sqrt(n).
The benchmarking routine should make use of the random module only.
8. Use the module timeit to experimentally test the running time of both functions. Give a graphical presentation of your results. Moreover, try to find the best-fit curves matching the two algorithms complexity by way of numpy and scipy.
9. Evaluate the (worst-case) approximation ratio of the solution given by your greedy program (with respect to the exact solution provided by your exhaustive program). Is it within the theoretical bounds you established in point 3?

## Assignment 3 ##

The problem we want to solve in this assignment is relatively simple to be described, and we are sure this will look somewhat familiar to you. You're given a long strand of DNA, i.e., a string s of n characters in the four-letter alphabet {A; C; T; G}, and you want to know if there are particular patterns that are repeated often in s, possibly with small modifications. More precisely, you're given a pattern length m <= n and a maximum distance k, and you want to know the string t of length m that is repeated most often in s, with up to k modifications. For example, if the strand of DNA is s = "GATTACA", the pattern length is m = 3 and the maximum distance is k = 1, then the best pattern is t = "ATA", has 3 approximate occurrences, at indices 1 ("ATT"), 1 ("TTA") and 4 ("ACA"). Note that, paradoxically, in this case, the best pattern does not appear exactly anywhere in the strand. An exact description of the problem requires some auxiliary mathematical definitions. Given two strings x; y of the same length and in the same alphabet, their Hamming distance H(x; y) is the number of positions in which x and y dffer (for example, H("ATA"; "ACA") = 1). A k-occurrence of a string x of length m in a string y of length n is the data of an index i <= n - m such that H(x; y[i : m]) <= k, where y[i : m] denotes the substring of y that starts at index i and has length m. We denote the number of distinct k-occurrences of x in y by Ok(x; y). Your problem is, given s; m; k as above, to compute the string t which makes Ok(t; s) maximum among all m-character strings.

This assignment asks you to:
1. Write a Python program which reads from a file called inputdata.txt the following data:
- a natural number m in decimal notation, in the first line;
- a natural number k in decimal notation, in the second line;
- a string s over the alphabet {A; C; T; G} in the third line;
and then determines the string t of length m that maximizes Ok(t; s) (or one such string, if there are several possibiities), and prints that string.
2. Test it against the example file inputdata.txt 
