#!/usr/bin/env python3
"""
Time Helper Module v2
คืนค่า timedelta 15 นาที
"""

from datetime import timedelta

def get_ten_minutes_delta():
    """
    คืนค่า datetime.timedelta(minutes=15)
    
    Returns:
        timedelta: เวลา 15 นาที
    """
    return timedelta(minutes=15)
