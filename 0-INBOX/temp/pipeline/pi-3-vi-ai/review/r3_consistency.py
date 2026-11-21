"""r3 review helper: count how often each Vietnamese item rendering used in pi-3 ch 8-15 occurs in
the approved pi-1 / pi-2 Vietnamese and in pi-3 ch 1 (uddeso). Console only; writes nothing.
Usage: python -I -X utf8 r3_consistency.py [term ...]   (with terms: print pi-1/pi-2 context lines for them)
"""
import re, sys
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
F1 = ROOT / r"AI_translation\vietnamese\pi-1-vietnamese-plain.md"
F2 = ROOT / r"AI_translation\vietnamese\pi-2-vietnamese-plain.md"
U = ROOT / r"AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\1-uddeso.md"

TERMS = """khối vật chất|khối cảm giác|khối tri giác|khối tạo tác|khối thức|lĩnh vực ý|lĩnh vực mắt|lĩnh vực vật xúc chạm|lĩnh vực đối tượng của ý|yếu tố mắt|yếu tố vật xúc chạm|yếu tố thức qua mắt|yếu tố thức qua tai|yếu tố thức qua mũi|yếu tố thức qua lưỡi|yếu tố thức qua thân|yếu tố ý thức|yếu tố ý|yếu tố đối tượng của ý|sự thật về khổ đau|sự thật về sự phát sinh|sự thật về sự chấm dứt|sự thật về con đường|năng lực mắt|năng lực thân|năng lực nữ tính|năng lực nam tính|năng lực sống|năng lực ý|năng lực dễ chịu|năng lực khó chịu|năng lực niềm vui|năng lực nỗi buồn|năng lực bình thản|năng lực niềm tin|năng lực tinh tấn|năng lực tỉnh thức|năng lực định tâm|năng lực trí tuệ|năng lực biết được điều chưa từng biết|năng lực hiểu biết trọn vẹn|năng lực của người đã hiểu biết trọn vẹn|vô minh làm điều kiện cho các sự tạo tác|các sự tạo tác làm điều kiện cho thức|thức làm điều kiện cho phần tinh thần và vật chất|sáu lĩnh vực nhận biết làm điều kiện cho sự tiếp xúc|sự tiếp xúc làm điều kiện cho cảm giác|cảm giác làm điều kiện cho khao khát|khao khát làm điều kiện cho sự bám víu|sự hiện hữu dưới dạng nghiệp|sự hiện hữu dưới dạng tái sinh|sự hiện hữu ở cõi dục lạc|sự hiện hữu ở cõi hình sắc|sự hiện hữu ở cõi không hình sắc|sự hiện hữu có tri giác|sự hiện hữu không có tri giác|sự hiện hữu không phải có tri giác cũng không phải không tri giác|sự hiện hữu gồm một khối|sự hiện hữu gồm bốn khối|sự hiện hữu gồm năm khối|sự sinh|sự lão hóa|sự chết|sự sầu muộn|sự than khóc|nỗi buồn|sự tuyệt vọng|sự thiết lập tỉnh thức|nỗ lực đúng đắn|nền tảng thần thông|tầng thiền|trạng thái không thể đo lường|năm năng lực|năm sức mạnh|bảy chi phần giác ngộ|con đường cao quý gồm tám chi phần|sự quyết định|sự chú tâm|chủ ý|phần tinh thần và vật chất|không xác định về mặt đạo đức|có khả năng sinh ra quả|là quả của nghiệp|không phải là quả của nghiệp cũng không có khả năng sinh ra quả|do nghiệp tạo ra và là đối tượng của sự bám víu|không do nghiệp tạo ra nhưng là đối tượng của sự bám víu|không do nghiệp tạo ra và không phải là đối tượng của sự bám víu|bị phiền não làm vẩn đục và là đối tượng của phiền não|không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não|không bị phiền não làm vẩn đục và không phải là đối tượng của phiền não|có sự hướng tâm và sự duy trì tâm|không có sự hướng tâm, chỉ có sự duy trì tâm|không có sự hướng tâm cũng không có sự duy trì tâm|có sự hân hoan đi kèm|có hạnh phúc đi kèm|có sự bình thản đi kèm|cần dứt bỏ bằng sự thấy chân lý|cần dứt bỏ bằng sự tu tập|không cần dứt bỏ bằng sự thấy chân lý cũng không cần dứt bỏ bằng sự tu tập|có gốc rễ cần dứt bỏ bằng sự thấy chân lý|có gốc rễ cần dứt bỏ bằng sự tu tập|dẫn đến sự tích lũy|dẫn đến sự giảm trừ|không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ|thuộc về người còn đang tu học|thuộc về người đã hoàn tất tu học|hạn hẹp|rộng lớn|không thể đo lường|có đối tượng hạn hẹp|có đối tượng rộng lớn|có đối tượng không thể đo lường|thấp kém|trung bình|ưu việt|cố định theo hướng sai lầm|cố định theo hướng đúng đắn|không cố định|lấy con đường làm đối tượng|lấy con đường làm gốc rễ|lấy con đường làm yếu tố chủ đạo|đã sinh khởi|chưa sinh khởi|sẽ sinh khởi|có đối tượng thuộc quá khứ|có đối tượng thuộc tương lai|có đối tượng thuộc hiện tại|ở nơi bản thân|ở bên ngoài bản thân|có đối tượng ở nơi bản thân và ở bên ngoài bản thân|thấy được và có tính va chạm|không thấy được nhưng có tính va chạm|là gốc rễ|có gốc rễ|gắn liền với gốc rễ|vừa là gốc rễ vừa có gốc rễ|có gốc rễ nhưng không phải là gốc rễ|vừa là gốc rễ vừa gắn liền với gốc rễ|gắn liền với gốc rễ nhưng không phải là gốc rễ|không phải là gốc rễ nhưng có gốc rễ|không phải là gốc rễ và không có gốc rễ|không có điều kiện|không do điều kiện tạo thành|thấy được|có tính va chạm|thuộc vật chất|phi vật chất|thuộc thế gian|vượt thế gian|là ô nhiễm|là đối tượng của ô nhiễm|vừa là ô nhiễm vừa là đối tượng của ô nhiễm|vừa là ô nhiễm vừa gắn liền với ô nhiễm|gắn liền với ô nhiễm nhưng không phải là ô nhiễm|không gắn liền với ô nhiễm nhưng là đối tượng của ô nhiễm|không gắn liền với ô nhiễm và không phải là đối tượng của ô nhiễm|xiềng xích|nút thắt|dòng lũ|ách|chướng ngại|sự hiểu sai lệch|bị sự hiểu sai lệch nắm giữ|có đối tượng|không có đối tượng|yếu tố đồng hành với tâm|hòa lẫn với tâm|do tâm sinh ra|cùng tồn tại với tâm|vận hành theo tâm|vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm|thuộc phần bên ngoài|phái sinh|do nghiệp tạo ra|sự bám víu|phiền não|bị phiền não làm vẩn đục|là đối tượng của phiền não|có sự hân hoan|thuộc cõi dục lạc|thuộc cõi hình sắc|thuộc cõi không hình sắc|nằm trong các cõi tồn tại|không nằm trong các cõi tồn tại|dẫn đến giải thoát|không dẫn đến giải thoát|cố định|còn có điều cao hơn|không có điều gì cao hơn|có xung đột|không có xung đột""".split("|")


def main():
    t1 = F1.read_text(encoding="utf-8"); t2 = F2.read_text(encoding="utf-8"); tu = U.read_text(encoding="utf-8")
    if len(sys.argv) > 1:
        for term in sys.argv[1:]:
            for name, t in (("pi-1", t1), ("pi-2", t2), ("pi-3 ch1", tu)):
                hits = [l for l in t.split("\n") if term in l]
                print(f"--- {term!r} in {name}: {len(hits)} lines")
                for l in hits[:3]:
                    i = l.index(term)
                    print("    …" + l[max(0, i - 80): i + len(term) + 80] + "…")
        return
    for term in TERMS:
        c1, c2, cu = t1.count(term), t2.count(term), tu.count(term)
        flag = "" if (c1 or c2) else "   <-- not in pi-1/pi-2"
        print(f"{c1:5d} {c2:5d} {cu:4d}  {term}{flag}")


if __name__ == "__main__":
    main()
