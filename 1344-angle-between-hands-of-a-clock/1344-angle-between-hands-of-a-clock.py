class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour ==12:
            hour = 0
        h = hour + minutes/60
        '''
        the clock is composed of 12 h so in degrees it is 360/12 for each hour exact
        while for minutes it is devided into 60 so 360/60
        '''
        h_angle = (360/12)*h
        m_angle = (360/60)*minutes
        print(h_angle)
        print(m_angle)
        return min(abs(h_angle - m_angle), 360 - abs(h_angle - m_angle))