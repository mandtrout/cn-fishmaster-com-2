def build_site_summary():
    site_info = {
        "title": "捕鱼达人指南站",
        "url": "https://cn-fishmaster.com",
        "keywords": ["捕鱼达人", "街机游戏", "休闲娱乐", "高分技巧", "捕鱼攻略"],
        "tags": ["game", "arcade", "fishing", "casual", "guide"],
        "description": (
            "一个专注于捕鱼达人系列游戏的资料站，"
            "提供游戏攻略、装备介绍、高分技巧和最新活动资讯。"
        ),
        "category": "游戏攻略",
        "language": "zh-CN",
        "last_updated": "2025-03-01"
    }

    summary_lines = []
    summary_lines.append("=" * 50)
    summary_lines.append(f"站点名称：{site_info['title']}")
    summary_lines.append(f"访问地址：{site_info['url']}")
    summary_lines.append(f"站点类别：{site_info['category']}")
    summary_lines.append(f"语言：{site_info['language']}")
    summary_lines.append(f"最后更新：{site_info['last_updated']}")
    summary_lines.append("")
    summary_lines.append("核心关键词：")
    for kw in site_info["keywords"]:
        summary_lines.append(f"  - {kw}")
    summary_lines.append("")
    summary_lines.append("标签：")
    for tag in site_info["tags"]:
        summary_lines.append(f"  [{tag}]")
    summary_lines.append("")
    summary_lines.append("站点简介：")
    summary_lines.append(f"  {site_info['description']}")
    summary_lines.append("=" * 50)
    return "\n".join(summary_lines)


def generate_keyword_highlights(keywords):
    highlights = []
    for idx, kw in enumerate(keywords, start=1):
        highlight = f"#{idx} {kw.upper()} —— 相关资源推荐"
        highlights.append(highlight)
    return highlights


def build_url_tag_mapping(url, tags):
    mapping = {
        "站点地址": url,
        "标签一览": tags,
        "标签数量": len(tags),
        "是否包含游戏标签": "game" in tags
    }
    return mapping


def format_mapping_as_text(mapping):
    lines = []
    lines.append("站点标签映射信息：")
    for key, value in mapping.items():
        lines.append(f"  {key}: {value}")
    return "\n".join(lines)


def main():
    summary = build_site_summary()
    print(summary)
    print()

    highlights = generate_keyword_highlights(["捕鱼达人", "高分技巧", "街机游戏", "休闲模式"])
    print("关键词高亮推荐：")
    for h in highlights:
        print(f"  {h}")
    print()

    mapping = build_url_tag_mapping("https://cn-fishmaster.com", ["game", "arcade", "fishing"])
    mapping_text = format_mapping_as_text(mapping)
    print(mapping_text)


if __name__ == "__main__":
    main()