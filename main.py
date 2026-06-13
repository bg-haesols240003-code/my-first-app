if st.button("✨ 취미 추천받기"):

    if age < 10:
        hobby = hobbies[0]  # 그림 그리기
        comment = "🧸 다양한 것을 경험하며 상상력을 키워보세요!"

    elif age < 20:
        hobby = hobbies[0]  # 그림 그리기
        comment = "🌈 창의력과 상상력이 풍부한 10대에게 딱 맞는 취미예요!"

    elif age < 30:
        hobby = hobbies[3]  # 사진 찍기
        comment = "📸 다양한 경험과 추억을 기록하기 좋은 시기예요!"

    elif age < 40:
        hobby = hobbies[1]  # 독서
        comment = "📚 자기계발과 새로운 지식을 쌓기에 좋은 나이예요!"

    elif age < 50:
        hobby = hobbies[4]  # 식물 키우기
        comment = "🌱 바쁜 일상 속에서 힐링과 여유를 느껴보세요!"

    elif age < 60:
        hobby = hobbies[5]  # 산책
        comment = "🚶 건강과 행복을 함께 챙길 수 있는 취미예요!"

    else:
        hobby = hobbies[2]  # 음악 감상
        comment = "🎵 여유롭게 음악을 즐기며 행복한 시간을 보내보세요!"

    st.balloons()

    st.success(f"🎉 추천 취미는 **{hobby['name']}** 입니다!")

    st.markdown("---")

    st.markdown(f"""
### 🏆 추천 결과

#### {hobby['name']}

📖 **취미 설명**
{hobby['desc']}

💬 **한마디**
{comment}
""")
