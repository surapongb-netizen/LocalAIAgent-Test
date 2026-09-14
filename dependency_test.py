#!/usr/bin/env python3
"""
Dependency Test Program
ทดสอบการ import humanize และ datetime
แสดงผล naturaltime ของ timedelta 3 วินาที
"""

import humanize
from datetime import timedelta as dt

def main():
    # สร้าง timedelta 3 วินาที
    time_delta = dt(seconds=3)
    
    # แปลงเป็นข้อความธรรมชาติด้วย humanize
    result = humanize.naturaltime(time_delta)
    
    # แสดงผลลัพธ์
    print(result)

if __name__ == "__main__":
    main()
