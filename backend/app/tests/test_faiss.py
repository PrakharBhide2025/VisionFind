from app.services.faiss_service import vector_search

def test_vector_search():
    res = vector_search(query_text="leaf", top_k=5)
    assert isinstance(res, list)
    assert len(res) == 5
