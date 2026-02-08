import os
import yaml
import pandas as pd
import math
import time

# 설정
FOLDER_PATH = "../_publications"
TARGET_AUTHOR = "Kyunghwan Choi"
METRICS_XLSX = "publications_metrics.xlsx"
PLOT_PAPER_LIST = 1 

def is_empty(value):
    """
    값이 None, NaN, 혹은 빈 문자열인지 확인하는 함수
    """
    if value is None:
        return True
    if isinstance(value, float) and math.isnan(value):
        return True
    if str(value).strip() == "":
        return True
    return False

def load_metrics_from_xlsx(xlsx_path):
    """
    Excel에서 {저널명: {IF, Quartile}} 정보를 가져옴
    """
    if not os.path.exists(xlsx_path):
        print(f"[Warning] {xlsx_path} 파일이 없습니다. 엑셀 파일을 먼저 생성해주세요.")
        return {}

    # 엑셀 파일 읽기
    df = pd.read_excel(xlsx_path)
    
    # 저널 이름을 키로 하는 딕셔너리로 변환 (공백 제거)
    df['Journal'] = df['Journal'].astype(str).str.strip()
    metrics_map = df.set_index('Journal').to_dict('index')
    
    return metrics_map

def get_integrated_papers():
    metrics_map = load_metrics_from_xlsx(METRICS_XLSX)
    
    integrated_data = []    # 정보가 매칭된 논문들
    missing_journal_papers = []  # Excel에 정보가 없는 논문들

    for root, _, files in os.walk(FOLDER_PATH):
        for file in files:
            # 1. '_'로 시작하는 참조 파일 및 확장자 예외처리
            if not file.endswith(".md") or file.startswith("_"):
                continue

            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                parts = content.split("---")
                yaml_content = parts[1] if len(parts) > 2 else content
                data = yaml.safe_load(yaml_content)

                # 조건 필터링 (International Journal & Published & 본인 저자)
                is_int_journal = (data.get("type") == "Journal Paper" and 
                                  data.get("domestic_or_international") == "International")
                
                has_author = any(isinstance(a, dict) and a.get("name") == TARGET_AUTHOR 
                                 for a in data.get("authors", []))

                if is_int_journal and has_author:
                    pubs = data.get("pub", [])
                    published_info = next((p for p in pubs if p.get("state") == "published"), None)
                    
                    if published_info:
                        journal_name = published_info.get("name", "").strip()
                        
                        # 2. Excel 데이터 매칭
                        if journal_name in metrics_map and (not is_empty(metrics_map[journal_name].get('Impact Factor')) and not is_empty(metrics_map[journal_name].get('Quartile'))):
                            m = metrics_map[journal_name]
                            integrated_data.append({
                                "title": data.get("title"),
                                "journal": journal_name,
                                "year": published_info.get("year"),
                                "impact_factor": m.get('Impact Factor'),
                                "quartile": m.get('Quartile')
                            })
                        else:
                            missing_journal_papers.append({
                                "title": data.get("title"),
                                "journal": journal_name,
                                "year": published_info.get("year")
                            })

            except Exception as e:
                print(f"[Error] {file_path}: {e}")

    return integrated_data, missing_journal_papers

# 실행
papers_data, missing_data = get_integrated_papers()

# 결과 출력 (Pandas DataFrame을 쓰면 출력이 예쁩니다)
print("\n=== 논문 저널 매칭 결과 ===")
print(f"총 논문 수: {len(papers_data) + len(missing_data)}")
print(f"매칭 완료된 논문 수: {len(papers_data)}")
print(f"정보가 없는 저널 논문 수: {len(missing_data)}")
recent_q1_papers = [p for p in papers_data if p['quartile'] == 'Q1' and int(p['year']) >= int(time.strftime('%Y')) - 5]
print(f"최근 5년 Q1 이상 논문 수: {len(recent_q1_papers)}")
recent_sci_papers = [p for p in papers_data if int(p['year']) >= int(time.strftime('%Y')) - 5]
print(f"최근 5년 SCI 논문 수: {len(recent_sci_papers)}")
print(f"최근 5년 Q1 이상 논문 비율: {len(recent_q1_papers) / len(recent_sci_papers) * 100:.2f}%")

if PLOT_PAPER_LIST:
    if papers_data:
        print("\n### [성공] 매칭 완료된 논문 목록 ###")
        data = pd.DataFrame(papers_data)
        data.index = range(1, len(data) + 1)  # 인덱스 1부터 시작 
        print(data[['year', 'journal', 'impact_factor', 'quartile', 'title']])

    if missing_data:
        print(f"\n### [주의] Excel에 정보가 없는 저널 ({len(missing_data)}편) ###")
        data = pd.DataFrame(missing_data)
        data.index = range(1, len(data) + 1)  # 인덱스 1부터 시작
        print(data[['year', 'journal', 'title']])
        
    print(f"\n### 최근 5년간 Q1 이상 논문 ###")
    if recent_q1_papers:
        data = pd.DataFrame(recent_q1_papers)
        data.index = range(1, len(data) + 1)  # 인덱스 1부터 시작
        print(data[['year', 'journal', 'impact_factor', 'quartile', 'title']])

    print(f"\n### 최근 5년간 SCI 논문 ###")
    if recent_sci_papers:
        data = pd.DataFrame(recent_sci_papers)
        data.index = range(1, len(data) + 1)  # 인덱스 1부터 시작
        print(data[['year', 'journal', 'impact_factor', 'quartile', 'title']])