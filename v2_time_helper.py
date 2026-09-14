#!/usr/bin/env python3
"""
Time Helper Module v2
คืนค่า timedelta 10 นาที
"""

from datetime import timedelta

def get_ten_minutes_delta():
    """
    คืนค่า datetime.timedelta(minutes=10)
    
    Returns:
        timedelta: เวลา 10 นาที
    """
    return timedelta(minutes=10)
