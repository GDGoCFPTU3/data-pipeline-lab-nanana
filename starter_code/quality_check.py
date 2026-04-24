# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

MIN_LENGTH = 10

def run_semantic_checks(doc_dict: dict) -> bool:
    content = str(doc_dict.get('content', '')).strip()

    if not content or len(content) < MIN_LENGTH:
        return False
    # 1. Kiểm tra độ dài: Nếu content trống hoặc < 10 ký tự -> False
    # TODO: Thực hiện kiểm tra độ dài ở đây

    # 2. Kiểm tra từ khóa lỗi
    toxic_keywords = ['Null pointer exception', 'OCR Error', 'Traceback']
    return all(w not in content for w in toxic_keywords)
