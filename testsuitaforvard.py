

import unittest

from testForvard import TestAddress

# load test cases
tc = unittest.TestLoader().loadTestsFromTestCase(TestAddress)

# create test suite
ts = unittest.TestSuite([tc])

# execute test suite
unittest.TextTestRunner(verbosity=2).run(ts)