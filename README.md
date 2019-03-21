# Algorithms

## Overview

These implementations are for individual study.

## Sorting

### Quicksort

The quicksort is implemented in `./quicksort.py`.



## Stable Marriage Problem

The [stable marriage problem](https://en.wikipedia.org/wiki/Stable_marriage_problem) is as below:
> Given *n* men and *n* women, where each person has ranked all members of the opposite sex in order of preference, marry the men and women together such that there are no two people of opposite sex who would both rather have each other than their current partners. When there are no such pairs of people, the set of marriages is deemed stable.

The Gale–Shapley algorithm which can guarantee to get a stable matching is implemented in `./stable_marriage.py`  and as below:

```
Initialize men and women to unmatched
While not (all men and women are matched):
	m = a random unmatched man 
  	w = first unmatched woman on perference list of m 
  	if w is not matched:
  		match (m, w)
  	elif w is matched:
  		m_ = the man matched to w
  		if w prefer m to m_:
			release(m_, w)
				match(m, w)
```

