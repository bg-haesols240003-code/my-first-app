hobby_data = {
    "10대": {
        "name": "🎨 그림 그리기",
        "desc": "상상력과 창의력을 마음껏 표현할 수 있는 취미예요."
    },
    "20대": {
        "name": "📷 사진 찍기",
        "desc": "추억을 기록하고 새로운 시각을 키울 수 있어요."
    },
    "30대": {
        "name": "📚 독서",
        "desc": "지식과 통찰력을 넓히는 최고의 취미예요."
    },
    "40대": {
        "name": "🌱 식물 키우기",
        "desc": "일상 속 힐링과 여유를 느낄 수 있어요."
    },
    "50대": {
        "name": "🚶 산책",
        "desc": "건강을 챙기면서 기분 전환도 할 수 있어요."
    }
}

if st.button("✨ 취미 추천받기"):

    if 10 <= age < 20:
        group = "10대"
        comment = "🌈 창의력이 반짝이는 시기예요!"

    elif 20 <= age < 30:
        group = "20대"
        comment = "📸 새로운 경험을 많이 쌓아보세요!"

    elif 30 <= age < 40:
        group = "30대"
        comment = "📚 자기계발에 투자하기 좋은 시기예요!"

    elif 40 <= age < 50:
        group = "40대"
        comment = "🌿 여유와 힐링이 중요해지는 시기예요!"

    elif 50 <= age < 60:
        group = "50대"
        comment = "💪 건강을 챙기며 즐길 수 있는 취미가 좋아요!"

    else:
        st.warning("😊 이 앱은 현재 10대~50대를 대상으로 추천합니다.")
        st.stop()

    st.balloons()

    st.success(
        f"🎉 {group}에게 추천하는 취미는 **{hobby_data[group]['name']}** 입니다!"
    )

    st.markdown(f"""
### 🏆 추천 결과

#### {hobby_data[group]['name']}

📖 **취미 설명**
{hobby_data[group]['desc']}

💬 **한마디**
{comment}
""")
