from datetime import datetime, timedelta
import requests

# 초기 날짜 설정
start_date_str = "2023-07-05"
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
# 몇 번 반복할지 정의
num_iterations = 11
headers = {
  "x-nxopen-api-key": ""
}

arr = []
# for 문을 사용하여 날짜를 1씩 증가시키기
for i in range(num_iterations):
    current_date = start_date + timedelta(days=i)
    formatted_date = current_date.strftime("%Y-%m-%d")
    print(type(formatted_date), formatted_date)
    urlString = "https://open.api.nexon.com/maplestory/v1/history/cube?count=100&date=" + formatted_date
    response = requests.get(urlString, headers = headers)
    arr.append(response.json())