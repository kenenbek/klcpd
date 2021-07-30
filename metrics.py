import numpy as np
import pandas as pd

class OnlineQualityMetrics(object):
    
    def __init__(self, thresholds):
        self.thresholds = thresholds
        
    def _time_false_alarm(self, score, label, thr):
        score_0 = score[label==0]
        T = np.arange(len(score_0))
        tfa = len(score_0)
        alarms = T[score_0 >= thr]
        if len(alarms) != 0:
            tfa = alarms[0]
        return tfa
    
    def _detection_delay(self, score, label, thr):
        score_1 = score[label==1]
        T = np.arange(len(score_1))
        dd = len(score_1)
        alarms = T[score_1 >= thr]
        if len(alarms) != 0:
            dd = alarms[0]
        return dd
        
        
    def estimate(self, score, label):
        
        data = []
        for thr in self.thresholds:
            tfa = self._time_false_alarm(score, label, thr)
            dd  = self._detection_delay(score, label, thr)
            data.append([thr, tfa, dd])
        
        curve = pd.DataFrame(columns=['Threshold', 'TimeFalseAlarm', 'DetectionDelay'], 
                             data=data)
        return curve