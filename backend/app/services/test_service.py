from fastapi import HTTPException, status

def get_simple_test_text():
    try:
        return "test"        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in get_simple_test_text! {e}")