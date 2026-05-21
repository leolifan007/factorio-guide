#!/usr/bin/env python3
"""
本地模拟 staged-deploy workflow 的核心逻辑
验证 manifest 读取、random skip、unit 选择、manifest 更新
"""
import json
import random
import sys
import os

print("=" * 60)
print("Staged Deploy Workflow — 本地模拟验证")
print("=" * 60)

# 模拟 manifest
manifest_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.deploy-manifest.json')
import subprocess
result = subprocess.run(['git', 'show', 'content-fixes-staged:.deploy-manifest.json'], capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data = json.loads(result.stdout)

total = len(data['units'])
pending = [u for u in data['units'] if not u.get('deployed')]
print(f"\n📦 总 units: {total}")
print(f"⏳ 待部署: {len(pending)}")

# 模拟 10 次"触发"（每次可能跳过）
print("\n" + "=" * 60)
print("模拟 10 次 cron 触发 (50% skip, 随机选 1-2)")
print("=" * 60)

random.seed(42)  # 固定种子可复现

all_ids = set(u['id'] for u in data['units'])
deployed_ids = set()

for round_num in range(10):
    print(f"\n--- Round {round_num + 1} ---")
    
    # Step 1: 随机延迟
    delay = random.randint(300, 1800)
    print(f"  ⏳ 初始延迟: {delay}s")
    
    # Step 2: 50% coin flip
    roll = random.randint(0, 99)
    skip = roll < 50
    print(f"  🎲 Coin flip: {roll} {'❌ SKIPPED' if skip else '✅ PROCEED'}")
    if skip:
        continue
    
    # Step 3: 二次延迟
    delay2 = random.randint(60, 600)
    print(f"  ⏳ 二次延迟: {delay2}s")
    
    # Step 4: 从 pending 中选
    remaining = [u for u in data['units'] if not u.get('deployed')]
    if not remaining:
        print("  ✅ 全部部署完成！")
        break
    
    # 随机选 1-2 个
    pick_count = 1 if random.random() < 0.6 else 2
    pick_count = min(pick_count, len(remaining))
    chosen = random.sample(remaining, pick_count)
    
    for u in chosen:
        content_count = len(u['files']['content'])
        docs_count = len(u['files']['docs'])
        print(f"  📄 → {u['id']} ({content_count} content + {docs_count} docs)")
        print(f"     msg: {u['message'][:50]}...")
        
        # 模拟文件拷贝
        for fpath in u['files']['content']:
            if os.path.exists(os.path.join(os.path.dirname(manifest_path), fpath)):
                print(f"     ✅ content: {fpath}")
            else:
                print(f"     ❌ MISSING: {fpath}")
        
        for fpath in u['files']['docs']:
            full_path = os.path.join(os.path.dirname(manifest_path), fpath)
            if os.path.exists(full_path):
                print(f"     ✅ docs: {fpath} ({os.path.getsize(full_path)} bytes)")
            else:
                print(f"     ❌ MISSING: {fpath}")
        
        # 标记已部署
        u['deployed'] = True
        deployed_ids.add(u['id'])
    
    print(f"  📊 进度: {len([u for u in data['units'] if u.get('deployed')])}/{total}")

# 最终统计
print("\n" + "=" * 60)
print("最终部署状态")
print("=" * 60)
for u in data['units']:
    status = '✅' if u.get('deployed') else '⏳'
    print(f"  {status} {u['id']}: {u['message'][:60]}")

print(f"\n总计: {len([u for u in data['units'] if u.get('deployed')])}/{total} 已部署")
print("✅ Workflow 核心逻辑验证通过！" if all(u.get('deployed') for u in data['units']) else "⏳ 模拟正常（随机skip机制生效）")

# 验证所有文件是否存在
print("\n" + "=" * 60)
print("文件完整性检查")
print("=" * 60)
all_ok = True
for u in data['units']:
    for key in ['content', 'docs']:
        for fpath in u['files'][key]:
            full_path = os.path.join(os.path.dirname(manifest_path), fpath)
            exists = os.path.exists(full_path)
            if not exists:
                print(f"  ❌ MISSING: {fpath}")
                all_ok = False
if all_ok:
    print("  ✅ 所有 manifest 中列出的文件都存在")
else:
    print("  ⚠️ 部分文件缺失")
