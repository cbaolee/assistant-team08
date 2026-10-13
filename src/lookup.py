import re

# Database of items/champions
DATABASE = [
    "B.F. Sword",
    "Caitlyn",
    "Infinity Edge",
    "Ahri"
]

def search(query: str, items: list[str] = DATABASE) -> list[str]:
    """Search items by substring or normalized abbreviation (e.g., ignoring punctuation)."""
    if not query:
        return []

    q_lower = query.lower()
    q_clean = re.sub(r'[^a-zA-Z0-9]', '', q_lower)
    results = []

    for item in items:
        # 1. Standard case-insensitive substring match
        if q_lower in item.lower():
            results.append(item)
            continue
        
        # 2. Normalized match (ignores dots, spaces, special chars like 'B.F. Sword' -> 'bfsword')
        cleaned_item = re.sub(r'[^a-zA-Z0-9]', '', item.lower())
        if q_clean and q_clean in cleaned_item:
            results.append(item)

    return results


# --- Tests ---
def test_search_functionality():
    # New Acceptance Test 1: 'bf' finds 'B.F. Sword'[cite: 1]
    assert "B.F. Sword" in search("bf"), "Test 1 Failed: 'bf' should find 'B.F. Sword'"
    
    # New Acceptance Test 2: 'cait' finds 'Caitlyn'[cite: 1]
    assert "Caitlyn" in search("cait"), "Test 2 Failed: 'cait' should find 'Caitlyn'"

    # Existing behavior validation[cite: 1]
    assert search("Ahri") == ["Ahri"]
    assert search("Edge") == ["Infinity Edge"]

    print("Acceptance criteria met: 2 new tests pass, no change to other answers.")[cite: 1]


if __name__ == "__main__":
    test_search_functionality()