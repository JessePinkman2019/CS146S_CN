#!/usr/bin/env python3
"""
使用 playwright 渲染 HTML 并截图为 PNG
解决 cairosvg 中文字体和 emoji 显示问题
"""
from playwright.sync_api import sync_playwright
import os

os.chdir('/chj/home/wanglang3/code/sch-demo/docs/claude_code_guide')

html_files = [
    'minimum_context.html',
    'workflow_diagram.html',
    'agentloop_diagram.html',
    'knowledge_diagram.html',
    'context_diagram.html',
    'flywheel_diagram.html',
    'claudemd_diagram.html',
    'skills_diagram.html',
    'memory_diagram.html',
    'subagents_diagram.html',
    'transition_diagram.html',
    'planmode_diagram.html',
    'session_diagram.html'
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for html_file in html_files:
        if not os.path.exists(html_file):
            print(f"SKIP: {html_file}")
            continue

        png_file = html_file.replace('.html', '.png')
        file_path = f'file://{os.path.abspath(html_file)}'

        try:
            page.goto(file_path, wait_until='networkidle')
            page.wait_for_timeout(1000)  # 等待渲染完成
            page.screenshot(path=png_file, full_page=True)
            print(f"✓ {png_file}")
        except Exception as e:
            print(f"✗ {html_file}: {e}")

    browser.close()

print("\n所有 PNG 生成完成！")
