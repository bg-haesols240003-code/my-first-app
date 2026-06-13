import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🌟 나이별 취미 추천기",
    page_icon="🎨",
    layout="centered"
)

# 제목
st.markdown(
    """
    <h1 style='text-align:center;'>🌟 나이별 취미 추천기 🌟</h1>
    <h4 style='text-align:center;'>나이를 입력하면 딱 맞는 취미를 추천해 드려요!</h4>
    """,
    unsafe_allow_html=True
)

st.write("")

# 나이 입력
age = st.number_input(
    "🎂 나이를 입력하세요",
    min_value=10,
    max_value=59,
    step=1
)

# 추천 버튼
if st.button("✨ 취미 추천받기"):

    if 10 <= age < 20:
        hobby = "🎨 그림 그리기"
        description = "상상력과 창의력을 마음껏 표현할 수 있는 취미예요."
        comment = "🌈 창의력이 반짝이는 10대에게 딱!"

    elif 20 <= age < 30:
        hobby = "📷 사진 찍기"
        description = "일상의 특별한 순간을 기록하고 추억을 남길 수 있어요."
        comment = "📸 새로운 경험을 많이 쌓는 20대에게 추천!"

    elif 30 <= age < 40:
        hobby = "📚 독서"
        description = "지식과 통찰력을 넓히고 자기계발에 도움을 줘요."
        comment = "🧠 성장하는 30대에게 잘 어울려요!"

    elif 40 <= age < 50:
        hobby = "🌱 식물 키우기"
        description = "식물이 자라는 모습을 보며 힐링과 여유를 얻을 수 있어요."
        comment = "🌿 바쁜 일상 속 작은 쉼표!"

    else:  # 50대
        hobby = "🚶 산책"
        description = "건강도 챙기고 기분 전환도 할 수 있는 최고의 취미예요."
        comment = "💪 건강과 행복을 함께 챙겨보세요!"

    # 풍선 효과
    st.balloons()

    # 결과 출력
    st.success(f"🎉 추천 취미는 **{hobby}** 입니다!")

    st.markdown("---")

    st.markdown(
        f"""
        ## 🏆 추천 결과

        ### {hobby}

        📖 **취미 설명**
        
        {description}

        💬 **한마디**
        
        {comment}
        """
    )

st.markdown("---")
st.caption("✨ 오늘도 즐거운 취미 생활 되세요! ✨")
