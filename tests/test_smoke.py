import pytest

def test_environment_setup():
    """Smoke test cơ bản để đảm bảo test runner hoạt động."""
    assert True, "Môi trường test đã được thiết lập thành công."

def test_dummy_tft_data():
    """Kiểm tra khả năng khởi tạo dữ liệu giả lập cho TFT."""
    dummy_comp = ["Ahri", "Yasuo", "Syndra", "Thresh"]
    assert len(dummy_comp) == 4, "Đội hình giả lập phải có 4 tướng."