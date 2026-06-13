import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "INTJ": ("뮤츠", "🧠 전략적이고 독립적인 성향! 항상 큰 그림을 보며 계획을 세워요."),
    "INTP": ("후딘", "🔬 호기심이 많고 분석을 좋아하는 천재형이에요."),
    "ENTJ": ("리자몽", "🔥 리더십이 강하고 목표를 향해 돌진하는 타입!"),
    "ENTP": ("팬텀", "😎 창의적이고 재치 넘치는 아이디어 뱅크!"),

    "INFJ": ("루기아", "🌊 깊은 통찰력과 따뜻한 마음을 가진 이상주의자예요."),
    "INFP": ("이브이", "🌈 상상력이 풍부하고 순수한 감성을 가졌어요."),
    "ENFJ": ("피카츄", "⚡ 사람들을 밝게 만드는 인기쟁이 리더!"),
    "ENFP": ("뮤", "✨ 자유롭고 호기심 많은 모험가예요."),

    "ISTJ": ("거북왕", "🛡️ 책임감이 강하고 믿음직한 성향이에요."),
    "ISFJ": ("해피너스", "💖 배려심이 많고 주변 사람을 잘 챙겨요."),
    "ESTJ": ("괴력몬", "💪 추진력이 강하고 조직을 이끄는 능력이 뛰어나요."),
    "ESFJ": ("푸크린", "🎉 친절하고 사교적인 분위기 메이커!"),

    "ISTP": ("루카리오", "🥋 침착하고 실용적인 문제 해결사예요."),
    "ISFP": ("나인테일", "🌸 감성이 풍부하고 자신만의 매력이 있어요."),
    "ESTP": ("갸라도스", "🌪️ 대담하고 에너지 넘치는 액션파!"),
    "ESFP": ("꼬부기", "😆 밝고 즐거운 분위기를 만드는 엔터테이너!")
}

st.markdown(
    """
    <h1 style='text-align:center; color:#ffcc00;'>
    ⚡ MBTI 포켓몬 추천기 ⚡
    </h1>
    <h4 style='text-align:center;'>
    당신과 가장 잘 어울리는 포켓몬은 누구일까요? 🎮
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("💡 MBTI를 입력하고 버튼을 눌러보세요!")

mbti = st.text_input(
    "📝 MBTI 입력 (예: INFP)",
    max_chars=4
).upper()

if st.button("🔍 포켓몬 추천받기"):
    if mbti in pokemon_data:
        pokemon, desc = pokemon_data[mbti]

        st.balloons()

        st.success(f"🎊 당신과 가장 잘 어울리는 포켓몬은 **{pokemon}** 입니다!")

        st.markdown("---")

        st.markdown(
            f"""
            ## 🌟 추천 포켓몬: {pokemon}

            ### 📖 당신의 성향
            {desc}

            ### 🎯 한 줄 요약
            **{pokemon}처럼 자신만의 매력을 가진 특별한 사람!**
            """
        )

        st.info(
            "🎮 재미로 보는 추천 결과입니다. "
            "친구들의 MBTI도 입력해 보세요!"
        )

    else:
        st.error("❗ 올바른 MBTI를 입력해주세요. (예: ENFP, ISTJ)")
        st.write("가능한 MBTI: ")
        st.write(", ".join(sorted(pokemon_data.keys())))

st.markdown("---")
st.caption("✨ MBTI Pokémon Match Maker ✨")
