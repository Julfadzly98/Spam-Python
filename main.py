import pywhatkit
import time  # To add a delay between messages if needed




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


# Define the list of phone numbers in international format
phone_numbers = [
    "+60 19-305 0872", "+60 10-944 3177", "+60 14-933 9253", "+60 11-2623 0118", 
    "+60 13-377 9703", "+60 11-1126 5584", "+60 16-335 6255", "+60 13-555 3293",
    "+60 19-484 9410", "+60 16-577 8857", "+60 10-935 9026", "+60 11-2626 1077",
    "+60 19-123 4567", "+60 12-345 6789", "+60 11-987 6543", "+60 14-111 2222",
    "+60 16-333 4444", "+60 17-555 6666", "+60 18-777 8888", "+60 19-999 0000",
]  # Replace with actual phone numbers




# Loop through numbers and send messages
for number in phone_numbers:
    try:
        print(f"Sending message to {number}")
        kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
        
        # Optional: Small delay to prevent excessive requests
        time.sleep(5)  # 5-second delay between messages
        
    except Exception as e:
        print(f"Failed to send message to {number}: {e}")
