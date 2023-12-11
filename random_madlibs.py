# The code is importing four different modules (`hp`, `code`, `zombie`, `hungergames`) from the
# `sample_madlibs` package. It also imports the `random` module.

from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m= random.choice([hp, code, zombie, hungergames])
    m.madlib()