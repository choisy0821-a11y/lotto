import random
import streamlit as st


# 로또 공 색상을 지정하는 함수 (실제 로또 번호대별 색상 적용)
def get_ball_style(num):
    if num <= 10:
        bg_color = "#fbc400"  # 노란색 (1~10)
    elif num <= 20:
        bg_color = "#69c8f2"  # 파란색 (11~20)
    elif num <= 30:
        bg_color = "#ff7272"  # 빨간색 (21~30)
    elif num <= 40:
        bg_color = "#aaa"  # 회색 (31~40)
    else:
        bg_color = "#b0d840"  # 녹색 (41~45)

    # 원형 공 형태의 HTML 스타일 반환
    return f"""
    <div style="
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: {bg_color};
        color: white;
        font-weight: bold;
        font-size: 16px;
        margin: 4px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    ">{num}</div>
    """


# 앱 제목 설정
st.title("🎲 로또 번호 생성기")

# 세션 상태 초기화 (생성된 번호 세트 저장용)
if "lotto_sets" not in st.session_state:
    st.session_state.lotto_sets = []

# 버튼 레이아웃 설정
col1, col2 = st.columns([2, 1])

with col1:
    # '로또번호 생성' 버튼 클릭 시 동작
    if st.button("로또번호 생성"):
        # 최대 5개 세트까지만 유지
        if len(st.session_state.lotto_sets) >= 5:
            st.session_state.lotto_sets.pop(0)  # 가장 오래된 세트 삭제

        # 1~45 사이 중복 없는 6개 번호 추출 후 정렬
        new_numbers = sorted(random.sample(range(1, 46), 6))
        st.session_state.lotto_sets.append(new_numbers)

with col2:
    # 초기화 버튼 (필요 시 전체 리셋)
    if st.button("초기화"):
        st.session_state.lotto_sets = []

st.write("---")

# 생성된 번호 세트 화면에 출력 (최대 5개)
if st.session_state.lotto_sets:
    for idx, lotto in enumerate(st.session_state.lotto_sets, 1):
        # 공 모양 HTML 태그 생성 후 렌더링
        balls_html = "".join([get_ball_style(n) for n in lotto])
        st.write(f"**Game {idx}**")
        st.markdown(balls_html, unsafe_allow_html=True)
        st.write("")
else:
    st.info("버튼을 눌러 로또 번호를 생성해보세요! (최대 5개 세트)")