# Algorithms

[TOC]

## Overview

These implementations are for individual study.

## Sorting

### Quicksort

The quicksort is implemented in `./quicksort.py`.


## Stable Matching

### Stable Marriage Problem

The [stable marriage problem](https://en.wikipedia.org/wiki/Stable_marriage_problem) is as below:
> Given *n* men and *n* women, where each person has ranked all members of the opposite sex in order of preference, marry the men and women together such that there are no two people of opposite sex who would both rather have each other than their current partners. When there are no such pairs of people, the set of marriages is deemed stable.

The Gale–Shapley algorithm which can __guarantee__ to get a stable matching is implemented in `./stable_marriage.py`  and as below:

```
Initialize men and women to unmatched
While not (all men and women are matched):
	m = a random unmatched man 
  	w = first unmatched woman on preference list of m 
  	if w is not matched:
  		match (m, w)
  	elif w is matched:
  		m_ = the man matched to w
  		if w prefer m to m_:
			release(m_, w)
			match(m, w)
```

Run the example with preference `./data_stable_marriage.csv` in the command line:

```shell
python stable_marriage.py
```

Note that:

1. The situation where men propose to women is different from where women propose to men. It can be shown in the result by running the example. In version of GS where men propose, each man receives the best valid partner (`w` is a valid partner of `m` if there exist stable matching where `m` and `w` are matched)
2. The result would be the same though the order of proposers is various. During the looping if man `m` is rejected, it means the woman `w` prefers another man `m_`. No matter whether `m_` and `w` are matched in the final result, `(m, w)`  must not be stable. Also, every man would propose to women by his preference. Actually, it can be thought as exhaustion from the best case of men to the worst case of them.
3. $O(n)=n^2$
4. The implementation uses 2 `dict` to represent the relation between men and women. Such as, `'A':'V'`means A is matched to B. Also for efficiency, `'A':0` means A is unmatched and it puts `0` in the last index of all preference lists.
5. Variants:
   * Some participants declare others as unacceptable.
   * Unequal number of men and women.
   * Limited polygamy.

### Stable Roommate Problem

__TBF__
