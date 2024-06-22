# import qrcode      
# from PIL import Image      #Image file import from pil
# import qrcode.constants    #constants module return constants and solve error
# qr = qrcode.QRCode(version=1,          #version(1-40)  #qrcode.QRCode হল Python লাইব্রেরি qrcode-এর একটি ক্লাস, যা QR কোড তৈরি করার জন্য ব্যবহৃত হয়। এই ক্লাসটি ব্যবহার করে আপনি সহজেই QR কোড তৈরি করতে এবং সেটিকে বিভিন্ন আকার ও কনফিগারেশনে কাস্টমাইজ করতে পারেন।
#                    error_correction = qrcode.constants.ERROR_CORRECT_H,
#                    box_size = 10,border=10,)            #সর্বোচ্চ স্তরের ত্রুটি সংশোধন ব্যবহার করা হয়েছে যা কোডের ৩০% পর্যন্ত ক্ষতিগ্রস্ত হলে পুনরুদ্ধার করতে পারে।
# qr.add_data("https://www.google.com/imghp?hl=ja&tab=ri&ogbl")    #whixh link we want to make qr
# qr.make(fit =True)
# img = qr.make_image(fill_color ="red", back_color ="white")  #fit=True মানে QR কোডের সমস্ত ডাটা যথাযথভাবে ফিট করার জন্য এর আকার স্বয়ংক্রিয়ভাবে সামঞ্জস্য করা হবে।
# img.save("google.png")

import qrcode
from PIL import Image
import qrcode.constants
qr = qrcode.QRCode(version=8,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 7, border = 10,)
qr.add_data = ("https://www.google.com/imghp?hl=ja&tab=ri&ogbl")
qr.make(fit = True)
img = qr.make_image(fill_color = "green", back_color = "red")
img.save("google.jpg")