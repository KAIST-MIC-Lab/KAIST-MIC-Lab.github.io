"""
pub2tex.py

VERSION HISTORY:
- Version 1.0 (Date: 2025.07.26)
- Version 1.1 (Date: 2025.08.15) - Bug fix in publication year extraction.

- Myeongseok Ryu
- dding_98@kaist.ac.kr
- 2025.07.26
"""

import os
import yaml

# WHO_ARE_YOU = "Kyunghwan Choi" 
WHO_ARE_YOU = "Myeongseok Ryu" 

def find_files_with_author(folder_path, target_author=WHO_ARE_YOU):

    under_review = []
    dom_conf = []
    dom_jour = []
    int_conf = []
    int_jour = []
    preprint = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if not file.endswith((".md")):
                continue

            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # YAML front matter 영역만 추출
                if content.strip().startswith("---"):
                    parts = content.split("---")
                    if len(parts) > 2:
                        yaml_content = parts[1]
                    else:
                        yaml_content = content
                else:
                    yaml_content = content

                data = yaml.safe_load(yaml_content)

                # authors 필드 확인
                if data and "authors" in data:
                    for author in data["authors"]:
                        if isinstance(author, dict) and author.get("name") == target_author:

                            if not "pub" in data:
                                preprint.append(file_path)
                            elif data["pub"][-1]["state"] == "submitted":
                                under_review.append(file_path)
                                break
                            elif data["type"] == "Conference Paper":
                                if data["domestic_or_international"] == "International":
                                    int_conf.append(file_path)
                                else:
                                    dom_conf.append(file_path)
                            elif data["type"] == "Journal Paper":
                                if data["domestic_or_international"] == "International":
                                    int_jour.append(file_path)
                                else:
                                    dom_jour.append(file_path)
                            break

            except Exception as e:
                print(f"[ERROR] {file_path}: {e}")

    return under_review, int_jour, int_conf, dom_conf, dom_jour, preprint

def make_TeX(category, files):
    TEX_RESULT = f"""
\\footnotesize{{\\textbf{{{category}}}

\\begin{{etaremune}}
"""
    
    # sort files by publication date
    files.sort(key=lambda x: yaml.safe_load(open(x, "r", encoding="utf-8").read().split("---")[1]).get("pub_date"), reverse=True)
    
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        if content.strip().startswith("---"):
            parts = content.split("---")
            if len(parts) > 2:
                yaml_content = parts[1]
            else:
                yaml_content = content
        else:
            yaml_content = content

        data = yaml.safe_load(yaml_content)

        authors = []
        for author in data["authors"]:
            if isinstance(author, dict) and author.get("name") == WHO_ARE_YOU:
                authors.append(f"\\textbf{{\\underline{{{author['name']}}}}}")
            else:
                authors.append(author["name"])

            if "corresponding" in author:
                authors[-1] += "\\textsuperscript{{*}}"

        title = data.get("title", "No Title")

        # year in pub_date field // replaced by year in pub field if exists
        pub_date = data.get("pub_date", "No Date")
        pub_year = pub_date.split("-")[0] if pub_date else "No Year"

        if "pub" in data:

            # not preprint
            pub_info = data["pub"][-1]
            publisher = pub_info["name"]
                
            pub_details = []
            if "vol" in pub_info:
                if pub_info["vol"] is not None:
                    pub_details.append(f"vol. {pub_info['vol']}")
            if "num" in pub_info:
                if pub_info["num"] is not None:
                    pub_details.append(f"no. {pub_info['num']}")
            if "pp" in pub_info:
                if pub_info["pp"] is not None:
                    pub_details.append(f"pp. {pub_info['pp']}")
            if "year" in pub_info:
                if pub_info["year"] is not None:
                    pub_year = pub_info["year"]
            pub_details.append(f"{pub_year}")

            state = pub_info["state"]

            url = "none"
            if url == "none" and "url" in pub_info:
                if pub_info["url"] is not None:
                    url = f"\\href{{{pub_info['url']}}}{{{title}}}"
            if url == "none" and "doi" in pub_info:
                if pub_info["doi"] is not None:
                    url = f"\\href{{https://doi.org/{pub_info['doi']}}}{{{title}}}"
            if url == "none" and "preprint" in data:
                preprint_info = data["preprint"][-1]
                
                if "doi" in preprint_info:
                    if preprint_info["doi"] is not None:
                        url = f"\\href{{https://doi.org/{preprint_info['doi']}}}{{{title}}}"
                
        else:
            # preprint
            if "year" in data["preprint"][-1]:
                if data["preprint"][-1]["year"] is not None:
                    pub_year = data["preprint"][-1]["year"]
            pub_info = data["preprint"][-1]
            publisher = pub_info["name"]
            pub_details = [f"{pub_year}"]
            state = "preprint"

            url = "none"
            if "doi" in pub_info:
                if pub_info["doi"] is not None:
                    url = f"\\href{{https://doi.org/{pub_info['doi']}}}{{{title}}}"
        
        TEX_RESULT += f"""
    \\item {{
        {url if url != "none" else title}
        \\\\
        {", ".join(authors)}
        \\\\
        \\textit{{
            \\textbf{{{publisher}}}{', (accepted, in press), ' if state == 'accepted' else ', '}{", ".join(pub_details)}
        }}
    }}
"""

    TEX_RESULT += f"""
\\end{{etaremune}}}}
    """

    return TEX_RESULT

def main():
    # 사용 예시
    folder = "_publications"  # 여기에 폴더 경로 입력
    under_review, int_jour, int_conf, dom_conf, dom_jour, preprint = find_files_with_author(folder)
    print("Found files:")
    for category, files in zip(
        [
            "Papers Under Review", "International Journal Papers", "International Conference Papers", 
            "Domestic Conference Papers", "Domestic Journal Papers", "Preprint Papers"
        ],
        [under_review, int_jour, int_conf, dom_conf, dom_jour, preprint]
    ):
        print(f"  {category}: {len(files)} files")
        for f in files:
            print(f"    - {f}")

    print("\nGenerating TeX files...")

    # TeX 파일 생성
    TEX_FILES = ""
    for category, files in zip(
        [
            "Papers Under Review", "International Journal Papers", "International Conference Papers", 
            "Domestic Conference Papers", "Domestic Journal Papers", "Preprint Papers"
        ],
        [under_review, int_jour, int_conf, dom_conf, dom_jour, preprint]
    ):
        if len(files) > 0:
            TEX_RESULT = make_TeX(category, files)
            TEX_FILES += TEX_RESULT

    # print("Generated TeX files:")
    # print(TEX_FILES)

    save_path = "publications.tex"
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(TEX_FILES)

    print(f"TeX files saved to {save_path}")

if __name__ == "__main__":
    main()