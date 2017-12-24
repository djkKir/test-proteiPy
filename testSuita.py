

import unittest

from testForvard import TestPosition
from testReverse import TestAddress

# load test cases
tc0 = unittest.TestLoader().loadTestsFromTestCase(TestAddress)
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestPosition)

# create test suite
ts = unittest.TestSuite([tc0, tc1])

# execute test suite
unittest.TextTestRunner(verbosity=2).run(ts)