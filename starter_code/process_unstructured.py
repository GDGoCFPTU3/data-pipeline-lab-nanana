import re
from datetime import datetime

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def process_pdf_data(raw_json: dict) -> dict:
    # Bước 1: Làm sạch nhiễu (Header/Footer) khỏi văn bản
    raw_text = raw_json.get("extractedText", "")
    # TODO: Dùng re.sub để xóa 'HEADER_PAGE_X' và 'FOOTER_PAGE_X'
    cleaned_content = re.sub(r"[HEADER|FOOTER]_PAGE_\d+", "", raw_text)

    # Bước 2: Map dữ liệu thô sang định dạng chuẩn của UnifiedDocument
    # TODO: Trả về dictionary với các key: document_id, source_type, author, category, content, timestamp
    return {
        'document_id': raw_json['docId'],
        'source_type': 'PDF',
        'author': raw_json.get('authorName', ''),
        'content': cleaned_content,
        'category': raw_json.get('doc_category', 'unknown'),
        'timestamp': raw_json.get('created_at', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    }

def process_video_data(raw_json: dict) -> dict:
    # TODO: Map dữ liệu thô từ Video sang định dạng chuẩn (giống PDF)
    # Lưu ý các key của Video: video_id, creator_name, transcript, category, published_timestamp
    return {
        'document_id': raw_json['video_id'],
        'source_type': 'Video',
        'author': raw_json.get('creator_name', 'unknown'),
        'content': raw_json.get('transcript', ''),
        'category': raw_json.get('category', 'unknown'),
        'timestamp': raw_json.get('created_at', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    }
