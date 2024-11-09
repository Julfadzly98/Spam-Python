import pywhatkit
import time  # To add a delay between messages if needed

# Define the list of phone numbers in international format
phone_numbers = ["+60168300256"]  # Replace with actual phone numbers




message = """ 

Hello Everyone! 😄

We are from Einstronic Enterprise Sdn Bhd and we're thrilled to announce the launch of our new EduTech journey – Maker Nation! 🥳🎊🎉

At Maker Nation, we’re all about hands-on STEM learning, and we’ve set up a series of workshop training sessions to dive into Arduino, IoT, Microbit, Robotics, AI, and 3D Printing. Our sessions are designed for both educators and enthusiasts eager to learn practical tools, fresh insights, and innovative strategies. 🌟

📚 Our Workshop Classes Include:
- Arduino Beginner & Starter
- IoT Project with ESP32
- Microbit Basic
- 3D Modelling & Printing
- Introduction to AI with IoT
- Robot Car - Sumo / Tracer
And MANY MORE! 🤩

👉 If you would like to know more, please join our WhatsApp group to stay updated on classes, events and offers - https://chat.whatsapp.com/DEOT8MxiqlTA6yh4bc8Bzz

🏢 We’re officially open at Donggongon Square, Pekan Donggongon, Penampang! Find us here at - https://maps.app.goo.gl/V6j1L98n95tfYsHV7

🕘 Our Workshop Schedule:
- Monday - Friday: 9:00 am - 4:00 pm
- Saturday: 9:00 am - 2:00 pm

🔥 We’re even offering a 1-Hour FREE Trial Class for anyone wanting to get a taste of what we’re about! 🤩

👀 Why Join Us?
This isn’t just another training – it’s a unique opportunity to grow professionally, connect with like-minded educators, and discover techniques that can transform your classrooms. Together, we’ll explore ways to engage students, foster their curiosity, and make learning memorable.

What You’ll Gain:
✅ Inspiring Ideas and Strategies: New approaches for engaging students, managing classrooms, and enhancing learning outcomes.
✅ Hands-On Activities: Practical exercises and real-world applications you can implement immediately.
✅ A Supportive Network of Teachers: Collaborate, share experiences, and find encouragement among fellow educators.
Let’s support one another in this shared mission to inspire young minds!

If you’re ready to bring fresh energy into your teaching and make a real impact, we’d love for you to join us. Feel free to reach out if you have any questions or need more details – I’m here to help! 😊

👉 Join our WhatsApp group to stay updated on classes, events and offers - https://chat.whatsapp.com/DEOT8MxiqlTA6yh4bc8Bzz

Looking forward to learning, growing, and inspiring together! 🤩

If you have any questions, feel free to call or personally chat with our person in-charge contact number:
- 0163056563 (Mr. MakerNation)

Warm regards,
Maker Nation
Einstronic Enterprise Sdn Bhd


 """






# Loop through each phone number and send the message instantly
for phone_number in phone_numbers:
    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        print(f"Message sent successfully to {phone_number}!")
        # Add a short delay to avoid sending messages too close together
        time.sleep(10)  # Adjust delay as necessary
    except Exception as e:
        print(f"An error occurred while sending to {phone_number}: {e}")
