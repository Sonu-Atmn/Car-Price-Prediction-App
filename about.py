import streamlit as st

def About():




    st.markdown("""
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                color: #333;
            }

            header {
                background-color: #3D90D7;
                color: white;
                padding: 40px 20px;  /* Adjust the padding here */
                margin: 10px;
                text-align: center;
                border-radius: 15px; /* Rounded corners */
                box-shadow: 0 8px 8px rgba(0, 0, 0, 0.2); /* Shadow */
            }

            /* About Section */
            .about-section {
                background-color: #3D90D7;
                color: white;
                padding: 40px 20px;  /* Adjust the padding here */
                margin: 10px;
                text-align: center;
                border-radius: 15px; /* Rounded corners */
                box-shadow: 0 8px 8px rgba(0, 0, 0, 0.2); /* Shadow */
            }

            /* Features Section */
            .features-container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 30px;
                padding: 0;  /* Ensure no extra padding */
                margin: 0;  /* Remove margin */
            }

            .feature-box {
                background-color: white;
                border: 2px solid #3498db;
                border-radius: 8px;
                padding: 20px;
                width: 300px;
                text-align: center;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin: 10px;  /* Adjust margin here if needed */
            }

            .contact-section {
            background-color: #fff;
            text-align: center;
            padding: 50px 20px;
            }

            .contact-links {
                font-size: 18px;
            }

            .contact-links a {
                margin: 0 20px;
                display: inline-block;
            }

            .contact-links img {
                width: 40px;  /* Adjust the size of the logo */
                height: auto;
                transition: transform 0.3s;
            }

            .contact-links img:hover {
                transform: scale(1.2);  /* Add hover effect for logo */
            }
        </style>

        <!-- Content Here -->
        <header>
            <h1>Welcome to My App</h1>
            <p>An innovative app designed to automate the process of car price prediction. Using advanced algorithms, it analyzes your car's details and provides an instant, accurate price estimate. Perfect for buyers and sellers looking to make informed decisions.</p>
        </header>

        <!-- About Me Section -->
        <section class="about-section">
            <h2>About Me</h2>
            <p>Hi, I'm Sonu Agrawal, a passionate developer and AI enthusiast. I love building applications that solve real-world problems and make life easier. This app is a result of my dedication to creating something meaningful.</p>
        </section>

        <!-- Features Section -->
        <section class="section">
            <h2 style="text-align: center; font-size: 36px;">App Features</h2>
            <div class="features-container">
                <div class="feature-box">
                    <h3>Real-Time Predictions</h3>
                    <p>Get accurate predictions based on your car's details.</p>
                </div>
                <div class="feature-box">
                    <h3>User-Friendly Interface</h3>
                    <p>An intuitive interface makes it easy to use the app.</p>
                </div>
                <div class="feature-box">
                    <h3>Data-Driven Insights</h3>
                    <p>Understand the trends and patterns in car pricing.</p>
                </div>
            </div>
        </section>

        <!-- Contact Me Section -->
        <section class="contact-section">
            <h2>Contact Me</h2>
                <div class="contact-links">
                    <p>Feel free to reach out!</p>
                    <a href="https://github.com/Sonu-Atmn" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub Logo">
                    </a>
                    <a href="https://www.linkedin.com/in/sonu-agrawal-b5a326254/" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/108px-LinkedIn_icon.svg.png" alt="LinkedIn Logo">
                    </a>
                    <a href="mailto:sonuagrawalsun@gmail.com">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Email Logo">
                    </a>
                </div>
        </section>
    """, unsafe_allow_html=True)


