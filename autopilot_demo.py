#!/usr/bin/env python3
"""
Autopilot Demo Program
แสดงผลของ humanize.naturaltime กับ timedelta 5 นาที
"""

import humanize
from datetime import timedelta as dt

def main():
    # สร้าง timedelta 5 นาที
    time_delta = dt(minutes=5)
    
    # แปลงเป็นข้อความธรรมชาติด้วย humanize
    result = humanize.naturaltime(time_delta)
    
    # แสดงผลลัพธ์
    print(result)

if __name__ == "__main__":
    main()
