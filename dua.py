import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Daily Islamic Duas",
    page_icon="🕌",
    layout="wide"
)

# Custom CSS with Apple-style design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;500;600;700&display=swap');
    
    * {
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }
    
    .main {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .title-container {
        background: linear-gradient(135deg, #1a5f7a 0%, #088856 100%);
        padding: 2rem;
        border-radius: 50px;
        margin-bottom: 1rem;
        box-shadow: 0 10px 20px rgba(0,0,0,0.9);
        color: white;
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        color: #FFF940;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .section-header {
        font-size: 2rem;
        color: #FF940;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        margin: 2rem 0;
        font-weight: 600;
        letter-spacing: -0.5px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .dua-card {
        background: #ffffff;
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border: 1px solid #e9ecef;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .dua-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.15);
            color :blue;
    }
    
    .dua-title {
        font-size: 1.5rem;
        color: #fff940;
        margin-bottom: 1.5rem;
        font-weight: 600;
        letter-spacing: -0.5px;
    }
    
    .arabic-text {
        font-family: 'Traditional Arabic', 'Scheherazade', serif;
        font-size: 2rem;
        text-align: right;
        color: green;
        direction: rtl;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 15px;
        margin: 1rem 0;
        line-height: 1.8;
    }
    
    .transliteration-text {
        font-size: 1.1rem;
        color: purple;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 10px;
        margin: 1rem 0;
        line-height: 1.6;
    }
    
    .translation-text {
        font-size: 1.1rem;
        color: #453677;
        padding: 1rem;
        line-height: 1.6;
        border-left: 4px solid #086375;
        margin: 1rem 0;
        background: #f8f9fa;
        border-radius: 0 10px 10px 0;
    }
    
    .source-text {
        font-size: 0.9rem;
        color: red;
        font-style: italic;
        margin-top: 1rem;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 3rem;
        border-top: 1px solid #e9ecef;
    }
    
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
        }
        
        .section-header {
            font-size: 1.5rem;
        }
        
        .dua-card {
            padding: 1.5rem;
        }
        
        .arabic-text {
            font-size: 1.8rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("""
    <div class="title-container">
        <h1 class="main-title">🕌 Daily Islamic Duas 🕌 </h1>
    </div>
""", unsafe_allow_html=True)
st.markdown("""
    <div class="dua-card">
        <div class="translation-text">
            <strong>Important Note:</strong><br>
            Islam has put great stress on five times a day prayers in general and saying the prayers in the mosque in particular. 
            Therefore, a practicing Muslim enters and exits a mosque five times a day where he submits to Allah Almighty and 
            indulges in His prayer. It is imperative that a Muslim knows and understands the importance of being in the mosque 
            and recites particular Duas on respective actions.
        </div>
    </div>
""", unsafe_allow_html=True)

# Function to display a dua card
def display_dua(title, arabic, transliteration, translation, source=""):
    st.markdown(f"""
    <div class="dua-card">
        <h3 class="dua-title">{title}</h3>
        <div class="arabic-text">{arabic}</div>
        <div class="transliteration-text">
            <strong>Transliteration:</strong><br>
            {transliteration}
        </div>
        <div class="translation-text">
            <strong>Translation:</strong><br>
            {translation}
        </div>
        <div class="source-text">Source: {source}</div>
    </div>
    """, unsafe_allow_html=True)

# Sections with Duas
st.markdown("<h2 class='section-header'>When In Anger</h2>", unsafe_allow_html=True)
display_dua(
    "Seeking Refuge from Anger",
    "اَعُوْذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيْمِ",
    "A'oozu Bil'laahi Minash Shaitaanir Rajeem",
    "I seek refuge in Al'laah from Shaitaan the cursed",
    "Tirmizi Shareef Vol.2 Pg.183"
)

st.markdown("<h2 class='section-header'>Before and After Meals</h2>", unsafe_allow_html=True)
display_dua(
    "Before Meal",
    "بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيْمِ",
    "Bismil laahir Rahmaanir Raheem",
    "Al'laah's Name we begin with, The Compassionate, Most Merciful",
    ""
)

display_dua(
    "After Meal",
    "اَلْحَمْدُ للهِ الَّذِىْ اَطْعَمَنَا وَسَقَاناَ وَجَعَلَناَ مِنَ الْمُسْلِمِيْنَ",
    "Alhumdu lil laahil Lazee At'amana Wa Saqaana Wa Ja'alana Minal Muslimeen",
    "All Praise is due to Al'laah, who has blessed us with food and drink and made us from amongst the Believers (Muslims)",
    "Abu Dawood Pg.573"
)

# Add more sections as needed...
display_dua(
     "Entering Home",
       "بِسْمِ اللَّهِ وَلَجْنَا، وَبِسْمِ اللَّهِ خَرَجْنَا، وَعَلَى رَبِّنَا تَوَكَّلْنَا",
      "Bismillahi walajna, wa bismillahi kharajna, wa 'ala rabbina tawakkalna",    
    "In the name of Allah we enter, in the name of Allah we leave, and upon our Lord we rely"

)

display_dua(
    "Entering And Leaving Home",

" بِسْمِ اللهِ تَوَكَّلْتُ عَلىَ اللهِ وَلاَ حَوْلَ وَلاَ قُوَّةَ اِلاَّ بِاللهِ ط",

"Bismil laahi Tawak’kaltu Alal laahi Wa Laa Hawla Wa Laa Quw’wata il’la bil’laah",
"Al’laah’s Name we begin with, I place my (full) trust in Al’laah and there is no Might and Power except with Al’laah.",
" [Tirmizi Shareef Vol.2 Pg.180] Home is the base of a person from which a person exits to search and earn the blessings of Allah Almighty and it is a place where after the long day a person returns and shares those blessings with the family members. Therefore, it is imperative that a Muslim realizes the importance of leaving the home and then entering it.The Noble Prophet (Salla Allahu ta’ala ‘alayhi wa Sallam) said, whoso ever recites this dua before leaving his home, all his difficulties will go away and he shall be protected from the mischief of his enemies and shaitaan will stay away from him",

)
display_dua(
    "While Traveling",


 "سُبْحَنَ الَّذِىْ سَخَّرَلَنَا هَذَا وَ مَا كُنَّا لَهُ مُقْرِنِيْنْ وَ اِنَّا اِلَى رَبِّنَا لَمُنْقَلِبُوْنْ ",
  " Subhaanal lazee Sakh’khara Lana Haaza Wa Maa Kun’na Lahu Muqrineen. Wa In’na ilaa Rab’bina La Munqaliboon”.",
 "Glory be to Al’laah who has given us control over this (mode of transport) and without his Grace we would not have been able to control it and undoubtedly we are to return towards our Lord.Traveling is also an activity, which people undertake on daily basis. No matter how small a distance is or whatever means of traveling is to be adopted, there is always a concern of safety with traveling. Therefore, it is imperative that a person asks for the protection and safety of Allah Almighty.",
"[Tirmizi, Abu Dawood]"
)

display_dua(
"When Feeling Stressed",

"هَ اِلاَّ اللهُ الْحَلِيْمُ الْحَكِيْمُ لآَ اِلَهَ اِلاَّ اللهُ رَبُّ الْعَرْشِ   ",
"Laa ilaaha il’lal laahul Haleemul Hakeemu – Laa ilaaha il’lal laahu Rab’bul Arshil Azeem – Laa ilaaha il’lal laahu Rab’bus Samawaati wal Ardi wa Rab’bul Arshil Kareem.Due to all the competition and hard struggle during the day, it is quite natural that people become stressed. It is this stress that sometimes takes the shape of anger while in other times it causes depression, both of which are not favorable, hence it is imperative that a Muslim keeps control when under stress of pressure.  Pertaining to facing any discomfort or being unhappy about something, Prophet Muhammad (PBUH) used to recite the following Dua:",
"There is none worthy of worship except Al’laah, The Fore-bearing, The All Wise. There is none worthy of worship except Al’laah, The Lord of the Exalted Throne. There is none worthy of worship except Al’laah, The Lord of the Skies and The Lord of the Earth and the Lord of the distinguished Throne",
" [Tirmidhi Vol.2 Pg. 181]"

"This Dua under stress shows the submissiveness of a person to the Authority and Supremacy of Allah Almighty, which represents the ideology that only He is the one Who can provide relief or assistance during stressful and discomforting situations."
)
# Masjid Section
st.markdown("<h2 class='section-header'>Entering and Exiting Masjid</h2>", unsafe_allow_html=True)

display_dua(
    "When Entering the Mosque",
    "اللّهُـمَّ افْتَـحْ لي أَبْوابَ رَحْمَتـِك",
    "Allaahum-maf-Tahlee Abwaaba Rahmatika",
    "O Allaah, open the doors of Your Mercy for me",
    "Sahi'h Muslim"
)

display_dua(
    "When Leaving the Mosque",
    "اللّهُـمَّ إِنّـي أَسْأَلُكَ مِـنْ فَضْـلِك",
    "Allaahum-ma In-nee As`aluka Min Fadhlika",
    "O Allaah, I seek of You Your Grace",
    "Sahi'h Muslim"
)
# Sneezing Section
st.markdown("<h2 class='section-header'>When Sneezing</h2>", unsafe_allow_html=True)

display_dua(
    "Person who Sneezes should say",
    "الْحَمْدُ لِلَّهِ",
    "Alhamdulillah",
    "Thanks and all praise be to Allah",
    ""
)

display_dua(
    "Person who hears should respond",
    "يَرْحَمُكَ اللَّهُ",
    "Yar Hamoo kall Lah",
    "May Allah have mercy on you",
    "Bukhari, Mishkaat Shareef Pg.405"
)
st.markdown("""
    <div class="dua-card">
        <div class="translation-text">
            <strong>About Sneezing:</strong><br>
            Although most of the activities undertaken by us in our daily routine are intentional, there are few unintentional 
            things as well that happen to us every day. One of such things is the act of sneezing. The revival of breath after 
            a sneeze is also a blessing of Allah Almighty and a Muslim ought to say thanks for it. Moreover, besides the person 
            who sneezes, the other person who witnesses the sneeze must also respond to the Dua made by the sneezer.
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ for the Muslim Ummah<br>
        <small>May Allah accept our prayers</small>
    </div>
""", unsafe_allow_html=True)
