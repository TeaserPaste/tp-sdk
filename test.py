# Cách dùng tối ưu với bản mới (Sync)
import tp
from tp.models import SnippetInput, Expiry

# Dùng with để tự động đóng kết nối
with tp.TeaserPaste("API_KEY") as api:
    # Auto-completion sẽ hoạt động tốt ở đây nhờ Enum
    api.paste(SnippetInput(
        title="New Code", 
        content="Hello", 
        expires=Expiry.HOUR_1 
    ))

    # Lấy tất cả snippet mà không cần lo về phân trang (skip/limit)
    for snippet in api.ls_iter():
        print(snippet) # In ra đẹp hơn nhờ __repr__