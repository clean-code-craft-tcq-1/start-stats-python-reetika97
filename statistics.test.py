import unittest
import statistics
import math

class EmailAlert():
  emailSent=0
    
class LEDAlert():
  ledGlows=0

class StatsAlerter:
  def __init__(self,maxThreshold, alerts):
    self.mt=maxThreshold
    self.ea=alerts[0].emailSent
    self.la=alerts[1].ledGlows    
    
  def checkAndAlert(self,lt):
    for i in range(0,len(lt)):
        if lt[i]>self.mt:
            self.ea=1
            self.la=1
    return [self.ea,self.la]

class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    [emailAlert.emailSent,ledAlert.ledGlows ]=statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)

if __name__ == "__main__":
  unittest.main()
