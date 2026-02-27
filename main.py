import os
import json
import datetime
import requests

FEISHU_APP_ID = os.environ["FEISHU_APP_ID"]
FEISHU_APP_SECRET = os.environ["FEISHU_APP_SECRET"]
BITABLE_APP_TOKEN = os.environ["FEISHU_BITABLE_APP_TOKEN"]
BITABLE_TABLE_ID = os.environ["FEISHU_BITABLE_TABLE_ID"]
TARGET_USER_EMAIL = os.environ["FEISHU_TARGET_USER_EMAIL"]

def get_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    r = requests.post(url, json={
        "app_id": FEISHU_APP_ID,
        "app_secret": FEISHU_APP_SECRET
    })
    return r.json()["tenant_access_token"]

def write_record(token, fields):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{BITABLE_APP_TOKEN}/tables/{BITABLE_TABLE_ID}/records"
    headers = {"Authorization": f"Bearer {token}"}
    requests.post(url, headers=headers, json={"fields": fields})

def main():
    token = get_token()
    today = datetime.date.today().isoformat()

    # 这里是示例数据
    rows = [
        {
            "日期": today,
            "类型": "厚文",
            "来源": "TechCrunch",
            "公司 / 事件": "示例AI公司融资",
            "一句话核心": "完成 3000 万美元融资",
            "赛道": "Agent",
            "炸点": "创始人来自Stripe",
            "延展角度": "Agent替代SaaS可能性",
            "关键数据（美元）": "30000000",
            "素材链接": "https://techcrunch.com",
            "状态": "待核验"
        }
    ]

    for r in rows:
        write_record(token, r)

if __name__ == "__main__":
    main()
