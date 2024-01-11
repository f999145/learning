from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Обработка запроса
    print(f"Request URL: {flow.request.url}")

def response(flow: http.HTTPFlow) -> None:
    # Обработка ответа
    print(f"Response URL: {flow.request.url}")
    print(f"Response Status Code: {flow.response.status_code}")
    print(f"Response Content: {flow.response.text}")

# Запустите прокси с использованием скрипта
# mitmproxy -p 8080 -s your_script.py
