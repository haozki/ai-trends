import urllib.request
import json
import os

# Use proxy if available
proxy = os.environ.get("https_proxy") or os.environ.get("HTTPS_PROXY")
if proxy:
    proxy_handler = urllib.request.ProxyHandler({"https": proxy, "http": proxy})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

candidates = {
    "OpenAI":      ["openai"],
    "Anthropic":   ["anthropic"],
    "Google":      ["google"],
    "xAI":         ["xai", "x-ai", "x"],
    "Meta":        ["meta", "facebook"],
    "Alibaba":     ["alibaba", "qwen", "alibabacloud"],
    "Baidu":       ["baidu", "ernie"],
    "DeepSeek":    ["deepseek"],
    "Z.ai":        ["zhipuai", "zhipu", "chatglm", "glm"],
    "Moonshot":    ["moonshot", "moonshotai", "kimi"],
    "Xiaomi":      ["xiaomi", "mimo"],
    "ByteDance":   ["bytedance", "byte-dance", "doubao"],
    "Tencent":     ["tencent", "hunyuan"],
    "Mistral":     ["mistral", "mistralai"],
    "Microsoft":   ["microsoft"],
    "MiniMax":     ["minimax", "mini-max"],
}

results = {}

for company, ids in candidates.items():
    for pid in ids:
        url = f"https://models.dev/logos/{pid}.svg"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            resp = urllib.request.urlopen(req, timeout=10)
            data = resp.read()
            if resp.status == 200 and len(data) > 50 and b"<svg" in data.lower():
                results[company] = pid
                print(f"  {company}: {pid} OK ({len(data)} bytes)")
                break
            else:
                print(f"  {company}: {pid} - status {resp.status}, size {len(data)}")
        except Exception as e:
            print(f"  {company}: {pid} - {type(e).__name__}: {e}")
    if company not in results:
        print(f"  {company}: NOT FOUND")

print("\n--- RESULTS ---")
for company, pid in results.items():
    print(f'"{company}": "https://models.dev/logos/{pid}.svg",')
