Non-Starvation
==============

When we added priorities we always read High before Medium before Low. If there is too much on high, medium and low will never be read.

Make a schema so that maximum of 70% is read from high, 20% from medium and 10% from low.