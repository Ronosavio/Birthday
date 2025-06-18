import streamlit as st

# Set page config
st.set_page_config(page_title="KID turned 13 !!!💛", page_icon="🌼")

# Initialize session states
if "passed_quiz" not in st.session_state:
    st.session_state.passed_quiz = False
if "pages" not in st.session_state:
    st.session_state.pages = 1
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "gave_chocolates" not in st.session_state:
    st.session_state.gave_chocolates = False

# --- Page 1: Quiz ---
if not st.session_state.passed_quiz and st.session_state.pages == 1:
    st.markdown("<h1 style='text-align: center; color: #FFC107;'>💛 Are ya Worthy to be 13?? 💛</h1>", unsafe_allow_html=True)

    st.audio(
        "https://raw.githubusercontent.com/Ronosavio/audio-files/master/ytmp3free.cc_ww-oiia-oiia-spinning-cat-youtubemp3free.org.mp3",
        format="audio/mp3"
    )

    questions = [
        {
            "q": "🌈 What's my favorite color?(it's in my language wahahaha)",
            "options": ["velupu", "karapu", "Manna", "Chomapu"],
            "answer": "Chomapu"
        },
        {
            "q": "🌙 What programming language do I code in?",
            "options": ["Java", "Python", "Viper", "Mark"],
            "answer": "Python"
        },
        {
            "q": "🎻 What instrument do I play?",
            "options": ["Cricket", "Flute", "Badminton", "Guitar"],
            "answer": "Guitar"
        },
        {
            "q": "🍭 What is my nickname?",
            "options": ["Nigga", "JoJo", "Appu", "Mojojo"],
            "answer": "Appu"
        },
        {
            "q": "🐣 What's my mother tongue?",
            "options": ["Kannada", "Hindi", "Malayalam", "Tamil"],
            "answer": "Malayalam"
        }
    ]

    score = 0
    responses = []

    st.write("Let's find out wahahaahaa 🎁")

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}: {q['q']}")
        choice = st.radio("Choose one:", [""] + q["options"], key=i)
        responses.append((choice, q["answer"]))

    if st.button("Proceed if ya think ya passed 🤪💫"):
        if any(c == "" for c, _ in responses):
            st.warning("Oi oi answer everything first,😤")
        else:
            for c, a in responses:
                if c == a:
                    score += 1

            if score == len(questions):
                st.success("🎉 Waaaw! 💛 You passed!!. Good job Kiddoo 🌙✨")
                st.balloons()
                st.session_state.passed_quiz = True
                st.session_state.pages = 2
                st.rerun()
            else:
                st.error(f"Oops! You got {score}/{len(questions)}, bobo ka!!🤭😝")

# --- Page 2: Chocolate Begging ---
elif st.session_state.passed_quiz and st.session_state.pages == 2:
    st.markdown("<h1 style='text-align: center; color: #F48FB1;'>🎁 It's your day hahaha 🎁</h1>", unsafe_allow_html=True)
    st.balloons()
    st.success("💛 YOU'RE OFFICIALLY 13-WORTHY HUH? 💥")
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGc1eW1wZDE4Z3NrY200cGdob2ttaWMyMnNzcjJkdDBmN2FxdjRxdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XbLeWvIwOcd2g/giphy.gif",
        use_container_width=True
    )

    st.markdown("---")
    st.subheader("🍫 That means treat!!...")

    excuses = [
        "🤩🤩🤩Chocolatoooo haha🤩🤩🤩",
        "😏, Guess you said no by mistake , Yes is on the left 🤭",
        "🤔 Mistake again ?? Kid focuss",
        "💀 That's a lot of mistakesss!!",
        "😢 But... You gotta give meee choclatess, it's your bday!",
        "🥺 Not gonna give me choclates huh??",
        "😖 What if I faint from lack of sugar? Do you want that??",
        "😭 My heart just cracked like a KitKat.",
        "😤 Be kind, rewind — and give me that chocolate!",
        "😩 This is emotional blackmail, and I'm not ashamed wahahahaa.",
        "🥵 If you say no again, I’ll cry in 3 different languages.",
        "😭 Don't womp womp MEEEEE!!!",
        "😈 Still no? I will haunt you throughout your whole existence!!!.",
        "💛 Please please please...!",
        "🫤 You give me no choice!!!",
        "🤪Bobo kaa, say yess now wahahaha!!!😝"
    ]

    excuse_index = min(st.session_state.no_count, len(excuses) - 1)

    with st.container():
        st.markdown(
            f"""
            <div style="border:2px dashed #FF69B4; padding:20px; border-radius:15px; background-color:#fffbea; color:#000;">
                <h3 style='color:#D81B60;'>Will you give all the chocolates to me? 🍬🍭🍫</h3>
                <p style="font-size:18px;">{excuses[excuse_index]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    col1, col2 = st.columns(2)

    with col2:
        if excuse_index < len(excuses) - 1:
            if st.button("No 😤 They're mine"):
                st.session_state.no_count += 1
                st.rerun()
        else:
            st.markdown(
                "<p style='font-size:16px; color:#D81B60;'>You've said no too many times...So I ate that button itself !!😁</p>",
                unsafe_allow_html=True
            )

    with col1:
        if st.button("Yes 😇 Take all"):
            st.session_state.gave_chocolates = True
            st.session_state.pages = 3
            st.rerun()

# --- Page 3: Final Party ---
elif st.session_state.gave_chocolates and st.session_state.pages == 3:
    st.markdown("<h1 style='text-align: center; color: #BA68C8;'>🍫 You gave me chocolates! You're officially 13 after all 💕</h1>", unsafe_allow_html=True)
    st.success("✨ OMG YESSSS! Chocosss 💛🍫")
    st.image(
        "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3Rocnp6YXd2amlyZ2htdjBnNmNjNDZ6NjV5YWw2dmFpbXRkNnQ0MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/242BalPH431y6H6a3A/giphy.gif",
        use_container_width=True
    )
    st.markdown("<p style='text-align:center;font-size:18px;'>Go eat cake now. Party starts 🎂🎉</p>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("🌟 Click me for a lil surprise?"):
        st.session_state.pages = 4
        st.rerun()
    

# --- Page 4: Nickname Guessing Game ---
elif st.session_state.pages == 4:
    nickname = "PIPPO"

    # Initialize session state
    if "guessed_letters" not in st.session_state:
        st.session_state.guessed_letters = [""] * len(nickname)
    if "current_letter_index" not in st.session_state:
        st.session_state.current_letter_index = 0

    idx = st.session_state.current_letter_index

    if idx < len(nickname):
        st.markdown("<h2 style='text-align: center; color: #FF4081;'>👀 Guess the letters of your nickname!!</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>Letter {idx + 1} of {len(nickname)}</h3>", unsafe_allow_html=True)

        guess = st.text_input(f"Type your guess for letter {idx + 1}", key=f"guess_{idx}").upper()

        if st.button("Submit Guess", key=f"submit_{idx}"):
            if guess == "":
                st.warning("Don't leave it blank! 😤")
            elif len(guess) > 1:
                st.warning("Only one letter please! 😅")
            elif guess == nickname[idx]:
                st.success(f"🎉 Yaay! '{guess}' is correct!")
                st.session_state.guessed_letters[idx] = guess
                st.session_state.current_letter_index += 1
                st.rerun()
            else:
                st.error("BOBOOOO!!!! Try again hehe 🐣")

        # Show current progress
        progress = [
            letter if letter != "" else "_" for letter in st.session_state.guessed_letters
        ]
        st.markdown(f"<h1 style='text-align: center; letter-spacing: 10px;'>{' '.join(progress)}</h1>", unsafe_allow_html=True)

    else:
        st.success("🎉 OMGGG YESSS! You completed the nickname 💛")
        st.balloons()
        st.markdown("<h1 style='text-align: center; color: #BA68C8;'>PIPPO 🐣</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;font-size:20px;'>I Named you PIPPO. 😛💛</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;font-size:20px;'>You will always be my  PIPPO. 🍭✨</p>", unsafe_allow_html=True)
        st.image(
        "https://i.pinimg.com/736x/03/7b/1d/037b1d44d35f13f46179101f801b0b90.jpg",
        use_container_width=True)
        if st.button("🌟 Click here to move forward haha"):
            st.session_state.pages = 5
            st.rerun()

elif st.session_state.pages == 5:
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🎂✨ Happy 13th Birthday, Kiddooo!!! ✨🎂</h1>", unsafe_allow_html=True)

    st.balloons()
    st.snow()  # Just for extra sparkle ❄️

    st.image(
        "https://i.pinimg.com/originals/72/3c/8a/723c8a768aa7c1e71c272df2fdcf1457.gif",
        caption="A magical birthday just for you! 🎈💛",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="background-color:#FFF3E0; padding:30px; border-radius:15px; border:2px solid #FFB74D;">
            <h2 style="text-align:center; color:#FF4081;">💛 Welcome to TEEN WORLD! 💫</h2>
            <p style="font-size:18px; color:#6D4C41; text-align:center;">
                From being the cutest little bean to now becoming a curious teen, <br>
                the journey ahead is gonna be full of laughter, secrets, and crazy dreams. 🐣<br><br>
                May your 13th be filled with sunshine, magic, chocolates, <br>
                and that special energy you bring around your people hehe. ✨<br><br>
                You have come a long way pippo and I am so proud of ya😁<br>
                <br>You’re officially a TEENAGER now. Own it. Slay it. Celebrate it!</br> 
                <br> And I will always be there to support ya no matter what haha 🍭<br>💥🎉
                <b> And always be kind to others and yourself 😌<b>
                <b>HAPPY BIRTHDAY PIPPOO🍭✨<b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("<h3 style='text-align:center;'>Here’s to beautiful years ahead, PIPPO 🐣💛</h3>", unsafe_allow_html=True)

    st.image(
    "https://raw.githubusercontent.com/Ronosavio/audio-files/master/1000124003.jpg",
    caption="I drew us btw haha I look soo cool😆 💛",
    use_container_width=True
)


    st.success("🌼 You’ve completed the test. Now go cut some cake and dance around cause you are worthy to be 13 Bobo Ka😝🐣 !! 💃")
