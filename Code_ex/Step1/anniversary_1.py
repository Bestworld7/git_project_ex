from datetime import datetime

now = datetime.now()
wedding_day = datetime(2012,3,1)
wedding_das = now - wedding_day
print(f"우리 결혼하지 + {wedding_das} 일째")