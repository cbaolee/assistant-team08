
def test_environment_setup():
    """Smoke test cơ bản để đảm bảo test runner hoạt động."""
    assert True, "Môi trường test đã được thiết lập thành công."

def test_dummy_tft_data():
    """Kiểm tra khả năng khởi tạo dữ liệu giả lập cho TFT."""
    dummy_comp = ["Ahri", "Yasuo", "Syndra", "Thresh"]
    assert len(dummy_comp) == 4, "Đội hình giả lập phải có 4 tướng."

import json
import os


def test_lookup_new_comps():
    """Kiểm tra file comps.json hợp lệ và chứa Exalted, Storyweaver."""
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'comps.json')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        comps = json.load(f)
    
    comp_names = [comp["name"] for comp in comps]
    
    assert "Exalted Flex" in comp_names, "Thiếu đội hình Exalted Flex"
    assert "Storyweaver Reroll" in comp_names, "Thiếu đội hình Storyweaver Reroll"