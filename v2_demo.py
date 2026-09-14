#!/usr/bin/env python3
"""
Demo Program v2
เรียกใช้ฟังก์ชันจาก v2_time_helper และแสดงผลด้วย humanize.naturaltime
"""

import humanize
from datetime import timedelta as dt
import v2_time_helper

def main():
    # เรียกใช้ฟังก์ชันจาก module helper
    time_delta = v2_time_helper.get_ten_minutes_delta()
    
    # แปลงเป็นข้อความธรรมชาติด้วย humanize
    result = humanize.naturaltime(time_delta)
    
    # แสดงผลลัพธ์
    print(result)

if __name__ == "__main__":
    main()
